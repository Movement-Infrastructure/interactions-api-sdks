# Go SDK UAT guide

End-to-end validation of the published Go module: install from the Go module proxy, authenticate, submit an interaction, and confirm it reached the Exchange.

Each step says what "good" looks like, so you can tell a real failure from
expected output.

---

## 1. Prerequisites

- **Go 1.22 or later.**
- **An Interactions API key for production.** See
  [Authentication](https://docs.movementinfrastructure.org/docs/interactions-api-authentication).

Your key should look like `12345.<secret>`: a numeric key ID, a dot, then a base64
secret. **Both halves are required.**

Keys are environment-specific. A key issued for the public test server will not
work against production.

```bash
export DDX_API_KEY='12345.your-secret-here'
go version   # expect go1.22 or later
```

Check the shape before going further:

```bash
kid=${DDX_API_KEY%%.*}
secret=${DDX_API_KEY#*.}

if [ -n "$kid" ] && [ -z "$(printf '%s' "$kid" | tr -d '0-9')" ]; then
  echo "key id numeric: true"
else
  echo "key id numeric: false"
fi

if [ "$secret" = "$DDX_API_KEY" ] || [ -z "$secret" ]; then
  echo "secret is NOT valid base64: no dot separator in key"
elif ! printf '%s' "$secret" | base64 -d >/dev/null 2>&1; then
  echo "secret is NOT valid base64: contains non-base64 characters"
elif [ $(( ${#secret} % 4 )) -ne 0 ]; then
  echo "secret is NOT valid base64: truncated, length is not a multiple of 4"
else
  echo "secret is valid base64: true"
fi
```

Both must be true.

---

## 2. Install from the Go module proxy into a clean environment

```bash
mkdir -p /tmp/ddx-uat && cd /tmp/ddx-uat

go mod init ddx-uat
go get github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go@latest
```

### Expected result

```bash
go list -m github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go
#   github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go v0.1.0
```

The package is named `ddxinteractionsapi`. Each step below imports it under the
shorter name `ddx`.

---

## 3. Authenticate, and check what your key can reach

Each step writes one program into its own directory under the scratch project
and runs it with `go run`. The quoted `'GO'` matters. Unquoted, the shell would
expand `$` and backticks before Go ever saw them.

```bash
mkdir -p auth && cat > auth/main.go <<'GO'
package main

import (
	"context"
	"errors"
	"fmt"
	"net/http"
	"os"

	ddx "github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go"
)

func main() {
	// No server override, so the client defaults to production.
	cfg := ddx.NewConfiguration()
	target, _ := cfg.ServerURL(0, nil)
	fmt.Println("target:", target)

	ctx := context.WithValue(context.Background(), ddx.ContextBasicAuth, ddx.BasicAuth{
		UserName: "", // empty on purpose
		Password: os.Getenv("DDX_API_KEY"),
	})

	me, resp, err := ddx.NewAPIClient(cfg).AuthenticationDetailsAPI.VversionAuthMeGet(ctx, "1").Execute()
	if err != nil {
		report("auth/me", resp, err)
	}

	fmt.Printf("workspace:    %s (%d)\n", me.Workspace.DisplayName, me.Workspace.WorkspaceId)
	for _, d := range me.Destinations {
		fmt.Printf("destination:  %s  isVanDestination=%t\n", d.GetName(), d.GetIsVanDestination())
	}
	if len(me.Destinations) > 0 {
		fmt.Println("destinations: see above")
	} else {
		fmt.Println("destinations: none")
	}
	if me.VanApiKey != nil {
		fmt.Println("van key:      present")
	} else {
		fmt.Println("van key:      none")
	}
}

func report(call string, resp *http.Response, err error) {
	var apiErr *ddx.GenericOpenAPIError
	if resp == nil || !errors.As(err, &apiErr) {
		fmt.Fprintf(os.Stderr, "%s failed: %v\n", call, err)
		os.Exit(1)
	}
	if resp.StatusCode == http.StatusUnauthorized {
		fmt.Fprintln(os.Stderr, "  A 401 here has several causes. See Common failure modes.")
	}
	fmt.Fprintf(os.Stderr, "%s failed: HTTP %d\n", call, resp.StatusCode)
	fmt.Fprintf(os.Stderr, "  x-correlation-id: %s\n", orNone(resp.Header.Get("x-correlation-id")))
	fmt.Fprintf(os.Stderr, "  body: %s\n", orNone(string(apiErr.Body())))
	os.Exit(1)
}

func orNone(s string) string {
	if s == "" {
		return "(none)"
	}
	return s
}
GO
go run ./auth
```

### Expected Result

`target:` prints `https://api.movementinfrastructure.org`, and your workspace
name and ID print without an error.

**Read the `destinations` and `van key` lines before continuing.** They determine where data is actually sent:

- **A destination with `isVanDestination=true`** - what you submit is
  forwarded to VAN as a real canvass response.
- **Other destinations** - the Exchange is itself a destination, so a key that
  routes there lists it here like any other.
- **An empty list** - nothing routes what you submit.

Authentication is HTTP Basic with the **API key in the password field and an
empty username**.

The credentials travel on the `context.Context` passed to each call. The client
defaults to production (`https://api.movementinfrastructure.org`). To point it
elsewhere, replace `cfg.Servers` with a full URL including the scheme.

---

## 4. Submit an interaction

Replace `vendorSource`, `committee`, and `person` with identifiers your
workspace actually has. Left as placeholders they will be rejected.

| Placeholder | Comes from | Required |
| --- | --- | --- |
| `vendorSource` | You. The canonical name of the platform the outreach actually went through, which is not always the tool making this request. | Always |
| `committee[].type` / `.id` | You. Your own identifier for the entity that ran or logged the outreach: a campaign, a state party, and so on. Any `type`/`id` pair is accepted, and DDx checks only that both are non-empty. | Always, at least one |
| `person[].type` / `.id` | The system that issued the ID. `type` names that system (`VAN`, `DNC`, `SOS`, `phone`, your own CRM) and `id` is the ID it gave out. | Unless you send `contactInfo` instead |
| `vanFields.*` | VAN, scoped to the committee your VAN key is attached to. | Only for a key with a VAN destination |

### If Van is a Destination

Only relevant if step 3 showed a destination with `isVanDestination` set. Two
things change in the payload below:

- `person` must include an entry of type `VAN` carrying that person's VAN ID. It
  is required even when you also send `contactInfo`, and a given identifier type
  may appear only once in the array.
- `vanFields` is required, and both fields are validated:
  - `contactTypeId` must be a positive integer, matching a Contact Type the
    destination VAN committee can reach
    ([contact types](https://docs.ngpvan.com/reference/canvassresponsescontacttypes)).
  - `resultCodeId` must be a positive integer available to that contact type
    ([result codes](https://docs.ngpvan.com/reference/canvassresponsesresultcodes)).
    One exception: if `outcomesDetailed` carries an `activist_code` or
    `survey_response` entry, `resultCodeId` must instead be null or `14`
    (Canvassed).

```go
	interaction.SetPerson([]ddx.PersonIdentifier{*ddx.NewPersonIdentifier("<their VAN id>", "VAN")})

	vanFields := ddx.NewInteractionVanFieldsDto()
	vanFields.SetContactTypeId("<contact type id>")
	vanFields.SetResultCodeId("<result code id>")
	interaction.SetVanFields(*vanFields)
```

`vendorSource`, `committee`, `stateCode`, `method`, and `outcome` do not change
for a VAN key. The VAN committee that receives this is the one attached to your
VAN key, not anything you put in `committee`.

```bash
mkdir -p submit && cat > submit/main.go <<'GO'
package main

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"time"

	ddx "github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go"
)

func main() {
	ctx := context.WithValue(context.Background(), ddx.ContextBasicAuth, ddx.BasicAuth{
		UserName: "",
		Password: os.Getenv("DDX_API_KEY"),
	})
	stamp := time.Now().UTC()

	// The constructor takes the required fields in order: stateCode,
	// attemptDateTime, method, committee, vendorSource, outcome.
	interaction := ddx.NewInteractionDto(
		"CA",
		stamp,
		ddx.CONTACTMETHOD_PHONE_CALL,
		[]ddx.CommitteeDetails{*ddx.NewCommitteeDetails("<your type>", "<your committee id>")},
		"<your vendor name>",
		ddx.OUTCOME_SUCCESSFUL_CONTACT,
	)
	// NewPersonIdentifier takes the id first, then the type.
	interaction.SetPerson([]ddx.PersonIdentifier{*ddx.NewPersonIdentifier("<your person id>", "<your type>")})

	metadata, _ := json.Marshal(map[string]any{"uat": true, "posted_at": stamp.Format(time.RFC3339)})
	interaction.SetJsonMetadata(string(metadata))

	body := ddx.NewInteractionsDto()
	body.SetInteractions([]ddx.InteractionDto{*interaction})

	result, resp, err := ddx.NewAPIClient(ddx.NewConfiguration()).InteractionsAPI.
		VversionInteractionsPost(ctx, "1").
		InteractionsDto(*body).
		Execute()
	if err != nil {
		var apiErr *ddx.GenericOpenAPIError
		if resp == nil || !errors.As(err, &apiErr) {
			fmt.Fprintf(os.Stderr, "post failed: %v\n", err)
			os.Exit(1)
		}
		fmt.Fprintf(os.Stderr, "post failed: HTTP %d\n", resp.StatusCode)
		fmt.Fprintf(os.Stderr, "  x-correlation-id: %s\n", resp.Header.Get("x-correlation-id"))
		fmt.Fprintf(os.Stderr, "  body: %s\n", apiErr.Body())
		os.Exit(1)
	}

	accepted := result.GetAcceptedInteractions()
	rejected := result.GetRejectedInteractions()

	fmt.Println("correlationId:", result.GetCorrelationId())
	fmt.Printf("accepted: %d  rejected: %d\n", accepted.GetCount(), rejected.GetCount())

	for _, row := range accepted.GetData() {
		fmt.Printf("  accepted idx %d: interactionId %s\n", row.GetIndex(), row.GetInteractionId())
	}
	for _, row := range rejected.GetData() {
		for _, e := range row.GetErrors() {
			fmt.Printf("  rejected idx %d: %s: %s\n", row.GetIndex(), e.GetField(), e.GetErrorMessage())
		}
	}
}
GO
go run ./submit
```

### Expected Result

A `correlationId`, and `accepted` equal to the number of rows you sent.

**Keep an `interactionId`** from the accepted list. Step 5 exports it.

The cap is **100 interactions per request**.

`attemptDateTime` takes a `time.Time`. The client serializes it to RFC 3339, so
a hand-formatted string is unnecessary.

Set optional fields with the `Set*` methods. The model stores them as pointers
or nullable wrappers, and a field that is never set is left out of the request.

### Valid enum values

`ContactMethod` and `Outcome` are typed string constants, and a typo in one is a
compile error. Each name is the type name and the wire value, both upper-cased
and joined by an underscore:

- `ContactMethod`: `CONTACTMETHOD_UNKNOWN`, `CONTACTMETHOD_MAIL`,
  `CONTACTMETHOD_LETTER`, `CONTACTMETHOD_DIGITAL_AD`, `CONTACTMETHOD_EMAIL`,
  `CONTACTMETHOD_TEXT`, `CONTACTMETHOD_TEXT_BROADCAST`,
  `CONTACTMETHOD_ROBO_CALL`, `CONTACTMETHOD_DIALER_CALL`,
  `CONTACTMETHOD_PHONE_CALL`, `CONTACTMETHOD_DOOR_KNOCK`,
  `CONTACTMETHOD_EVENT`, `CONTACTMETHOD_HOT_SPOT`, `CONTACTMETHOD_ONE_ON_ONE`,
  `CONTACTMETHOD_WEB_INTERACTION`
- `Outcome`: `OUTCOME_UNKNOWN`, `OUTCOME_CLICKED_LINK`, `OUTCOME_EMAIL_OPENED`,
  `OUTCOME_SUBMITTED_FORM`, `OUTCOME_SUCCESSFUL_CONTACT`, `OUTCOME_DECEASED`,
  `OUTCOME_DELIVERABILITY_ERROR`, `OUTCOME_PERMANENTLY_UNDELIVERABLE`,
  `OUTCOME_INACCESSIBLE`, `OUTCOME_LANGUAGE_BARRIER`, `OUTCOME_MOVED`,
  `OUTCOME_NO_ANSWER`, `OUTCOME_WRONG_NUMBER`, `OUTCOME_HOSTILE`,
  `OUTCOME_MARKED_SPAM`, `OUTCOME_REFUSED`, `OUTCOME_DELIVERED`,
  `OUTCOME_LIT_DROP`, `OUTCOME_LEFT_MESSAGE`, `OUTCOME_OTHER`

---

## 5. Put the interaction ID in your environment

```bash
export INTERACTION_ID='<interactionId from step 4>'
```

---

## 6. Look up the interaction's transaction records

```bash
mkdir -p transactions && cat > transactions/main.go <<'GO'
package main

import (
	"context"
	"errors"
	"fmt"
	"os"
	"regexp"

	ddx "github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go"
)

var guid = regexp.MustCompile(`(?i)^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`)

func main() {
	interactionID := os.Getenv("INTERACTION_ID")

	// The route takes a GUID. A correlationId will not match, which is a
	// clearer failure here than the 404 the server would return for one.
	if !guid.MatchString(interactionID) {
		fmt.Fprintf(os.Stderr, "INTERACTION_ID is not a GUID: %q\n", interactionID)
		fmt.Fprintln(os.Stderr, "Use an interactionId from the accepted list in step 4, not a correlationId.")
		os.Exit(1)
	}

	ctx := context.WithValue(context.Background(), ddx.ContextBasicAuth, ddx.BasicAuth{
		UserName: "",
		Password: os.Getenv("DDX_API_KEY"),
	})

	txns, resp, err := ddx.NewAPIClient(ddx.NewConfiguration()).InteractionsAPI.
		VversionInteractionsInteractionIdTransactionsGet(ctx, interactionID, "1").
		ShowOnlyFailedTransactions(false).
		Execute()
	if err != nil {
		var apiErr *ddx.GenericOpenAPIError
		if resp == nil || !errors.As(err, &apiErr) {
			fmt.Fprintf(os.Stderr, "transactions lookup failed: %v\n", err)
			os.Exit(1)
		}
		fmt.Fprintf(os.Stderr, "transactions lookup failed: HTTP %d\n", resp.StatusCode)
		fmt.Fprintf(os.Stderr, "  x-correlation-id: %s\n", resp.Header.Get("x-correlation-id"))
		fmt.Fprintf(os.Stderr, "  body: %s\n", apiErr.Body())
		os.Exit(1)
	}

	metadata := txns.GetMetadata()
	fmt.Println("count:", metadata.GetCount())
	for _, row := range txns.GetData() {
		fmt.Printf("  %s  %s\n", row.GetDateCreatedUtc().Format("2006-01-02T15:04:05Z07:00"), row.GetStatus())
		for _, log := range row.GetLogs() {
			fmt.Printf("      HTTP %d  %s\n", log.GetResponseStatusCode(), log.GetResponse())
		}
	}
}
GO
go run ./transactions
```

### Expected Result

The call returns immediately. What it contains depends on where your workspace
routes interactions, which step 3 told you:

- **A destination with `isVanDestination` set**: a row per delivery attempt,
  each with a status of `Received`, `Processing`, `Success`, `Failed`,
  `Invalid`, `Duplicate`, or `InternalError`, plus any response logs recorded
  for it.
- **No VAN destination**: `count: 0` and no rows. Only the VAN send path writes
  these records. A key that routes to the Exchange has a destination and still
  returns `count: 0` here, because the Exchange is reported by exchange status
  instead.

`count: 0` is a valid result, not a failure. What this step verifies is that the
call authenticates, returns a parsed response, and reports whatever records
exist for the interaction you submitted.

`ShowOnlyFailedTransactions` is set to false on purpose. It defaults to true,
which returns only `Failed`, `Invalid`, and `Duplicate` rows and would hide a
successful delivery.

Exchange delivery is reported by a different endpoint,
`interactions/exchange-status`. It advances on a scheduled transformation rather
than on your request and can lag by up to an hour, so it is outside this UAT.

The interactive reference is at
[docs.movementinfrastructure.org/reference](https://docs.movementinfrastructure.org/reference/interactions).

---

## 7. Common failure modes

| Symptom | Likely cause |
|---|---|
| `module ... requires go >= 1.22` | Go older than 1.22, with automatic toolchain downloads turned off (`GOTOOLCHAIN=local`). |
| `no required module provides package` | Running `go run` outside `/tmp/ddx-uat`, or `go get` skipped, so the import does not resolve. |
| `401 Unauthorized`, empty body | Key missing the `<keyId>.` prefix; secret not valid base64; key issued for a different environment; key revoked or expired; workspace suppressed; or the key lacks the required role. |
| Rows rejected with a per-row error | Per-row validation. Read `rejectedInteractions.data[].errors`. |
| `INTERACTION_ID is not a GUID` | You passed the `correlationId`. That route takes a GUID `interactionId` only, and correlation IDs are either a numeric trace ID or `mig-` prefixed. Use an ID from the accepted list in step 4. |
| Step 6 returns `count: 0` | The key has no destination with `isVanDestination` set, so no transaction record exists; or `ShowOnlyFailedTransactions` was left at its default of true. |

### Causes of 401 Errors

The 401 is deliberately generic and covers several distinct causes, including
a **valid key that simply lacks the required role**, which is an authorization
failure reported as an authentication one. If the key shape checks out in
step 1, ask the API team to check server-side logs rather than guessing.

`Body()` on the returned `*ddx.GenericOpenAPIError` carries the API's
explanation; the error message alone is only the status line.

---

## 8. Sign-off checklist

- [ ] Installed from the Go module proxy into a clean scratch project
- [ ] `auth/me` returned the expected workspace
- [ ] Reviewed `destinations` / `van key` before submitting
- [ ] Submitted an interaction and received a `correlationId`
- [ ] Rejected rows, if any, reported a usable per-row reason
- [ ] Retrieved transaction records for an accepted `interactionId`,
      with `ShowOnlyFailedTransactions` set to false
- [ ] Filed anything unexpected, with version and `correlationId`
