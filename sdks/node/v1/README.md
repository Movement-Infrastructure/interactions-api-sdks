# ddx-interactions-api

Node client for the DDx Interactions API, generated from its OpenAPI
specification.

- API version: v1
- Package version: 0.1.0
- Generator version: 7.10.0

## Requirements

Node 18 or later. The client calls the platform's `fetch`, so the package has
no runtime dependencies.

## Installation

```shell
npm install ddx-interactions-api
```

## Changelog

API changes are recorded in the
[changelog](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/node/v1/CHANGELOG.md),
regenerated from a diff of the OpenAPI specification on each sync. Entries
marked **breaking** require a change on the consumer side.

## Reporting issues

This package is generated. Edits to it are overwritten on the next spec sync.
Report problems against the API specification rather than the generated code.

## Getting Started

```typescript
import { AuthenticationDetailsApi, Configuration, ResponseError } from 'ddx-interactions-api';

// HTTP basic auth, API key in the password field, empty username.
// basePath already defaults to the production API.
const api = new AuthenticationDetailsApi(
  new Configuration({
    username: '',
    password: process.env.DDX_API_KEY,
  }),
);

try {
  const me = await api.vversionAuthMeGet({ version: '1' });
  console.log(me);
} catch (e) {
  if (e instanceof ResponseError) {
    // The thrown error carries only the status line. The body says why.
    console.error(`Interactions API returned ${e.response.status}: ${await e.response.text()}`);
  } else {
    throw e;
  }
}
```

## Documentation

Per-endpoint and per-model pages are generated alongside the client:
[Apis](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/node/v1/docs/Apis) and [Models](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/node/v1/docs/Models). They are linked absolutely
because the npm package ships only `dist/`.

The same field documentation travels with the exported types, so editor
autocomplete on an imported type reads the shape without leaving the file.
