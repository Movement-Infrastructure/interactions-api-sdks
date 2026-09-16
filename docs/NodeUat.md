# Node SDK UAT guide

End-to-end validation of the published npm package: install from npm, authenticate, submit an interaction, and confirm it reached the Exchange.

Each step says what "good" looks like, so you can tell a real failure from
expected output.

---

## 1. Prerequisites

- **Node 18 or later.** The client calls the platform's global `fetch`.
- **An Interactions API key for production.** See
  [Authentication](https://docs.movementinfrastructure.org/docs/interactions-api-authentication).

Your key should look like `12345.<secret>`: a numeric key ID, a dot, then a base64
secret. **Both halves are required.**

Keys are environment-specific. A key issued for the public test server will not
work against production.

```bash
export DDX_API_KEY='12345.your-secret-here'
node --version   # expect v18 or later
```

Check the shape before going further:

```bash
node --input-type=module <<'JS'
const [kid, secret] = (process.env.DDX_API_KEY ?? '').split(/\.(.*)/s);

console.log('key id numeric:', /^\d+$/.test(kid ?? ''));

if (!secret) {
  console.log('secret is NOT valid base64: no dot separator in key');
} else {
  const decoded = Buffer.from(secret, 'base64');
  console.log('secret is valid base64:', decoded.toString('base64') === secret);
}
JS
```

Both must be true.

---

## 2. Install from npm into a clean environment

```bash
mkdir -p /tmp/ddx-uat && cd /tmp/ddx-uat

npm init -y
npm install ddx-interactions-api
```

A scratch project outside the repo resolves the package from npm instead of
from the source tree. A file missing from the published tarball fails here
rather than after release.

### Expected result

```bash
npm ls ddx-interactions-api
#   └── ddx-interactions-api@0.1.0
```

**Before the first release**, the package is not on npm yet and `npm install`
will fail. To rehearse against the artifact about to be published, pack it and
install the tarball:

```bash
npm pack --pack-destination /tmp <repo>/sdks/node/v1
npm install /tmp/ddx-interactions-api-0.1.0.tgz
```

Everything from step 3 on is identical either way.

---

## 3. Authenticate, and check what your key can reach

Each step pipes a module to `node` from the scratch directory, so the bare
import resolves against the `node_modules` you just created. The quoted `'JS'`
matters. Unquoted, the shell would expand `$` and backticks before Node ever
saw them.

```bash
node --input-type=module <<'JS'
import { AuthenticationDetailsApi, Configuration, ResponseError } from 'ddx-interactions-api';

// basePath is a full URL, scheme included.
const config = new Configuration({
  basePath: process.env.DDX_API_BASE_PATH ?? 'https://api.movementinfrastructure.org',
  username: '',                                  // empty on purpose
  password: process.env.DDX_API_KEY,
});

console.log('target:', config.basePath);

const api = new AuthenticationDetailsApi(config);

try {
  const me = await api.vversionAuthMeGet({ version: '1' });

  console.log(`workspace:    ${me.workspace?.displayName} (${me.workspace?.workspaceId})`);
  for (const d of me.destinations ?? []) {
    console.log(`destination:  ${d.name}  isVanDestination=${d.isVanDestination}`);
  }
  console.log('destinations:', me.destinations?.length ? 'see above' : 'none');
  console.log('van key:     ', me.vanApiKey ? 'present' : 'none');
} catch (e) {
  if (!(e instanceof ResponseError)) throw e;

  const cid = e.response.headers.get('x-correlation-id') ?? 'none';
  const body = await e.response.text();

  if (e.response.status === 401) {
    console.error('  A 401 here has several causes. See Common failure modes.');
  }

  console.error(`auth/me failed: HTTP ${e.response.status}`);
  console.error(`  x-correlation-id: ${cid}`);
  console.error(`  body: ${body || '(empty)'}`);
  process.exit(1);
}
JS
```

### Expected Result

`target:` prints `https://api.movementinfrastructure.org`, and your workspace
name and ID print without an exception.

**Read the `destinations` and `van key` lines before continuing.** They decide
what step 4 actually does:

- **A destination with `isVanDestination=true`** - what you submit is
  forwarded to VAN as a real canvass response. Coordinate before submitting.
- **Other destinations** - the Exchange is itself a destination, so a key that
  routes there lists it here like any other.
- **An empty list** - nothing routes what you submit, the Exchange included.

Authentication is HTTP Basic with the **API key in the password field and an
empty username**. That surprises people; it is correct.

`basePath` is a full URL including the scheme. The Ruby client splits host and
scheme into separate fields. The Node one does not.

---

## 4. Submit an interaction

Replace `vendorSource`, `committee`, and `person` with identifiers your
workspace actually has. Left as placeholders they will be rejected.

```bash
node --input-type=module <<'JS'
import {
  ContactMethod,
  Configuration,
  InteractionsApi,
  Outcome,
  ResponseError,
} from 'ddx-interactions-api';

const config = new Configuration({
  basePath: process.env.DDX_API_BASE_PATH ?? 'https://api.movementinfrastructure.org',
  username: '',
  password: process.env.DDX_API_KEY,
});

const api = new InteractionsApi(config);
const stamp = new Date();

const interactionsDto = {
  interactions: [
    {
      stateCode: 'CA',
      attemptDateTime: stamp,
      method: ContactMethod.PhoneCall,
      outcome: Outcome.SuccessfulContact,
      vendorSource: '<your vendor name>',
      committee: [{ type: '<your type>', id: '<your committee id>' }],
      person: [{ type: '<your type>', id: '<your person id>' }],
      jsonMetadata: JSON.stringify({ uat: true, posted_at: stamp.toISOString() }),
    },
  ],
};

try {
  const result = await api.vversionInteractionsPost({ version: '1', interactionsDto });

  console.log('correlationId:', result?.correlationId);
  console.log(
    `accepted: ${result?.acceptedInteractions?.count}  rejected: ${result?.rejectedInteractions?.count}`,
  );

  for (const row of result?.acceptedInteractions?.data ?? []) {
    console.log(`  accepted idx ${row.index}: interactionId ${row.interactionId}`);
  }
  for (const row of result?.rejectedInteractions?.data ?? []) {
    for (const err of row.errors ?? []) {
      console.log(`  rejected idx ${row.index}: ${err.field}: ${err.errorMessage}`);
    }
  }
} catch (e) {
  if (!(e instanceof ResponseError)) throw e;

  const cid = e.response.headers.get('x-correlation-id') ?? 'none';
  const body = await e.response.text();

  console.error(`post failed: HTTP ${e.response.status}`);
  console.error(`  x-correlation-id: ${cid}`);
  console.error(`  body: ${body || '(empty)'}`);
  process.exit(1);
}
JS
```

### Expected Result

A `correlationId`, and `accepted` equal to the number of rows you sent.

**Keep an `interactionId`** from the accepted list. Step 5 exports it.

The cap is **100 interactions per request**.

`attemptDateTime` takes a `Date`. The client serializes it to ISO 8601, so a
hand-formatted string is unnecessary.

### Valid enum values

`ContactMethod` and `Outcome` are exported as const objects, so a typo is a
type error under TypeScript. Member names are the PascalCase form of the wire
value:

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
node --input-type=module <<'JS'
import { Configuration, InteractionsApi, ResponseError } from 'ddx-interactions-api';

const interactionId = process.env.INTERACTION_ID ?? '';

// The route takes a GUID. A correlationId will not match, which is a clearer
// failure here than the 404 the server would return for one.
if (!/^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(interactionId)) {
  console.error(`INTERACTION_ID is not a GUID: ${interactionId || '(unset)'}`);
  console.error('Use an interactionId from the accepted list in step 4, not a correlationId.');
  process.exit(1);
}

const api = new InteractionsApi(
  new Configuration({
    basePath: process.env.DDX_API_BASE_PATH ?? 'https://api.movementinfrastructure.org',
    username: '',
    password: process.env.DDX_API_KEY,
  }),
);

try {
  const txns = await api.vversionInteractionsInteractionIdTransactionsGet({
    interactionId,
    version: '1',
    showOnlyFailedTransactions: false,
  });

  console.log('count:', txns.metadata?.count ?? 0);
  for (const row of txns.data ?? []) {
    console.log(`  ${row.dateCreatedUtc?.toISOString()}  ${row.status}`);
    for (const log of row.logs ?? []) {
      console.log(`      HTTP ${log.responseStatusCode}  ${log.response}`);
    }
  }
} catch (e) {
  if (!(e instanceof ResponseError)) throw e;

  const cid = e.response.headers.get('x-correlation-id') ?? 'none';
  const body = await e.response.text();

  console.error(`transactions lookup failed: HTTP ${e.response.status}`);
  console.error(`  x-correlation-id: ${cid}`);
  console.error(`  body: ${body || '(empty)'}`);
  process.exit(1);
}
JS
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

---

## 7. Common failure modes

| Symptom | Likely cause |
|---|---|
| `SyntaxError: Unexpected token` on import | Node older than 18, or the script run without `--input-type=module`. |
| `Cannot find package 'ddx-interactions-api'` | Running from a directory other than the scratch project, so the bare import does not resolve. |
| `401 Unauthorized`, empty body | Key missing the `<keyId>.` prefix; secret not valid base64; key issued for a different environment; key revoked or expired; workspace suppressed; or the key lacks the required role. |
| Rows rejected with a per-row error | Per-row validation. Read `rejectedInteractions.data[].errors`. |
| `INTERACTION_ID is not a GUID` | You passed the `correlationId`. That route takes a GUID `interactionId` only, and correlation IDs are either a numeric trace ID or `mig-` prefixed. Use an ID from the accepted list in step 4. |
| Step 6 returns `count: 0` | The key has no destination with `isVanDestination` set, so no transaction record exists; or `showOnlyFailedTransactions` was left at its default of true. |

### On that 401

The 401 is deliberately generic and covers several distinct causes, including
a **valid key that simply lacks the required role**, which is an authorization
failure reported as an authentication one. If the key shape checks out in
step 1, ask the API team to check server-side logs rather than guessing.

`ResponseError` carries the raw `Response`. The message alone is only the status
line, so read `await e.response.text()` for the API's explanation.

---

## 8. Where the model docs live

The typescript-fetch generator emits no separate docs directory. Request and
response types are exported from the package root, and the field documentation
from the specification travels with them, so editor autocomplete on
`InteractionsDto` is the fastest way to read the shape.

---

## 9. Sign-off checklist

- [ ] Installed from npm into a clean scratch project
- [ ] `auth/me` returned the expected workspace
- [ ] Reviewed `destinations` / `van key` before submitting
- [ ] Submitted an interaction and recorded the `correlationId`
- [ ] Looked up the interaction's transaction records
