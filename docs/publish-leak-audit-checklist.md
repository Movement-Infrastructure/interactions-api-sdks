# SDK publish leak-audit checklist

Reusable pre-publish audit for every language SDK in this repo.

Run this **once per language, against a real build artifact**, before that language's first publish to
any registry — and again before the test → production registry flip. Copy the checklist somewhere
per-language and tick items there rather than editing this file.

Two things are being audited, and they fail in different ways:

- **Actions logs** — a credential that reaches a log line is disclosed to everyone with read access to
  the run, and Actions logs outlive the run.
- **Package contents** — anything inside the published artifact is permanent and world-readable once
  it hits a public registry. Yanking a version does not unpublish the file.

---

## 1. Registry credentials

- [ ] **Prefer OIDC trusted publishing over a stored token.** PyPI/TestPyPI, npm, RubyGems, NuGet, and
      Maven Central all support it. There is no secret to leak, mask, or rotate — the strongest single
      control available, and it removes most of section 2 from scope.
- [ ] If a token is unavoidable, it is scoped to the single package (not account-wide) and stored as a
      repo **secret**, never a **variable**. Variables are not masked in logs.
- [ ] Token is referenced only via `env:` on the publishing step, never passed as a command-line
      argument. Arguments appear in `ps` output and in `set -x` traces; env vars do not.
- [ ] Publish job is gated on the default branch / a tag, and uses a
      [GitHub Environment](https://docs.github.com/en/actions/deployment/targeting-different-environments)
      so the credential is not readable by workflows on arbitrary branches.
- [ ] Publish workflow does **not** use `pull_request_target` or `workflow_run` with a checkout of
      untrusted PR code. Those run with secrets in scope against code the author controls.

## 2. Actions log hygiene

- [ ] No `set -x` (or `bash -x`, `ACTIONS_STEP_DEBUG`) in any job that has a credential in scope.
- [ ] No step echoes a secret, an auth header, or a whole API response that may embed one. Assigning
      to a shell variable is fine; `echo`ing it is not.
- [ ] **Verify masking empirically, don't assume it.** GitHub masks only exact literal matches of
      registered secrets. A secret that has been base64'd, URL-encoded, JSON-escaped, or embedded in a
      derived value (e.g. a `Basic` auth header built from a token) prints **unmasked**. Search a real
      run's logs for a distinctive substring of the credential.
- [ ] `actions/checkout` runs with `persist-credentials: false` in any job that does not itself push.
      The default writes an `http.extraheader` credential into `.git/config` as
      `base64("x-access-token:<token>")` — an unmasked form of a live token sitting in the workspace
      that third-party build tooling can read.
- [ ] The client's debug/verbose mode is **off** in CI. Generated OpenAPI clients wire a debug flag
      straight into the HTTP layer's header tracing (for Python, `Configuration.debug = True` sets
      `http.client.HTTPConnection.debuglevel = 1`), which prints full request headers — including
      `Authorization` — to stdout.
- [ ] No test or example in CI authenticates against a real environment with a real key. If a
      staging-API test is genuinely needed, keep it out of the published package and out of any job
      whose logs are broadly readable.
- [ ] Failure paths reviewed, not just the happy path. Exception traces and `--verbose` retry output
      are where credentials usually surface. Read the log of a **deliberately failed** publish.

## 3. Package contents

Build the real artifact and enumerate it. Do not reason from config files — packaging tools disagree
with each other about what "excluded" means.

- [ ] Artifact built locally from a clean checkout, and **every** file listed:
      - Python: `python -m build`, then `tar tzf dist/*.tar.gz` **and** `unzip -l dist/*.whl`
      - Node: `npm pack --dry-run`
      - Ruby: `gem contents` / `tar tf` the `.gem`
      - C#: `unzip -l *.nupkg`
      - Kotlin/Java: `unzip -l *.jar` (and the `-sources.jar`)
      - Swift: the published source tree is the git tag itself — audit `git archive` output
- [ ] **sdist and wheel audited separately.** They are built by different code paths and routinely
      differ. Confirmed on the Python SDK: `find_packages(exclude=[...])` keeps tests out of the wheel
      while setuptools' default sdist manifest ships `tests/test*.py` anyway.
- [ ] `.gitattributes export-ignore` is **not** relied on for package exclusion. It only affects
      `git archive`, i.e. GitHub's "Source code (tar.gz)" release assets. It has zero effect on a
      wheel, sdist, npm tarball, gem, or nupkg.
- [ ] No credentials, tokens, private keys, `.env`, `.netrc`, or CI config in the artifact.
- [ ] No local or runner filesystem paths (`/Users/…`, `/home/runner/…`, `/github/workspace/…`,
      `C:\…`). These leak developer identities and CI layout.
- [ ] No internal hostnames or non-production environment URLs. **Check the spec's `servers:` block** —
      it is copied verbatim into the client. The Python SDK currently ships
      `api-dev.movementinfrastructure.org` in its host list.
- [ ] No internal implementation details in public docstrings — backend type names, namespaces, table
      or queue names. These come from the spec's schema `description` fields.
- [ ] Package metadata is real: author, author email, license, repository URL, version. Generated
      defaults (`OpenAPI Generator Community`, `team@openapitools.org`, `NoLicense`, `0.0.0`) are
      publish blockers, and the author email is a third party's address.
- [ ] **Long description / README audited as published content.** It renders on the registry's public
      project page. The spec's `info.description` flows into it, into the file header of every
      generated source file, and into `PKG-INFO`/`METADATA`.
- [ ] Artifact scanned with a secret scanner, not just grep — e.g.
      `gitleaks detect --no-git --source <extracted-dir>` or `trufflehog filesystem <dir>`.
      Expect one known false positive in generated Python clients: `password='the-password'` in
      `configuration.py`'s docstring example.

## 4. Repository and history

- [ ] `git log -p` / a history-wide scanner shows no committed credential on **any** ref, including
      deleted and bot-authored branches. A private repo going public exposes all of them.
- [ ] GitHub secret scanning and push protection enabled on the repo (free for public repos; requires
      Advanced Security while private).
- [ ] Any credential found at any point in history is **rotated**, not just deleted. Assume disclosure.

## 5. Post-publish verification

- [ ] Artifact downloaded back **from the registry** and re-enumerated. What you built and what the
      registry serves are not guaranteed identical — this is the only check that covers the publish
      step itself.
- [ ] Installed into a clean environment and imported, with no credential present, to confirm the
      package does not depend on something that only existed in CI.
- [ ] Registry project page reviewed as an anonymous visitor.

---

## If a credential was disclosed

1. **Rotate first.** Revoke at the provider before anything else; deleting the log or yanking the
   version does not un-disclose it.
2. Delete the affected Actions log run and yank the affected package version.
3. Assume the value was scraped. Public-registry uploads and public repo pushes are indexed within
   minutes.
4. Record what leaked, how, and the control added — then add the missing control to this
   checklist so the next language inherits it.
