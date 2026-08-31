#!/usr/bin/env ruby
# frozen_string_literal: true

# Consumer-side check for the Ruby SDK. Run under `bundle exec` so the gem
# resolves through consumer-check/ruby/Gemfile rather than the source tree.
#
# Without DDX_API_KEY this only loads the gem and reports what it resolved,
# which is enough to catch a broken build and is safe to run anywhere. With a
# key it also calls GET /v{version}/auth/me -- read-only, and the cheapest call
# that proves connectivity, auth and deserialization all work end to end.

require "ddx_interactions_api"

API_VERSION = ENV.fetch("DDX_API_VERSION", "1")

spec = Gem.loaded_specs["ddx_interactions_api"]

# Which build actually got installed. The whole point of this harness is that
# this is a question with a non-obvious answer.
puts "version:  #{DdxInteractionsApi::VERSION}"
puts "resolved: #{spec.source}"
puts "path:     #{spec.full_gem_path}"

api_key = ENV["DDX_API_KEY"]
if api_key.nil? || api_key.empty?
  puts "\nDDX_API_KEY unset; skipping the live call."
  exit 0
end

config = DdxInteractionsApi::Configuration.new
config.scheme = ENV.fetch("DDX_API_SCHEME", "https")
config.host = ENV.fetch("DDX_API_HOST", DdxInteractionsApi::Configuration.default.host)
# HTTP basic with the API key in the password field and an empty username.
config.username = ""
config.password = api_key

puts "target:   #{config.scheme}://#{config.host}"

client = DdxInteractionsApi::ApiClient.new(config)

begin
  me = DdxInteractionsApi::AuthenticationDetailsApi.new(client)
                                                   .vversion_auth_me_get(API_VERSION)
rescue DdxInteractionsApi::ApiError => e
  # Print the body: the SDK's message is just the status line, and the body is
  # where the API says why.
  warn "\nauth/me failed: HTTP #{e.code}"
  warn e.response_body.to_s
  exit 1
end

puts "\nauth/me OK"
puts me.to_hash.inspect
