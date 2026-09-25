# C# SDK UAT guide

End-to-end validation of the published NuGet package: install from NuGet, authenticate, submit an interaction, and confirm it reached the Exchange.

Each step says what "good" looks like, so you can tell a real failure from
expected output.

---

## 1. Prerequisites

- **.NET 8.0 SDK or later.** The package targets `net8.0`.
- **An Interactions API key for production.** See
  [Authentication](https://docs.movementinfrastructure.org/docs/interactions-api-authentication).

Your key should look like `12345.<secret>`: a numeric key ID, a dot, then a base64
secret. **Both halves are required.**

Keys are environment-specific. A key issued for the public test server will not
work against production.

```bash
export DDX_API_KEY='12345.your-secret-here'
dotnet --version   # expect 8.0 or later
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

## 2. Install from NuGet into a clean environment

```bash
mkdir -p /tmp/ddx-uat && cd /tmp/ddx-uat

dotnet new console --force
dotnet add package Ddx.InteractionsApi
```


### Expected result

```bash
dotnet list package
#   > Ddx.InteractionsApi      0.1.0      0.1.0
```

The package ID is dotted, and so are the namespaces you import
(`using Ddx.InteractionsApi.Api;`, `.Client`, `.Model`).

---

## 3. Authenticate, and check what your key can reach

Each step replaces `Program.cs` and re-runs. The quoting around `'CS'` matters.
Each step replaces `Program.cs` and re-runs.

```bash
cat > Program.cs <<'CS'
using Ddx.InteractionsApi.Api;
using Ddx.InteractionsApi.Client;

// Configuration takes no BasePath, so it defaults to production.
var config = new Configuration
{
    Username = "",                       // empty on purpose
    Password = Environment.GetEnvironmentVariable("DDX_API_KEY")
               ?? throw new InvalidOperationException("DDX_API_KEY is not set"),
};

Console.WriteLine($"target: {config.BasePath}");

var auth = new AuthenticationDetailsApi(config);

try
{
    var me = auth.VversionAuthMeGet("1");

    Console.WriteLine($"workspace:    {me.Workspace.DisplayName} ({me.Workspace.WorkspaceId})");
    foreach (var d in me.Destinations ?? [])
    {
        Console.WriteLine($"destination:  {d.Name}  isVanDestination={d.IsVanDestination}");
    }
    Console.WriteLine($"destinations: {(me.Destinations?.Count > 0 ? "see above" : "none")}");
    Console.WriteLine($"van key:      {(me.VanApiKey is not null ? "present" : "none")}");
}
catch (ApiException e)
{
    var cid = e.Headers?.TryGetValue("x-correlation-id", out var v) == true
        ? string.Join(",", v)
        : "none";

    if (e.ErrorCode == 401)
    {
        Console.Error.WriteLine("  A 401 here has several causes. See Common failure modes.");
    }

    Console.Error.WriteLine($"auth/me failed: HTTP {e.ErrorCode}");
    Console.Error.WriteLine($"  x-correlation-id: {cid}");
    Console.Error.WriteLine($"  body: {(string.IsNullOrEmpty(e.ErrorContent?.ToString()) ? "(empty)" : e.ErrorContent)}");
    Environment.Exit(1);
}
CS

dotnet run
```

### Expected Result

`target:` prints `https://api.movementinfrastructure.org`, and your workspace
name and ID print without an exception.

**Read the `destinations` and `van key` lines before continuing.** They decide
what step 4 actually does:

- **A destination with `isVanDestination=True`** - what you submit is
  forwarded to VAN as a real canvass response. Coordinate before submitting.
- **Other destinations** - the Exchange is itself a destination, so a key that
  routes there lists it here like any other.
- **An empty list** - nothing routes what you submit.

Authentication is HTTP Basic with the **API key in the password field and an
empty username**.

`Configuration` takes no `BasePath`, so it defaults to production
(`https://api.movementinfrastructure.org`). When set, it is a full URL
including the scheme.

---

## 4. Submit an interaction

Replace `vendorSource`, `committee`, and `person` with identifiers your
workspace actually has. Left as placeholders they will be rejected.

```bash
cat > Program.cs <<'CS'
using System.Text.Json;
using Ddx.InteractionsApi.Api;
using Ddx.InteractionsApi.Client;
using Ddx.InteractionsApi.Model;

var config = new Configuration
{
    Username = "",
    Password = Environment.GetEnvironmentVariable("DDX_API_KEY")
               ?? throw new InvalidOperationException("DDX_API_KEY is not set"),
};

var interactions = new InteractionsApi(config);
var stamp = DateTime.UtcNow;

var payload = new InteractionsDto(
    interactions: new List<InteractionDto>
    {
        new(
            stateCode: "CA",
            attemptDateTime: stamp,
            method: ContactMethod.PhoneCall,
            outcome: Outcome.SuccessfulContact,
            vendorSource: "<your vendor name>",
            committee: new List<CommitteeDetails> { new(type: "<your type>", id: "<your committee id>") },
            person: new List<PersonIdentifier> { new(type: "<your type>", id: "<your person id>") },
            jsonMetadata: JsonSerializer.Serialize(new { uat = true, posted_at = stamp })),
    });

try
{
    var result = interactions.VversionInteractionsPost("1", payload);

    Console.WriteLine($"correlationId: {result.CorrelationId}");
    Console.WriteLine($"accepted: {result.AcceptedInteractions.Count}  rejected: {result.RejectedInteractions.Count}");

    foreach (var row in result.AcceptedInteractions.Data ?? [])
    {
        Console.WriteLine($"  accepted idx {row.Index}: interactionId {row.InteractionId}");
    }
    foreach (var row in result.RejectedInteractions.Data ?? [])
    {
        foreach (var err in row.Errors ?? [])
        {
            Console.WriteLine($"  rejected idx {row.Index}: {err.Field}: {err.ErrorMessage}");
        }
    }
}
catch (ApiException e)
{
    var cid = e.Headers?.TryGetValue("x-correlation-id", out var v) == true
        ? string.Join(",", v)
        : "none";

    Console.Error.WriteLine($"post failed: HTTP {e.ErrorCode}");
    Console.Error.WriteLine($"  x-correlation-id: {cid}");
    Console.Error.WriteLine($"  body: {(string.IsNullOrEmpty(e.ErrorContent?.ToString()) ? "(empty)" : e.ErrorContent)}");
    Environment.Exit(1);
}
CS

dotnet run
```

### Expected Result

A `correlationId`, and `accepted` equal to the number of rows you sent.

**Keep an `interactionId`** from the accepted list. Step 5 exports it.

The cap is **100 interactions per request**.

`attemptDateTime` is a `DateTime`, not a string. Use `DateTime.UtcNow` or a
`DateTimeKind.Utc` value. The serializer writes ISO 8601 from it.

### Valid enum values

These are typed enums in the C# client, so a bad value is a compile error rather
than a 400. Member names are the PascalCase form of the wire value:

- `ContactMethod`: `Unknown`, `Mail`, `Letter`, `DigitalAd`, `Email`, `Text`,
  `TextBroadcast`, `RoboCall`, `DialerCall`, `PhoneCall`, `DoorKnock`, `Event`,
  `HotSpot`, `OneOnOne`, `WebInteraction`
- `Outcome`: `Unknown`, `ClickedLink`, `EmailOpened`, `SubmittedForm`,
  `SuccessfulContact`, `Deceased`, `DeliverabilityError`,
  `PermanentlyUndeliverable`, `Inaccessible`, `LanguageBarrier`, `Moved`,
  `NoAnswer`, `WrongNumber`, `Hostile`, `MarkedSpam`, `Refused`, `Delivered`,
  `LitDrop`, `LeftMessage`, `Other`

`Event` is the one value whose wire form is already capitalised.

---

## 5. Put the interaction ID in your environment

```bash
export INTERACTION_ID='<interactionId from step 4>'
```

---

## 6. Look up the interaction's transaction records

```bash
cat > Program.cs <<'CS'
using Ddx.InteractionsApi.Api;
using Ddx.InteractionsApi.Client;

var config = new Configuration
{
    Username = "",
    Password = Environment.GetEnvironmentVariable("DDX_API_KEY")
               ?? throw new InvalidOperationException("DDX_API_KEY is not set"),
};

var raw = Environment.GetEnvironmentVariable("INTERACTION_ID") ?? "";

// Interaction ID should be a GUID. Accidentally pasting in a Correlation ID instead will give you a parse error here
if (!Guid.TryParse(raw, out var interactionId))
{
    Console.Error.WriteLine($"INTERACTION_ID is not a GUID: {(raw.Length == 0 ? "(unset)" : raw)}");
    Console.Error.WriteLine("Use an interactionId from the accepted list in step 4, not a correlationId.");
    Environment.Exit(1);
}

var interactions = new InteractionsApi(config);

try
{
    var txns = interactions.VversionInteractionsInteractionIdTransactionsGet(
        interactionId, "1", showOnlyFailedTransactions: false);

    Console.WriteLine($"count: {txns.Metadata?.Count ?? 0}");
    foreach (var row in txns.Data ?? [])
    {
        Console.WriteLine($"  {row.DateCreatedUtc}  {row.Status}");
        foreach (var log in row.Logs ?? [])
        {
            Console.WriteLine($"      HTTP {log.ResponseStatusCode}  {log.Response}");
        }
    }
}
catch (ApiException e)
{
    var cid = e.Headers?.TryGetValue("x-correlation-id", out var v) == true
        ? string.Join(",", v)
        : "none";

    Console.Error.WriteLine($"transactions lookup failed: HTTP {e.ErrorCode}");
    Console.Error.WriteLine($"  x-correlation-id: {cid}");
    Console.Error.WriteLine($"  body: {(string.IsNullOrEmpty(e.ErrorContent?.ToString()) ? "(empty)" : e.ErrorContent)}");
    Environment.Exit(1);
}
CS

dotnet run
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

`showOnlyFailedTransactions` is set to false on purpose. It defaults to true,
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
| `error NETSDK1045: The current .NET SDK does not support targeting .NET 8.0` | SDK older than 8.0. |
| `401 Unauthorized`, empty body | Key missing the `<keyId>.` prefix; secret not valid base64; key issued for a different environment; key revoked or expired; workspace suppressed; or the key lacks the required role. |
| Rows rejected with a per-row error | Per-row validation. Read `RejectedInteractions.Data[].Errors`. |
| `INTERACTION_ID is not a GUID` | You passed the `correlationId`. That route takes a GUID `interactionId` only, and correlation IDs are either a numeric trace ID or `mig-` prefixed. Use an ID from the accepted list in step 4. |
| Step 6 returns `count: 0` | The key has no destination with `isVanDestination` set, so no transaction record exists; or `showOnlyFailedTransactions` was left at its default of true. |

### On that 401

The 401 is deliberately generic and covers several distinct causes, including
a **valid key that simply lacks the required role**, which is an authorization
failure reported as an authentication one. If the key shape checks out in
step 1, ask the API team to check server-side logs rather than guessing.

`ApiException.ErrorContent` carries the API's explanation; the exception message
alone is only the status line.

---

## 8. Where the model docs live

The package ships the compiled library and `README.md` only, so `docs/*.md`
are not inside the installed package. The model links in the README point back
at [this repo](https://github.com/Movement-Infrastructure/interactions-api-sdks/tree/main/sdks/csharp/v1/docs),
and the interactive reference is at
[docs.movementinfrastructure.org/reference](https://docs.movementinfrastructure.org/reference/interactions).

`InteractionsDto.md` and `InteractionDto.md` are the two this guide sends.

---

## 9. Sign-off checklist

- [ ] Installed from NuGet into a clean scratch project
- [ ] `auth/me` returned the expected workspace
- [ ] Reviewed `destinations` / `van key` before submitting
- [ ] Submitted an interaction and received a `correlationId`
- [ ] Rejected rows, if any, reported a usable per-row reason
- [ ] Retrieved transaction records for an accepted `interactionId`,
      with `showOnlyFailedTransactions` set to false
- [ ] Filed anything unexpected, with version and `correlationId`
