# Python SDK UAT guide

End-to-end validation of the published Python SDK: install from PyPI, authenticate, submit an interaction, and confirm it reached the Exchange.

Each step says what "good" looks like, so you can tell a real failure from
expected output.

---

## 1. Prerequisites

- **Python 3.8 or later**
- **An Interactions API key for production.** See
  [Authentication](https://docs.movementinfrastructure.org/docs/interactions-api-authentication).

Your key should look like `12345.<secret>`: a numeric key ID, a dot, then a base64
secret. **Both halves are required.**

Keys are environment-specific. A key issued for the public test server will not
work against production.

```bash
export DDX_API_KEY='12345.your-secret-here'
```

Check the shape before going further:

```bash
python3 - <<'PY'
import base64, os

parts = os.environ["DDX_API_KEY"].split(".", 1)
print("key id numeric:", kid.isdigit())
try:
    if not secret:
        raise ValueError("no dot separator in key")
    base64.b64decode(secret, validate=True)
    print("secret is valid base64: True")
except Exception as e:
    print("secret is NOT valid base64:", e)
PY
```

Both must be true.

---

## 2. Install from PyPI into a clean environment

```bash
mkdir -p /tmp/ddx-uat && cd /tmp/ddx-uat
python3 -m venv .venv
source .venv/bin/activate

pip install ddx-interactions-api
```
### Expected result

```bash
pip show ddx-interactions-api | grep -E '^(Name|Version)'
#   Name: ddx-interactions-api
#   Version: <latest release>
```

The install name is hyphenated; the import name is underscored
(`import ddx_interactions_api`).

---

## 3. Authenticate, and check what your key can reach

```bash
python - <<'PY'
import os
import ddx_interactions_api as sdk

cfg = sdk.Configuration(
    username="",                                   # empty on purpose
    password=os.environ["DDX_API_KEY"],
)
print("target:", cfg.host)

with sdk.ApiClient(cfg) as client:
    me = sdk.AuthenticationDetailsApi(client).vversion_auth_me_get("1")

print("workspace:   ", me.workspace.display_name, f"({me.workspace.workspace_id})")
print("destinations:", me.destinations or "none")
print("van key:     ", "present" if me.van_api_key else "none")
PY
```

`Configuration` takes no `host`, so it defaults to production
(`https://api.movementinfrastructure.org`).

### Expected Result

`target:` prints the production host, and your workspace name and ID print
without an exception.

**Read the `destinations` and `van key` lines before continuing.** They decide
what step 4 actually does:

- **Both empty** - interactions land in the Exchange and go no further.
- **Either populated** - what you submit is forwarded to those systems, and for
  VAN that means real canvass responses. Coordinate before submitting.

Authentication is HTTP Basic with the **API key in the password field and an
empty username**. That surprises people; it is correct.

---

## 4. Submit an interaction

Replace `vendorSource`, `committee`, and `person` with identifiers your
workspace actually has. Left as placeholders they will be rejected.

```bash
python - <<'PY'
import json, os
from datetime import datetime, timezone
import ddx_interactions_api as sdk

cfg = sdk.Configuration(username="", password=os.environ["DDX_API_KEY"])
stamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

payload = sdk.InteractionsDto.from_dict({"interactions": [{
    "stateCode": "CA",
    "attemptDateTime": stamp,
    "method": "phone_call",
    "outcome": "successful_contact",
    "vendorSource": "<your vendor name>",
    "committee": [{"type": "<your type>", "id": "<your committee id>"}],
    "person":    [{"type": "<your type>", "id": "<your person id>"}],
    "jsonMetadata": json.dumps({"uat": True, "posted_at": stamp}),
}]})

with sdk.ApiClient(cfg) as client:
    api = sdk.InteractionsApi(client)
    result = api.vversion_interactions_post("1", interactions_dto=payload)

print("correlationId:", result.correlation_id)
print("accepted:", result.accepted_interactions.count,
      " rejected:", result.rejected_interactions.count)
for row in (result.accepted_interactions.data or []):
    print(f"  accepted idx {row.index}: interactionId {row.interaction_id}")
for row in (result.rejected_interactions.data or []):
    for err in (row.errors or []):
        print(f"  rejected idx {row.index}: {err.var_field}: {err.error_message}")

PY
```

### Expected Result

A `correlationId`, and `accepted` equal to the number of rows you sent.

**Keep an `interactionId`** from the accepted list. Step 5 exports it.

A mixed batch returns **HTTP 207** rather than 200. That is expected, not an
error: the result object is populated either way, and
`rejected_interactions.data[].errors` carries the per-row reason.

The cap is **100 interactions per request**.

### Valid enum values

- `method`: `unknown`, `mail`, `letter`, `digital_ad`, `email`, `text`,
  `text_broadcast`, `robo_call`, `dialer_call`, `phone_call`, `door_knock`,
  `Event`, `hot_spot`, `one_on_one`, `web_interaction`
- `outcome`: `unknown`, `clicked_link`, `email_opened`, `submitted_form`,
  `successful_contact`, `deceased`, `deliverability_error`,
  `permanently_undeliverable`, `inaccessible`, `language_barrier`, `moved`,
  `no_answer`, `wrong_number`, `hostile`, `marked_spam`, `refused`,
  `delivered`, `lit_drop`, `left_message`, `other`

`Event` is the one capitalised value, exactly as written.

---

## 5. Put the interaction ID in your environment

```bash
export INTERACTION_ID='<interactionId from step 4>'
```

---

## 6. Look up the interaction's transaction records

```bash
python - <<'PY'
import os
import ddx_interactions_api as sdk

cfg = sdk.Configuration(username="", password=os.environ["DDX_API_KEY"])

with sdk.ApiClient(cfg) as client:
    txns = sdk.InteractionsApi(client).vversion_interactions_interaction_id_transactions_get(
        os.environ["INTERACTION_ID"], "1", show_only_failed_transactions=False)

print("count:", txns.metadata.count if txns.metadata else 0)
for row in (txns.data or []):
    print(f"  {row.date_created_utc}  {row.status}")
    for log in (row.logs or []):
        print(f"      HTTP {log.response_status_code}  {log.response}")
PY
```

### Expected Result

The call returns immediately. What it contains depends on where your workspace
sends interactions, which step 3 told you:

- **Destinations or a VAN key present**: a row per delivery attempt, each with a
  status of `Received`, `Processing`, `Success`, `Failed`, `Invalid`,
  `Duplicate`, or `InternalError`, plus any response logs recorded for it.
- **Neither present**: `count: 0` and no rows. Transaction records are written
  when an interaction is forwarded to an external system such as VAN. An
  interaction that stops at the Exchange never gets one.

`count: 0` is a valid result, not a failure. What this step verifies is that the
call authenticates, returns a parsed response, and reports whatever records
exist for the interaction you submitted.

`show_only_failed_transactions` is set to false on purpose. It defaults to true,
which returns only `Failed`, `Invalid`, and `Duplicate` rows and would hide a
successful delivery.

Exchange delivery is reported by a different endpoint,
`interactions/exchange-status`. It advances on a scheduled transformation rather
than on your request and can lag by up to an hour, so it is outside this UAT.

The interactive reference is at
[docs.movementinfrastructure.org/reference](https://docs.movementinfrastructure.org/reference/interactions).

---

## 7. Where the model docs live

`docs/*.md` are not shipped inside the package. The model links on the PyPI
project page point back at this repo, and the interactive reference is at
[docs.movementinfrastructure.org/reference](https://docs.movementinfrastructure.org/reference/interactions).

---

## 8. Common failure modes

| Symptom | Likely cause |
|---|---|
| `401 Unauthorized`, empty body | Key missing the `<keyId>.` prefix; secret not valid base64; key issued for a different environment; key revoked or expired; workspace suppressed; or the key lacks the required role. |
| `ValidationError` before any request | A bad `method` or `outcome`. Validated client-side, so the batch never leaves your machine. |
| Rows rejected with a per-row error | Per-row validation. Read `rejected_interactions.data[].errors`. |
| `404` from step 6 | You passed the `correlationId`. That route takes a GUID `interactionId` only, and correlation IDs are either a numeric trace ID or `mig-` prefixed. Use an ID from the accepted list in step 4. |
| Step 6 returns `count: 0` | Either the workspace sends nowhere external, so no transaction record is ever written, or `show_only_failed_transactions` was left at its default of true. |

### On that 401

The 401 is deliberately generic and covers several distinct causes: including
a **valid key that simply lacks the required role**, which is an authorization
failure reported as an authentication one. If the key shape checks out in
step 1, ask the API team to check server-side logs rather than guessing. Quote
the `x-correlation-id` response header.

---

## 9. Sign-off checklist

- [ ] Installed from PyPI into a clean virtualenv
- [ ] `auth/me` returned the expected workspace
- [ ] Reviewed `destinations` / `van key` before submitting
- [ ] Submitted an interaction and received a `correlationId`
- [ ] Rejected rows, if any, reported a usable per-row reason
- [ ] Retrieved transaction records for an accepted `interactionId`,
      with `show_only_failed_transactions` set to false
- [ ] Filed anything unexpected, with version and `correlationId`
