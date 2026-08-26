# interactions-api-sdks

Auto-generated SDKs for the [Movement Infrastructure Interactions API](https://api.movementinfrastructure.org).

This repository is **private** during development and will be made public when the first SDK is ready to publish to a public package registry.

This readme of devloper details will need to move to a new home before that time.

## Layout

```
interactions-api-sdks/
├── openapi/
│   └── v1/
│       └── swagger.json        # synced from mig-readme-docs (reference/mercury.json)
└── sdks/
    ├── python/v1/
    ├── node/v1/
    ├── csharp/v1/
    ├── kotlin/v1/
    ├── swift/v1/
    ├── ruby/v1/
    └── php/v1/
```

Each language directory contains a generated SDK produced by [`openapi-generator`](https://openapi-generator.tech/) from `openapi/v1/swagger.json`. The spec is the source of truth and is pulled from the [`mig-readme-docs`](https://github.com/Movement-Infrastructure/mig-readme-docs) repository on a schedule.

## How it works

1. A scheduled GitHub Action (`.github/workflows/sync-spec.yml`, hourly at :17) fetches the current `reference/mercury.json` from `mig-readme-docs`.
2. If it differs from the committed `openapi/v1/swagger.json`, a PR is opened against this repo.
3. CI on the PR regenerates each language SDK and bumps the package version from the PR's labels — minor by default, patch or major if labelled. See [Versioning](#versioning).
4. Sync PRs merge to `develop`. Promoting `develop` → `main` is the deliberate act that releases: CI builds each package and publishes it to its registry. See [Publishing](#publishing).

## Internal developer setup

Everything an internal developer needs to operate and modify the sync/generate pipeline. None of this is relevant to SDK consumers.

### GitHub Apps

Two GitHub Apps power the automation. Each authenticates at workflow runtime by minting a short-lived installation token (~1h) from its private key, so there is no long-lived API token to rotate.

- **`interactions-api-sdk-sync`** — installed on `mig-readme-docs` with `Contents: Read` only. The scheduled sync workflow uses it to read `reference/mercury.json`. No other access on `mig-readme-docs`; no access to any other repo.
- **`interactions-api-sdk-generator-bot`** — installed on `interactions-api-sdks` with `Contents: Write` and `Pull requests: Write`. Used by the sync workflow to open sync PRs, and by the generate workflow to commit regenerated SDKs back to PR branches. Authoring under this App (instead of the default `GITHUB_TOKEN`) is what lets downstream workflows fire on its commits.

### Credentials storage

All credentials are stored on this repo under `Settings → Secrets and variables → Actions`. Backup copies of every value are kept in 1Password (**Eng Admin** vault).

| Name | Type | Belongs to | Contents |
| --- | --- | --- | --- |
| `READMEDOCS_SYNC_APP_ID` | Variable | `interactions-api-sdk-sync` | App ID, shown on the App's settings page. |
| `READMEDOCS_SYNC_PRIVATE_KEY` | Secret | `interactions-api-sdk-sync` | Full contents of the `.pem` private key, including the `-----BEGIN/END RSA PRIVATE KEY-----` lines. |
| `SDK_GENERATOR_APP_ID` | Variable | `interactions-api-sdk-generator-bot` | App ID, shown on the App's settings page. |
| `SDK_GENERATOR_PRIVATE_KEY` | Secret | `interactions-api-sdk-generator-bot` | Full contents of the `.pem` private key, including the `-----BEGIN/END RSA PRIVATE KEY-----` lines. |

### Rotation

- **App IDs and Installation IDs** do not rotate. They only change if the App is recreated or reinstalled.
- **Private key** rotation (same procedure for either App):
  1. Generate a new private key on the App's settings page. Download the `.pem` file.
  2. Update the corresponding `*_PRIVATE_KEY` secret on this repo and the matching 1Password entry.
  3. Confirm the sync/generate workflows run green with the new key.
  4. Delete the old private key from the App's settings page.

No fixed rotation cadence is required, since installation tokens are minted fresh each run. Rotate immediately if a private key is suspected to be compromised.

### Configuration toggles

| Variable | Default | Purpose |
| --- | --- | --- |
| `READMEDOCS_SYNC_BRANCH` | unset (default branch) | Override which branch of `mig-readme-docs` the sync workflow reads `reference/mercury.json` from. Useful for validating the sync against in-flight branches. Set to a branch name; a tag or commit SHA also works. The workflow logs the resolved value at the top of each run. |

### Running the sync by hand

`sync-spec.yml` runs hourly at :17, and can also be triggered from **Actions → Sync OpenAPI spec from mig-readme-docs → Run workflow**. The optional `upstream_ref` input overrides which ref of `mig-readme-docs` that run reads from, and takes precedence over `READMEDOCS_SYNC_BRANCH` — use it for a one-off check against an in-flight branch without leaving a repo variable set.

Re-running the sync is safe. The branch name (`sync/mercury-<short-sha>`) is derived from the upstream commit that last touched the spec, so a run that finds an open PR for that SHA leaves it alone rather than opening a duplicate.

### Versioning

Package versions live in each SDK's `openapi-generator-config.yaml` as `packageVersion`, and flow from there into the generated manifest (`pyproject.toml` / `setup.py` for Python). That config field is the source of truth — nothing edits the generated manifest directly.

`generate-python-sdk.yml` rewrites it on every sync PR via `scripts/bump_version.py`, before running the generator, so the bump and the code it produced land in one commit.

| Label | Effect |
| --- | --- |
| `interactions-api-major` | Bumps major (A). Wins over the others. Requires a CODEOWNERS approval acknowledging the break — see the [MIG-1926](https://linear.app/movementinfrastructure/issue/MIG-1926) runbook. |
| `interactions-api-patch` | Bumps patch (C). |
| `interactions-api-minor` | None. Minor (B) is the default when no other label is present. |

Two properties worth knowing:

- **The bump is computed from the base branch**, not the PR branch. Pushing again or toggling a label recomputes the same version rather than stacking a second bump — a PR always lands exactly one bump ahead of its base.
- **Precedence is largest-wins.** A PR carrying both the major and patch labels is contradictory; the script honors the declared breaking change.

A major bump emits an Actions `::notice::` so it's visible in the run log rather than passing as another line of output. `--force-bump` overrides the labels entirely, for out-of-band bumps not driven by a PR.

Dry-run the script against any config without writing:

```bash
python scripts/bump_version.py \
  --current-config sdks/python/v1/openapi-generator-config.yaml \
  --labels-json '["interactions-api-patch"]'
```

Its unit tests run on every PR via `tooling-tests.yml`:

```bash
pip install -r scripts/requirements-test.txt
pytest scripts/tests -q
```

### Publishing

Two branches, two roles. `develop` is where sync PRs land and where the version is computed. `main` is the release branch — pushing to it publishes.

```
sync PR ──merge──> develop ──promotion PR──> main ──> TestPyPI
```

`publish-python-testpypi.yml` fires on push to `main` under `sdks/python/v1/**`, or on manual dispatch. It builds the sdist and wheel from the committed SDK (nothing is regenerated at publish time), gates on package metadata, then uploads.

**Authentication is OIDC trusted publishing — there is no token.** The publish job mints a short-lived OIDC token that TestPyPI exchanges for a one-time upload grant. Nothing to store in secrets, mask in logs, or rotate, which is what section 1 of [the leak-audit checklist](docs/publish-leak-audit-checklist.md) asks for.

Three properties the workflow relies on, each worth preserving if you edit it:

- **The trusted publisher is bound to this file's name.** Renaming `publish-python-testpypi.yml` breaks publishing until the TestPyPI publisher config is updated to match.
- **Build and publish are separate jobs.** Only `publish` has `id-token: write`, and it does nothing but download a prebuilt artifact and upload it. No generated or third-party code executes with the credential in scope.
- **The build job checks out with `persist-credentials: false`.** The default leaves an unmasked live token in `.git/config` as an `http.extraheader`, readable by any tooling that runs afterwards.

Every run writes the full sdist and wheel file listings to the job summary, so the artifact enumeration the checklist requires becomes a permanent per-release record rather than something done by hand once.

The metadata gate fails the release on the generated defaults the audit flagged (`team@openapitools.org`, `OpenAPI Generator Community`, version `0.0.0`). `twine check` does not catch these — it validates that the long description renders, not that the author is a real person.

**First-time setup**, once per registry:

1. Create the `main` branch from `develop`.
2. On TestPyPI, add a *pending publisher* under Publishing: PyPI project name `ddx-interactions-api`, owner `Movement-Infrastructure`, repository `interactions-api-sdks`, workflow `publish-python-testpypi.yml`, environment `testpypi`. Pending publishers work before the project exists — the first upload creates it.

   The project name is the one field that is *not* the repository name, and it must match `projectName` in `sdks/python/v1/openapi-generator-config.yaml`. Get it wrong and the OIDC handshake still succeeds — the upload then fails at the end with `400 Non-user identities cannot create new projects`, because the identity is only allowed to create the project its pending publisher names.
3. Create a GitHub Environment named `testpypi` on this repo. Attach required reviewers if a release should need a human gate.

## Status

Bootstrapping. See the [auto-generated SDKs plan](https://github.com/Movement-Infrastructure/minerva/blob/develop/Plans/AutoGeneratedSDKs.md) and the [Mercury SDKs Linear project](https://linear.app/movementinfrastructure/project/mercury-sdks-4d0ee2eb499d) for current progress.
