# Ruby SDK UAT guide

End-to-end validation of the published Ruby gem: install from RubyGems, authenticate, submit an interaction, and confirm it reached the Exchange.

Each step says what "good" looks like, so you can tell a real failure from
expected output.

---

## 1. Prerequisites

- **Ruby 3.0 or later.** 
- **An Interactions API key for production.** See
  [Authentication](https://docs.movementinfrastructure.org/docs/interactions-api-authentication).

Your key should look like `12345.<secret>` — a numeric key ID, a dot, then a base64
secret. **Both halves are required.**

Keys are environment-specific. A key issued for the public test server will not
work against production.

```bash
export DDX_API_KEY='12345.your-secret-here'
ruby -v   # expect 3.0 or later
```

Check the shape before going further:

```bash
ruby -rbase64 -e '
  kid, secret = ENV.fetch("DDX_API_KEY").split(".", 2)
  puts "key id numeric: #{kid.to_s.match?(/\A\d+\z/)}"
  begin
    Base64.strict_decode64(secret.to_s)
    puts "secret is valid base64: true"
  rescue => e
    puts "secret is NOT valid base64: #{e.message}"
  end
'
```

Both must be true.

---

## 2. Install from RubyGems into a clean environment

```bash
mkdir -p /tmp/ddx-uat && cd /tmp/ddx-uat

gem install ddx_interactions_api --pre --install-dir ./vendor
export GEM_HOME="$PWD/vendor" GEM_PATH="$PWD/vendor"
```

**`--pre` is required.** Every release is a prerelease (`X.Y.Z.pre.N`), and both
`gem install` and Bundler skip prereleases unless asked. Without it the install
finds nothing.

`--install-dir` keeps the gem out of your system Ruby, which is what makes this
a clean-environment test.

### Expected result

```bash
gem list ddx_interactions_api
#   ddx_interactions_api (0.1.0.pre.N)
```

The gem name is underscored, and so is the require path
(`require "ddx_interactions_api"`).

---

## 3. Authenticate, and check what your key can reach

```ruby
require "ddx_interactions_api"

config = DdxInteractionsApi::Configuration.new
# Host only, no scheme. Defaults to the production API.
config.username = ""                       # empty on purpose
config.password = ENV.fetch("DDX_API_KEY")

puts "target: #{config.scheme}://#{config.host}"

client = DdxInteractionsApi::ApiClient.new(config)

begin
  me = DdxInteractionsApi::AuthenticationDetailsApi.new(client).vversion_auth_me_get("1")
rescue DdxInteractionsApi::ApiError => e
  # The exception message is only the status line; the body says why.
  abort "auth/me failed: HTTP #{e.code}\n#{e.response_body}"
end

puts "workspace:    #{me.workspace.display_name} (#{me.workspace.workspace_id})"
puts "destinations: #{me.destinations&.any? ? me.destinations : 'none'}"
puts "van key:      #{me.van_api_key ? 'present' : 'none'}"
```

### Expected Result

`target:` prints `https://api.movementinfrastructure.org`, and your workspace
name and ID print without an exception.

**Read the `destinations` and `van key` lines before continuing.** They decide
what step 4 actually does:

- **Both empty** — interactions land in the Exchange and go no further.
- **Either populated** — what you submit is forwarded to those systems, and for
  VAN that means real canvass responses. Coordinate before submitting.

Authentication is HTTP Basic with the **API key in the password field and an
empty username**. That surprises people; it is correct.

Note `config.host` takes a bare host with no scheme — `config.scheme` is
separate and defaults to `https`.

---

## 4. Submit an interaction

Replace `vendorSource`, `committee`, and `person` with identifiers your
workspace actually has. Left as placeholders they will be rejected.

```ruby
require "ddx_interactions_api"
require "json"

config = DdxInteractionsApi::Configuration.new
config.username = ""
config.password = ENV.fetch("DDX_API_KEY")

interactions = DdxInteractionsApi::InteractionsApi.new(
  DdxInteractionsApi::ApiClient.new(config)
)

stamp = Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ")

payload = DdxInteractionsApi::InteractionsDto.build_from_hash({
  interactions: [{
    stateCode: "CA",
    attemptDateTime: stamp,
    method: "phone_call",
    outcome: "successful_contact",
    vendorSource: "<your vendor name>",
    committee: [{ type: "<your type>", id: "<your committee id>" }],
    person:    [{ type: "<your type>", id: "<your person id>" }],
    jsonMetadata: JSON.generate({ uat: true, posted_at: stamp }),
  }]
})

begin
  result = interactions.vversion_interactions_post("1", interactions_dto: payload)
rescue DdxInteractionsApi::ApiError => e
  abort "post failed: HTTP #{e.code}\n#{e.response_body}"
end

puts "correlationId: #{result.correlation_id}"
puts "accepted: #{result.accepted_interactions.count}  rejected: #{result.rejected_interactions.count}"
(result.rejected_interactions.data || []).each do |row|
  (row.errors || []).each do |err|
    puts "  rejected idx #{row.index}: #{err.field_name}: #{err.error_message}"
  end
end
```

### Expected Result

A `correlationId`, and `accepted` equal to the number of rows you sent.

**Keep the `correlationId`** — it is the only handle for step 5.

The cap is **100 interactions per request**.

### Valid enum values

These are **not** shipped in the gem:

- `method`: `unknown`, `mail`, `letter`, `digital_ad`, `email`, `text`,
  `text_broadcast`, `robo_call`, `dialer_call`, `phone_call`, `door_knock`,
  `Event`, `hot_spot`, `one_on_one`, `web_interaction`
- `outcome`: `unknown`, `clicked_link`, `email_opened`, `submitted_form`,
  `successful_contact`, `deceased`, `deliverability_error`,
  `permanently_undeliverable`, `inaccessible`, `language_barrier`, `moved`,
  `no_answer`, `wrong_number`, `hostile`, `marked_spam`, `refused`,
  `delivered`, `lit_drop`, `left_message`, `other`

`Event` is the one capitalised value, exactly as written.

---

## 5. Verify it reached the Exchange

```ruby
require "ddx_interactions_api"

config = DdxInteractionsApi::Configuration.new
config.username = ""
config.password = ENV.fetch("DDX_API_KEY")

interactions = DdxInteractionsApi::InteractionsApi.new(
  DdxInteractionsApi::ApiClient.new(config)
)

statuses = interactions.vversion_interactions_exchange_status_get(
  "1", correlation_id: ENV.fetch("CORRELATION_ID"), limit: 100
)

(statuses.data || []).each do |row|
  puts "  #{row.interaction_id}  #{row.status}"
end
```

Run with `CORRELATION_ID=<id from step 4>`.

### Expected Result

One row per accepted interaction, progressing to a terminal status.

The Exchange is asynchronous, so an immediate call may return an early status
or no rows. Re-run after a few seconds before calling it a failure.

The interactive reference is at
[docs.movementinfrastructure.org/reference](https://docs.movementinfrastructure.org/reference/interactions).

---

## 6. Common failure modes

| Symptom | Likely cause |
|---|---|
| `gem install` finds nothing | Missing `--pre`. Every release is a prerelease. |
| `Bundler could not find compatible versions` | Ruby 2.6 (macOS system Ruby). Use 3.0 or later. |
| `401 Unauthorized`, empty body | Key missing the `<keyId>.` prefix; secret not valid base64; key issued for a different environment; key revoked or expired; workspace suppressed; or the key lacks the required role. |
| `ArgumentError: ... is not a valid attribute` | A misspelled field name. `build_from_hash` rejects unknown keys. |
| Rows rejected with a per-row error | Per-row validation. Read `rejected_interactions.data[].errors`. |
| Status query returns nothing | The Exchange is asynchronous. Retry after a few seconds. |

### On that 401

The 401 is deliberately generic and covers several distinct causes — including
a **valid key that simply lacks the required role**, which is an authorization
failure reported as an authentication one. If the key shape checks out in
step 1, ask the API team to check server-side logs rather than guessing.

`ApiError#response_body` carries the API's explanation; the exception message
alone is only the status line.

---

## 7. Where the model docs live

The gemspec ships `lib/**` and `README.md` only, so `docs/*.md` are not inside
the installed gem. The model links in the README point back at
[this repo](https://github.com/Movement-Infrastructure/interactions-api-sdks/tree/main/sdks/ruby/v1/docs),
and the interactive reference is at
[docs.movementinfrastructure.org/reference](https://docs.movementinfrastructure.org/reference/interactions).

---

## 8. Sign-off checklist

- [ ] Installed from RubyGems with `--pre` into a clean `GEM_HOME`
- [ ] `auth/me` returned the expected workspace
- [ ] Reviewed `destinations` / `van key` before submitting
- [ ] Submitted an interaction and received a `correlationId`
- [ ] Rejected rows, if any, reported a usable per-row reason
- [ ] Exchange status reached a terminal state for each accepted interaction
- [ ] Filed anything unexpected, with version and `correlationId`
