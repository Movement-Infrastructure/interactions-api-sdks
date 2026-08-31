# Node v1 SDK smoke tests

A minimal suite that runs against the **generated** `ddx-interactions-api`
client to catch a broken SDK before a PR merges.

- `import-smoke.test.ts` — the client loads and exposes its public surface
  (runtime classes, the two API classes, key model converters).
- `publish-interactions.test.ts` — one happy-path `POST /v1/interactions` call
  against a mocked server (`msw`), asserting the response deserializes into
  `InteractionsBatchResultDto`, the templated path resolves, basic auth is sent,
  and the request body serializes as the API expects.

## Running locally

The tests import the generated client, so generate and patch it first:

```bash
# from the repo root — requires Java 17 for openapi-generator 7.10.0
java -jar .cache/openapi-generator-cli.jar generate \
  -i openapi/v1/swagger.json -g typescript-fetch \
  -o sdks/node/v1 -c sdks/node/v1/openapi-generator-config.yaml

python scripts/patch_node_sdk.py sdks/node/v1 --expect-name ddx-interactions-api

cd sdks/node/v1
npm install
npm test
```

The patch step is not optional. Without it `tsconfig.json` has no `include`, so
`tsc` type-checks the test dependencies and the build fails before the tests run.

In CI this is done for you by `.github/workflows/node-sdk-tests.yml`, which
regenerates the SDK from the spec on every PR and runs this suite as a required
check.

## Notes

- These files are protected from regeneration by `../.openapi-generator-ignore`.
- Tests import from `../src`, not `../dist`. `npm run build` is a separate CI
  step, so a compile failure is reported on its own rather than as a test error.
- The happy-path test calls `vversionInteractionsPost`, an auto-derived slug —
  the spec defines no `operationId` for the interactions endpoints, so the
  generator names methods from the path and verb.
