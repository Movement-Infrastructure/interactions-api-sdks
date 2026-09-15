# POST /v1/interactions against a stubbed server.
#
# The OpenAPI spec sets no operationId for these endpoints, so the generator
# derives `vversion_interactions_post` from the path and verb. `version` is a
# required positional argument with no default, which is why the path resolves
# to /v1/interactions only when the caller passes "1".

require "spec_helper"
require "webmock/rspec"

API_VERSION = "1"
HOST = "localhost:4010"

# Minimal request the API accepts.
REQUEST_BODY = {
  interactions: [
    {
      stateCode: "CA",
      attemptDateTime: "2026-07-30T10:00:00Z",
      method: "phone_call",
      committee: [{ type: "Matchbook", id: "1" }],
      vendorSource: "Matchbook",
      outcome: "successful_contact",
      person: [{ type: "Matchbook", id: "1" }]
    }
  ]
}.freeze

MOCK_RESPONSE = {
  correlationId: "test-correlation-123",
  totalInteractions: 1,
  acceptedInteractions: {
    count: 1,
    data: [{ interactionId: "11111111-1111-1111-1111-111111111111", index: 0 }]
  },
  rejectedInteractions: { count: 0, data: [] }
}.freeze

RSpec.describe DdxInteractionsApi::InteractionsApi do
  let(:client) do
    config = DdxInteractionsApi::Configuration.new
    config.scheme = "http"
    config.host = HOST
    # HTTP basic auth, API key in the password field, empty username. The stub
    # ignores it, but setting credentials exercises the client's auth path.
    config.username = ""
    config.password = "test"
    DdxInteractionsApi::ApiClient.new(config)
  end

  it "posts interactions and deserializes the batch result" do
    stub = stub_request(:post, "http://#{HOST}/v#{API_VERSION}/interactions")
           .to_return(
             status: 200,
             body: MOCK_RESPONSE.to_json,
             headers: { "Content-Type" => "application/json" }
           )

    body = DdxInteractionsApi::InteractionsDto.build_from_hash(REQUEST_BODY)
    result = described_class.new(client).vversion_interactions_post(
      API_VERSION, interactions_dto: body
    )

    expect(stub).to have_been_requested
    expect(result).to be_a(DdxInteractionsApi::InteractionsBatchResultDto)
    expect(result.total_interactions).to eq(1)
    expect(result.correlation_id).to eq("test-correlation-123")
    expect(result.accepted_interactions.count).to eq(1)
  end

  it "resolves the templated path to /v1/ rather than a literal /v{version}/" do
    stub_request(:post, %r{/interactions\z}).to_return(
      status: 200,
      body: MOCK_RESPONSE.to_json,
      headers: { "Content-Type" => "application/json" }
    )

    body = DdxInteractionsApi::InteractionsDto.build_from_hash(REQUEST_BODY)
    described_class.new(client).vversion_interactions_post(API_VERSION, interactions_dto: body)

    expect(a_request(:post, "http://#{HOST}/v1/interactions")).to have_been_made
    expect(a_request(:post, %r{/v\{version\}/})).not_to have_been_made
  end

  it "sends the API key as basic auth with an empty username" do
    stub_request(:post, %r{/interactions\z}).to_return(
      status: 200,
      body: MOCK_RESPONSE.to_json,
      headers: { "Content-Type" => "application/json" }
    )

    body = DdxInteractionsApi::InteractionsDto.build_from_hash(REQUEST_BODY)
    described_class.new(client).vversion_interactions_post(API_VERSION, interactions_dto: body)

    expect(
      a_request(:post, %r{/interactions\z}).with(basic_auth: ["", "test"])
    ).to have_been_made
  end
end
