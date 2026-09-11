#!/usr/bin/env ruby
# frozen_string_literal: true

# Consumer-side check for the Ruby SDK. Run under `bundle exec` so the gem
# resolves through this directory's Gemfile rather than the source tree.
#
# Without DDX_API_KEY it loads the gem and reports what it resolved. With one it
# also calls GET /v{version}/auth/me, a read-only call that exercises
# connectivity, auth and deserialization together.

require "ddx_interactions_api"

API_VERSION = ENV.fetch("DDX_API_VERSION", "1")

spec = Gem.loaded_specs["ddx_interactions_api"]

# Which build actually got installed.
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
  # The exception message is only the status line; the body says why.
  warn "\nauth/me failed: HTTP #{e.code}"
  warn e.response_body.to_s
  exit 1
end

puts "\nauth/me OK"
puts me.to_hash.inspect
