# Python v1 SDK smoke tests (MIG-1918)

A minimal suite that runs against the **generated** `mi_interactions_api`
package to catch a broken SDK before a PR merges.

- `test_import_smoke.py` — the package imports and exposes its public surface
  (client classes, the two API classes, key models).
- `test_publish_interactions.py` — one happy-path `POST /v1/interactions` call
  against a mocked HTTP server (`pytest-httpserver`), asserting the response
  deserializes into `InteractionsBatchResultDto`.

## Running locally

The tests import the generated package, so generate and install it first:

```bash
# from the repo root — requires Java 17 for openapi-generator 7.10.0
java -jar .cache/openapi-generator-cli.jar generate \
  -i openapi/v1/swagger.json -g python \
  -o sdks/python/v1 -c sdks/python/v1/openapi-generator-config.yaml

pip install ./sdks/python/v1
pip install -r sdks/python/v1/requirements-test.txt
pytest sdks/python/v1/tests -q
```

In CI this is done for you by `.github/workflows/python-sdk-tests.yml`, which
regenerates the SDK from the spec on every PR and runs this suite as a required
check.

## Notes

- These files are protected from regeneration by `../.openapi-generator-ignore`.
- The happy-path test discovers the POST operation at runtime because the spec
  defines no `operationId` (the generated method name is an auto-derived slug).
