# Proves the generated gem loads and exposes the surface consumers depend on.
# Cheap to run and catches a broken generation before the happy-path spec has to
# stand up a mock server.

require "spec_helper"

RSpec.describe "generated gem" do
  it "loads and defines its module" do
    expect(defined?(DdxInteractionsApi)).to eq("constant")
  end

  it "exposes the client, configuration and API classes" do
    expect(DdxInteractionsApi::ApiClient).to be_a(Class)
    expect(DdxInteractionsApi::Configuration).to be_a(Class)
    expect(DdxInteractionsApi::InteractionsApi).to be_a(Class)
    expect(DdxInteractionsApi::AuthenticationDetailsApi).to be_a(Class)
  end

  it "exposes the models the happy path round-trips" do
    expect(DdxInteractionsApi::InteractionsDto).to be_a(Class)
    expect(DdxInteractionsApi::InteractionsBatchResultDto).to be_a(Class)
    expect(DdxInteractionsApi::WhoAmIApiKeyDto).to be_a(Class)
  end

  it "reports the version the generator config set" do
    expect(DdxInteractionsApi::VERSION).to match(/\A\d+\.\d+\.\d+\z/)
  end

  it "defaults to the production host" do
    expect(DdxInteractionsApi::Configuration.default.host).to eq("api.movementinfrastructure.org")
  end
end
