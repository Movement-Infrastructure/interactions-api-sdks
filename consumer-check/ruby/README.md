# Ruby consumer check

Installs the Ruby SDK from outside its source tree and exercises it, optionally
against a live host. `sdks/ruby/v1/spec/` runs with the gemspec's `lib/` already
on the load path, so it cannot catch a file that `s.files` omits. This can.

Requires Ruby >= 3.0, the gemspec's floor. The repo pins 3.2.11 in
`.ruby-version`. macOS system Ruby is 2.6 and will fail to resolve.

## Sources

`SDK_SOURCE` selects the build under test.

```bash
# Local working tree, no commit needed. The fast loop.
SDK_SOURCE=path bundle install
SDK_SOURCE=path bundle exec ruby check.rb

# A pushed branch, resolved the way a consumer would.
SDK_SOURCE=git SDK_BRANCH=<branch> bundle install
SDK_SOURCE=git SDK_BRANCH=<branch> bundle exec ruby check.rb

# A published version.
SDK_SOURCE=gem SDK_VERSION=0.2.0.pre.1 bundle install
SDK_SOURCE=gem SDK_VERSION=0.2.0.pre.1 bundle exec ruby check.rb
```

`SDK_BRANCH` defaults to `develop`.

The `git` source clones over SSH and needs a working SSH key. Bundler clones
without a terminal, so a URL that asks for credentials fails with `could not
read Username for 'https://github.com'` instead of prompting.

Only `gem` exercises the real packaged artifact. `git` resolves files straight
from the repo, so anything excluded from `s.files` still loads and the omission
stays invisible until publish.

Delete `Gemfile.lock` when switching sources. It is gitignored for that reason.

## Live call

Without `DDX_API_KEY`, `check.rb` loads the gem, reports which build it
resolved, and exits. With one it also calls `GET /v{version}/auth/me`, a
read-only call that exercises connectivity, auth and deserialization together.

```bash
DDX_API_HOST=<api-host> DDX_API_KEY=<key> SDK_SOURCE=path bundle exec ruby check.rb
```

| Variable | Default |
| --- | --- |
| `DDX_API_HOST` | the gem's compiled-in default (`api.movementinfrastructure.org`) |
| `DDX_API_SCHEME` | `https` |
| `DDX_API_VERSION` | `1` |
| `DDX_API_KEY` | unset; live call skipped |

The key goes over HTTP basic in the password field with an empty username.
