# MIG-1918 — Add Python SDK smoke-test suite (blocking merge)

[Linear ticket](https://linear.app/movementinfrastructure/issue/MIG-1918/add-python-sdk-smoke-test-suite-blocking-merge)

## Background

Milestone follow-on to [MIG-1917](./MIG-1917-generate-python-sdk.md) (generate
the Python SDK on every sync PR). We now need a minimal test suite that runs
against the **generated** `sdks/python/v1/` package and blocks PR merge if the
generated SDK is broken.

Scope, as agreed:
- An **import smoke test**.
- **One happy-path call** (`POST /v1/interactions`) against a **mocked server**.
- Wired into CI as a **required check** that blocks merge.

## Key facts that shaped the design

- The SDK is **generated, not committed** to `develop` — `sdks/python/v1/` and
  `openapi/v1/swagger.json` hold only `.gitkeep`s until a sync PR lands. The SDK
  exists on a branch only after `openapi/v1/swagger.json` is present and
  openapi-generator has run. So tests must run against a freshly generated SDK.
- The spec has **no `operationId`s**, so openapi-generator derives operation
  method names from verb+path (e.g. `post_v_version_interactions`). That slug is
  brittle, so the happy-path test discovers the POST op at runtime rather than
  hard-coding it. Class/model names (from tags and schema names) are stable.
- The generator uses `library: urllib3` (a real HTTP client), so the mock is a
  live localhost server (`pytest-httpserver`), not a transport monkeypatch.

## Decision: standalone, all-PRs workflow (not inline in the generate workflow)

A required status check that is path-filtered shows as perpetually "pending" on
PRs that don't match the filter, which blocks merge forever. So the check runs
on **all** PRs to `develop` and regenerates the SDK from the spec itself. On a
branch with no committed spec (bootstrap window), the SDK cannot change, so the
heavy steps are skipped and the job passes.

## Deliverables

- [x] `sdks/python/v1/tests/test_import_smoke.py` — package + public-surface imports.
- [x] `sdks/python/v1/tests/test_publish_interactions.py` — happy-path `POST /v1/interactions`
      against `pytest-httpserver`, asserting the response deserializes to
      `InteractionsBatchResultDto`.
- [x] `sdks/python/v1/tests/conftest.py` — `api_client` fixture pointing at the mock server.
- [x] `sdks/python/v1/tests/README.md` — how to run locally.
- [x] `sdks/python/v1/requirements-test.txt` — `pytest`, `pytest-httpserver`.
- [x] `sdks/python/v1/.openapi-generator-ignore` — protect the above from regeneration.
- [x] `.github/workflows/python-sdk-tests.yml` — job `smoke`, on all PRs to develop.
- [ ] Mark `Python SDK tests / smoke` as a **required status check** on `develop`
      (branch-protection setting — see below). Needs repo admin; not a repo file.

## Enabling the required check (branch protection)

After the workflow has run at least once on a PR (so the context is known), add
it to `develop`'s required checks. Either via Settings → Branches → `develop` →
"Require status checks to pass" → add `Python SDK tests / smoke`, or:

```bash
gh api -X PATCH repos/Movement-Infrastructure/interactions-api-sdks/branches/develop/protection \
  -f 'required_status_checks[strict]=true' \
  -f 'required_status_checks[checks][][context]=Python SDK tests / smoke'
```

(Adjust the payload to preserve any existing protection settings.)

## Known limitations / follow-ups

- **Bootstrap window:** while `develop` has no committed spec, PRs that only
  edit the tests can't be exercised (nothing to generate against) and the check
  passes vacuously. Once the first sync PR merges, `develop` carries the spec
  and every subsequent PR runs the suite for real.
- **MIG-1917 plan note** said the smoke tests would be added as steps inside
  `generate-python-sdk.yml`. We chose a standalone workflow instead for a clean
  required check (see Decision above); the generate workflow is unchanged.
- The happy-path asserts on a few snake_cased response fields
  (`total_interactions`, `correlation_id`, `accepted_interactions.count`); if the
  spec's schema names change, update the assertions.
