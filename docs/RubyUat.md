# Ruby SDK UAT guide

End-to-end validation of the published Ruby gem: install from RubyGems, authenticate, submit an interaction, and confirm it reached the Exchange.

Each step says what "good" looks like, so you can tell a real failure from
expected output.

---

## 1. Prerequisites

- **Ruby 3.0 or later.** 
- **An Interactions API key for production.** See
  [Authentication](https://docs.movementinfrastructure.org/docs/interactions-api-authentication).

Your key should look like `12345.<secret>`: a numeric key ID, a dot, then a base64
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
    raise "no dot separator in key" if secret.to_s.empty?
    Base64.strict_decode64(secret)
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

gem install ddx_interactions_api --install-dir ./vendor
export GEM_HOME="$PWD/vendor" GEM_PATH="$PWD/vendor"
```

`--install-dir` keeps the gem out of your system Ruby, which is what makes this
a clean-environment test.

### Expected result

```bash
gem list ddx_interactions_api
#   ddx_interactions_api (0.1.0)
```

The gem name is underscored, and so is the require path
(`require "ddx_interactions_api"`).

---

## 3. Authenticate, and check what your key can reach

```bash
ruby - <<'RUBY'
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
  cid = (e.response_headers || {})["x-correlation-id"] || "none"
  warn "  A 401 here has several causes. See Common failure modes." if e.code == 401
  abort "auth/me failed: HTTP #{e.code}\n  x-correlation-id: #{cid}\n  body: #{e.response_body.to_s.empty? ? "(empty)" : e.response_body}"
end

puts "workspace:    #{me.workspace.display_name} (#{me.workspace.workspace_id})"
(me.destinations || []).each do |d|
  puts "destination:  #{d.name}  is_van_destination=#{d.is_van_destination}"
end
puts "destinations: #{me.destinations&.any? ? 'see above' : 'none'}"
puts "van key:      #{me.van_api_key ? 'present' : 'none'}"
RUBY
```

### Expected Result

`target:` prints `https://api.movementinfrastructure.org`, and your workspace
name and ID print without an exception.

**Read the `destinations` and `van key` lines before continuing.** They decide
what step 4 actually does:

- **A destination with `is_van_destination=true`** - what you submit is
  forwarded to VAN as a real canvass response. Coordinate before submitting.
- **Other destinations** - the Exchange is itself a destination, so a key that
  routes there lists it here like any other.
- **An empty list** - nothing routes what you submit, the Exchange included.

Authentication is HTTP Basic with the **API key in the password field and an
empty username**. That surprises people; it is correct.

Note `config.host` takes a bare host with no scheme, `config.scheme` is
separate and defaults to `https`.

---

## 4. Submit an interaction

Replace `vendorSource`, `committee`, and `person` with identifiers your
workspace actually has. Left as placeholders they will be rejected.

```bash
ruby - <<'RUBY'
require "ddx_interactions_api"
require "json"

config = DdxInteractionsApi::Configuration.new
config.username = ""
config.password = ENV.fetch("DDX_API_KEY")

interactions = DdxInteractionsApi::InteractionsApi.new(
  DdxInteractionsApi::ApiClient.new(config)
)

stamp = Time.now.utc.strftime("%Y-%m-%dT%H:%M:%SZ")

payload = DdxInteractionsApi::InteractionsDto.new(
  interactions: [
    DdxInteractionsApi::InteractionDto.new(
      state_code: "CA",
      attempt_date_time: stamp,
      method: "phone_call",
      outcome: "successful_contact",
      vendor_source: "<your vendor>",
    committee: [{ type: "<your type>", id: "<your committee id>" }],
    person:    [{ type: "<your type>", id: "<your person id>" }],
      json_metadata: JSON.generate({ uat: true, posted_at: stamp })
    )
  ]
)

begin
  result = interactions.vversion_interactions_post("1", interactions_dto: payload)
rescue DdxInteractionsApi::ApiError => e
  cid = (e.response_headers || {})["x-correlation-id"] || "none"
  abort "post failed: HTTP #{e.code}\n  x-correlation-id: #{cid}\n  body: #{e.response_body.to_s.empty? ? "(empty)" : e.response_body}"
end

puts "correlationId: #{result.correlation_id}"
puts "accepted: #{result.accepted_interactions.count}  rejected: #{result.rejected_interactions.count}"
(result.accepted_interactions.data || []).each do |row|
  puts "  accepted idx #{row.index}: interactionId #{row.interaction_id}"
end
(result.rejected_interactions.data || []).each do |row|
  (row.errors || []).each do |err|
    puts "  rejected idx #{row.index}: #{err.field}: #{err.error_message}"
  end
end
RUBY
```

### Expected Result

A `correlationId`, and `accepted` equal to the number of rows you sent.

**Keep an `interactionId`** from the accepted list. Step 5 exports it.

The cap is **100 interactions per request**.

### Valid enum values

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

## 5. Put the interaction ID in your environment

```bash
export INTERACTION_ID='<interactionId from step 4>'
```

---

## 6. Look up the interaction's transaction records

```bash
ruby - <<'RUBY'
require "ddx_interactions_api"

config = DdxInteractionsApi::Configuration.new
config.username = ""
config.password = ENV.fetch("DDX_API_KEY")

interactions = DdxInteractionsApi::InteractionsApi.new(
  DdxInteractionsApi::ApiClient.new(config)
)

begin
  txns = interactions.vversion_interactions_interaction_id_transactions_get(
    ENV.fetch("INTERACTION_ID"), "1", show_only_failed_transactions: false
  )
rescue DdxInteractionsApi::ApiError => e
  cid = (e.response_headers || {})["x-correlation-id"] || "none"
  warn "  A 404 usually means you passed a correlationId. See step 5." if e.code == 404
  abort "transactions lookup failed: HTTP #{e.code}\n  x-correlation-id: #{cid}\n  body: #{e.response_body.to_s.empty? ? "(empty)" : e.response_body}"
end

puts "count: #{txns.metadata&.count || 0}"
(txns.data || []).each do |row|
  puts "  #{row.date_created_utc}  #{row.status}"
  (row.logs || []).each do |log|
    puts "      HTTP #{log.response_status_code}  #{log.response}"
  end
end
RUBY
```

### Expected Result

The call returns immediately. What it contains depends on where your workspace
routes interactions, which step 3 told you:

- **A destination with `is_van_destination` set**: a row per delivery attempt,
  each with a status of `Received`, `Processing`, `Success`, `Failed`,
  `Invalid`, `Duplicate`, or `InternalError`, plus any response logs recorded
  for it.
- **No VAN destination**: `count: 0` and no rows. Only the VAN send path writes
  these records. A key that routes to the Exchange has a destination and still
  returns `count: 0` here, because the Exchange is reported by exchange status
  instead.

`count: 0` is a valid result, not a failure. What this step verifies is that the
call authenticates, returns a parsed response, and reports whatever records
exist for the interaction you submitted.

`show_only_failed_transactions` is set to false on purpose. It defaults to true,
which returns only `Failed`, `Invalid`, and `Duplicate` rows and would hide a
successful delivery.

Exchange delivery is reported by a different endpoint,
`interactions/exchange-status`. It advances on a scheduled transformation rather
than on your request and can lag by up to an hour, so it is outside this UAT.

The interactive reference is at
[docs.movementinfrastructure.org/reference](https://docs.movementinfrastructure.org/reference/interactions).

---

## 7. Common failure modes

| Symptom | Likely cause |
|---|---|
| `Bundler could not find compatible versions` | Ruby 2.6 (macOS system Ruby). Use 3.0 or later. |
| `401 Unauthorized`, empty body | Key missing the `<keyId>.` prefix; secret not valid base64; key issued for a different environment; key revoked or expired; workspace suppressed; or the key lacks the required role. |
| `ArgumentError: ... is not a valid attribute` | A misspelled field name. `build_from_hash` rejects unknown keys. |
| Rows rejected with a per-row error | Per-row validation. Read `rejected_interactions.data[].errors`. |
| `404` from step 6 | You passed the `correlationId`. That route takes a GUID `interactionId` only, and correlation IDs are either a numeric trace ID or `mig-` prefixed. Use an ID from the accepted list in step 4. |
| Step 6 returns `count: 0` | The key has no destination with `is_van_destination` set, so no transaction record exists; or `show_only_failed_transactions` was left at its default of true. |

### On that 401

The 401 is deliberately generic and covers several distinct causes: including
a **valid key that simply lacks the required role**, which is an authorization
failure reported as an authentication one. If the key shape checks out in
step 1, ask the API team to check server-side logs rather than guessing.

`ApiError#response_body` carries the API's explanation; the exception message
alone is only the status line.

---

## 8. Where the model docs live

The gemspec ships `lib/**` and `README.md` only, so `docs/*.md` are not inside
the installed gem. The model links in the README point back at
[this repo](https://github.com/Movement-Infrastructure/interactions-api-sdks/tree/main/sdks/ruby/v1/docs),
and the interactive reference is at
[docs.movementinfrastructure.org/reference](https://docs.movementinfrastructure.org/reference/interactions).

---

## 9. Sign-off checklist

- [ ] Installed from RubyGems into a clean `GEM_HOME`
- [ ] `auth/me` returned the expected workspace
- [ ] Reviewed `destinations` / `van key` before submitting
- [ ] Submitted an interaction and received a `correlationId`
- [ ] Rejected rows, if any, reported a usable per-row reason
- [ ] Retrieved transaction records for an accepted `interactionId`,
      with `show_only_failed_transactions` set to false
- [ ] Filed anything unexpected, with version and `correlationId`
