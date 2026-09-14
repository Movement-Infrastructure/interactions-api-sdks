# Python SDK UAT guide

End-to-end validation of the published Python SDK against **production**:
install from PyPI, authenticate, submit an interaction, and confirm it reached
the Exchange.

Each step says what "good" looks like, so you can tell a real failure from
expected output.

**Report anything that does not match** on the
[Mercury SDKs project](https://linear.app/ddx/project/mercury-sdks-4d0ee2eb499d),
or open an issue on this repo. Include the package version, the command you
ran, and the `correlationId` or the `x-correlation-id` response header.

> **This guide targets production.** There is no dry-run mode and no test flag.
> Anything the API accepts is a real record, and if your key has Destinations
> configured it is forwarded to those systems. Step 3 tells you how to check
> that before you submit anything.

---

## 1. Prerequisites

- **Python 3.8 or later**
- **An Interactions API key for production.** See
  [Authentication](https://docs.movementinfrastructure.org/docs/interactions-api-authentication).

Your key looks like `12345.<secret>` — a numeric key ID, a dot, then a base64
secret. **Both halves are required.** A bare secret is rejected before the key
is looked up, with a generic 401.

Keys are environment-specific. A key issued for the public test server will not
work against production.

```bash
export DDX_API_KEY='12345.your-secret-here'
```

Check the shape before going further:

```bash
python3 -c "
import base64, os
kid, _, secret = os.environ['DDX_API_KEY'].partition('.')
print('key id numeric:', kid.isdigit())
try:
    base64.b64decode(secret, validate=True); print('secret is valid base64: True')
except Exception as e:
    print('secret is NOT valid base64:', e)
"
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

### What good looks like

```bash
pip show ddx-interactions-api | grep -E '^(Name|Version)'
#   Name: ddx-interactions-api
#   Version: <latest release>
```

pip should report `Collecting ddx-interactions-api` from PyPI, not a local
path — that is what proves you are testing the published artifact.

The install name is hyphenated; the import name is underscored
(`import ddx_interactions_api`).

---

## 3. Authenticate, and check what your key can reach

The smallest call that proves connectivity, credentials, and deserialization
work together — and it tells you how far a submission will travel.

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

### What good looks like

`target:` prints the production host, and your workspace name and ID print
without an exception.

**Read the `destinations` and `van key` lines before continuing.** They decide
what step 4 actually does:

- **Both empty** — interactions land in the Exchange and go no further.
- **Either populated** — what you submit is forwarded to those systems, and for
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
for row in (result.rejected_interactions.data or []):
    for err in (row.errors or []):
        print(f"  rejected idx {row.index}: {err.field_name}: {err.error_message}")
PY
```

### What good looks like

A `correlationId`, and `accepted` equal to the number of rows you sent.

**Keep the `correlationId`** — it is the only handle for step 5.

A mixed batch returns **HTTP 207** rather than 200. That is expected, not an
error: the result object is populated either way, and
`rejected_interactions.data[].errors` carries the per-row reason.

The cap is **100 interactions per request**.

### Valid enum values

These are **not** shipped in the package, and a bad value fails locally before
any request is sent:

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

## 5. Verify it reached the Exchange

```bash
CORRELATION_ID=<id from step 4> python - <<'PY'
import os
import ddx_interactions_api as sdk

cfg = sdk.Configuration(username="", password=os.environ["DDX_API_KEY"])

with sdk.ApiClient(cfg) as client:
    statuses = sdk.InteractionsApi(client).vversion_interactions_exchange_status_get(
        "1", correlation_id=os.environ["CORRELATION_ID"], limit=100)

for row in (statuses.data or []):
    print(f"  {row.interaction_id}  {row.status}")
PY
```

### What good looks like

One row per accepted interaction, progressing to a terminal status.

The Exchange is asynchronous, so an immediate call may return an early status
or no rows. Re-run after a few seconds before calling it a failure.

The interactive reference is at
[docs.movementinfrastructure.org/reference](https://docs.movementinfrastructure.org/reference/interactions).

---

## 6. Where the model docs live

`docs/*.md` are not shipped inside the package. The model links on the PyPI
project page point back at this repo, and the interactive reference is at
[docs.movementinfrastructure.org/reference](https://docs.movementinfrastructure.org/reference/interactions).

---

## 7. Common failure modes

| Symptom | Likely cause |
|---|---|
| `401 Unauthorized`, empty body | Key missing the `<keyId>.` prefix; secret not valid base64; key issued for a different environment; key revoked or expired; workspace suppressed; or the key lacks the required role. |
| `ValidationError` before any request | A bad `method` or `outcome`. Validated client-side, so the batch never leaves your machine. |
| Rows rejected with a per-row error | Per-row validation. Read `rejected_interactions.data[].errors`. |
| Status query returns nothing | The Exchange is asynchronous. Retry after a few seconds. |

### On that 401

The 401 is deliberately generic and covers several distinct causes — including
a **valid key that simply lacks the required role**, which is an authorization
failure reported as an authentication one. If the key shape checks out in
step 1, ask the API team to check server-side logs rather than guessing. Quote
the `x-correlation-id` response header.

---

## 8. Sign-off checklist

- [ ] Installed from PyPI into a clean virtualenv
- [ ] `auth/me` returned the expected workspace
- [ ] Reviewed `destinations` / `van key` before submitting
- [ ] Submitted an interaction and received a `correlationId`
- [ ] Rejected rows, if any, reported a usable per-row reason
- [ ] Exchange status reached a terminal state for each accepted interaction
- [ ] Filed anything unexpected, with version and `correlationId`
