# interactions-api-sdks

Auto-generated SDKs for the [Movement Infrastructure Interactions API](https://api.movementinfrastructure.org).

This repository is **private** during development and will be made public when the first SDK is ready to publish to a public package registry.

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
3. CI on the PR regenerates each language SDK and bumps the package version from the PR's labels — minor by default, patch or major if labelled.
4. Sync PRs merge to `develop`. Promoting `develop` → `main` is the deliberate act that releases: CI builds each package and publishes it to its registry.

## Status

Bootstrapping. Python is the first language through the pipeline; the other
`sdks/*` directories are placeholders.
