# Ruby v1 publish leak audit

Per-language record for [`publish-leak-audit-checklist.md`](publish-leak-audit-checklist.md), run
before the Ruby SDK's first push to RubyGems.

- **Audited**: 2026-09-10
- **Artifact**: `ddx_interactions_api-0.1.0.gem`, built with `gem build` from a clean detached
  worktree at `e7aa4bd` — not from a working tree with build cruft in it
- **Registry**: RubyGems.org, OIDC trusted publishing, no stored token
- **Scanner**: gitleaks 8.30.1
- **Not covered**: section 5 is post-publish and cannot run until the first version is up

## 1. Registry credentials

- [x] OIDC trusted publishing, not a stored token. `rubygems/configure-rubygems-credentials@v2.1.0`
      exchanges the workflow's OIDC token for a short-lived credential. Nothing to mask, leak, or
      rotate.
- [x] Token scoping, `env:`-only reference — n/a, there is no token.
- [x] Publish job gated on the release branch and an environment. Fires on `push` to `main` under
      `sdks/ruby/v1/**`; `environment: rubygems` carries a `main`-only deployment branch policy,
      matching `pypi`. Only the `publish` job holds `id-token: write`, and it does nothing but
      download a prebuilt artifact and push it.
- [x] No `pull_request_target`, no `workflow_run` with a checkout of untrusted code.

## 2. Actions log hygiene

- [x] No `set -x`, `bash -x`, or `ACTIONS_STEP_DEBUG` in any Ruby workflow.
- [x] No step echoes a secret or a whole API response. The only `secrets.*` reference across the
      three Ruby workflows is `secrets.GITHUB_TOKEN` in the generate workflow, which needs it to
      push the regenerated SDK back to the PR branch.
- [x] Masking verified empirically — n/a. No secret is ever in scope on the publish path, which is
      the point of trusted publishing.
- [x] `persist-credentials: false` in every Ruby job that does not itself push.
      **Found and fixed during this audit**: `ruby-sdk-tests.yml` checked out with the default and
      never pushes, leaving a live token in `.git/config` while `bundle install` resolved and ran
      third-party gem code. It was the only workflow in the repo missing this. `generate-ruby-sdk.yml`
      does push, so it keeps credentials by necessity.
- [x] Client debug mode off in CI. `Configuration#debugging` defaults to `false` and no spec or
      workflow enables it.
- [x] No test authenticates against a real environment. The specs stub HTTP with webmock; no
      workflow references `DDX_API_KEY`. `consumer-check/ruby/` can make a live call but is
      developer-run and not wired into CI.
- [x] Failure paths reviewed. `ApiError` carries `code` and `response_body`; neither the specs nor
      the README examples print request headers, so the basic-auth credential is not echoed on the
      error path.

## 3. Package contents

- [x] Built from a clean checkout and **every** file enumerated: 62 files — 61 under `lib/` plus
      `README.md`. No `docs/`, `spec/`, `Gemfile`, `Gemfile.lock`, `Rakefile`, `.gemspec`, or
      `openapi-generator-config.yaml`. This is what the gemspec `s.files` patch exists to guarantee,
      and it is confirmed against the built artifact rather than read off the gemspec.
- [x] sdist/wheel split — n/a, a gem is a single artifact.
- [x] `.gitattributes export-ignore` not relied on. Exclusion comes from `s.files`, which is an
      explicit `Dir["lib/**/*"]` allowlist rather than a glob-minus-exclusions.
- [x] No credentials, tokens, private keys, `.env`, `.netrc`, or CI config in the artifact.
- [x] No local or runner filesystem paths. No `/Users/`, `/home/runner/`, `/github/workspace/`, or
      Windows drive paths.
- [x] Non-production hostnames — **one, accepted, not a blocker.**
      `lib/ddx_interactions_api/configuration.rb` ships `api-dev.movementinfrastructure.org` in its
      server list, copied verbatim from the spec's `servers:` block. It is a documented public test
      server, named as such in the top-level README, and the Python SDK ships it too. Recorded here
      so the decision is explicit rather than an oversight. The full host list in the artifact is
      `api.movementinfrastructure.org`, `api-dev.movementinfrastructure.org`, `demexchange.com`,
      `docs.ngpvan.com`, `github.com`, `rubygems.org`, `ruby-doc.org`, and
      `openapi-generator.tech`.
- [ ] **Internal implementation detail in a public docstring — open, fix upstream.**
      `models/exchange_interaction_status_dto_cursor_paginated_response_dto.rb:17` reads
      `Extends Minerva.Dto.Api.GetResponseDto\`1 with cursor-based pagination support.` That is a
      backend .NET namespace and type, including the generic-arity backtick, and it is shipped as a
      public docstring.
      It comes from the schema `description` on `ExchangeInteractionStatusDtoCursorPaginatedResponseDto`
      in `openapi/v1/swagger.json`, so it cannot be fixed here — edits under `sdks/` are overwritten
      on the next sync. **Fix the description in `mig-readme-docs` → `reference/mercury.json`.**
      Not Ruby-specific: the Python SDK already ships the same string in
      `models/exchange_interaction_status_dto_cursor_paginated_response_dto.py` and in
      `docs/ExchangeInteractionStatusDtoCursorPaginatedResponseDto.md`, so it is already public on
      TestPyPI.
      The model *names* `MinervaMetadataDto` and `MercuryDestinationVanApiKeyDto` carry internal
      service codenames too, but they are part of the published API contract and appear in the public
      API reference, so they are out of scope for this audit.
- [x] Package metadata is real: `DDx API Team`, `api@demexchange.com`, `MIT`,
      `https://github.com/Movement-Infrastructure/interactions-api-sdks`, `>= 3.0`. None of the
      generator defaults (`OpenAPI-Generator`, `team@openapitools.org`, `unlicense`, `0.0.0`)
      survive; `publish-ruby-rubygems.yml` re-checks all of them against the built artifact and
      refuses to publish otherwise.
- [x] README audited as published content. `README.md` ships inside the gem, so
      `scripts/verify_readme.py --language ruby` now gates it on both the PR and the publish path.
      It is produced by `templates/ruby/README.mustache`, which exists to remove the built-in
      template's git-URL install instructions, generator class name, and `YOUR_USERNAME` /
      `YOUR_PASSWORD` placeholders.
- [x] Scanned with a secret scanner, not just grep: `gitleaks detect --no-git` over the extracted
      artifact — 413 KB scanned, **no leaks found**. No false positives; the known Python
      `password='the-password'` docstring has no Ruby equivalent.

## 4. Repository and history

- [x] History-wide scan clean: `gitleaks git --log-opts="--all"` over 77 commits, 3.17 MB —
      **no leaks found**.
- [x] GitHub secret scanning **enabled**; push protection **enabled**.
- [x] No credential found at any point in history, so nothing to rotate.

Noted, outside this audit's scope: `code_security` and `dependabot_security_updates` are disabled on
the repo.

## 5. Post-publish verification — not yet run

Cannot run until the first version is on RubyGems. Do all three immediately after:

- [ ] Download the `.gem` back **from RubyGems** and re-enumerate it. What was built and what the
      registry serves are different artifacts until proven equal.
- [ ] `gem install ddx_interactions_api --pre` into a clean environment with no credential present,
      and `require` it, to confirm the package works without anything from the build machine.
- [ ] Review https://rubygems.org/gems/ddx_interactions_api as an anonymous visitor.

## Outcome

One issue fixed during the audit (`persist-credentials` in `ruby-sdk-tests.yml`) and one left open
that must be fixed in the upstream spec, not here (the `Minerva.Dto.Api` docstring). The open item
already ships in the Python SDK, so it does not block the Ruby publish any more than it blocked
Python's — but it should be corrected upstream before either registry page is treated as final.
