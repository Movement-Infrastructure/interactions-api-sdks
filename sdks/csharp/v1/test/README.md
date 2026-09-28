# C# v1 SDK smoke tests

A minimal suite that runs against the **generated** `Ddx.InteractionsApi`
assembly to catch a broken SDK before a PR merges.

- `ImportSmokeTest.cs` — the assembly builds and exposes its public surface
  (client types, the two API classes, key models).
- `PublishInteractionsTest.cs` — one happy-path `POST /v1/interactions` call
  against a stubbed transport, asserting the response deserializes into
  `InteractionsBatchResultDto`, the templated path resolves, basic auth is sent,
  and the request body serializes as the API expects.
- `StubHttpMessageHandler.cs` — captures the outgoing request and returns a
  canned response. Hand-rolled because the generated client accepts an
  `HttpClient`, so a short handler keeps the dependencies to xUnit alone.

## Running locally

The tests reference the generated client, so generate and patch it first:

```bash
# from the repo root — requires Java 17 for openapi-generator 7.10.0
java -jar .cache/openapi-generator-cli.jar generate \
  -i openapi/v1/swagger.json -g csharp \
  -o sdks/csharp/v1 -c sdks/csharp/v1/openapi-generator-config.yaml \
  -t templates/csharp

python scripts/patch_dotnet_sdk.py \
  sdks/csharp/v1/src/Ddx.InteractionsApi/Ddx.InteractionsApi.csproj

cd sdks/csharp/v1
dotnet test test/Ddx.InteractionsApi.Test/Ddx.InteractionsApi.Test.csproj
```

`.github/workflows/csharp-sdk-tests.yml` does the same on every PR.

## Notes

- These files are protected from regeneration by `../.openapi-generator-ignore`.
- The test project is deliberately **not** in `Ddx.InteractionsApi.sln`. The
  generator rewrites the solution on every sync, so an entry added there would
  be clobbered. CI runs the project by path instead.
- The tests live in namespace `InteractionsApiSdkTests`, outside the `Ddx.*`
  tree. Inside it, the namespace `Ddx.InteractionsApi` shadows the class
  `Ddx.InteractionsApi.Api.InteractionsApi` and the type can't be named without
  full qualification. Consumers outside `Ddx.*` are unaffected.
- The happy-path test calls `VversionInteractionsPost`. The spec sets no
  `operationId` for the interactions endpoints, so the generator derives method
  names from the path and verb.
