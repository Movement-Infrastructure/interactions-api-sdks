using System.Text;
using System.Text.Json;
using Ddx.InteractionsApi.Api;
using Ddx.InteractionsApi.Client;
using Ddx.InteractionsApi.Model;
using Xunit;

namespace InteractionsApiSdkTests;

/// <summary>
/// POST /v1/interactions against a stubbed transport.
///
/// The OpenAPI spec sets no operationId for these endpoints, so the generator
/// derives VversionInteractionsPost from the path and verb. `version` is a
/// required argument with no default, which is why the path resolves to
/// /v1/interactions only when the caller passes "1".
/// </summary>
public class PublishInteractionsTest
{
    private const string Host = "http://localhost:4010";
    private const string ApiVersion = "1";
    private const string ApiKey = "test";

    private const string MockResponse = """
        {
          "correlationId": "test-correlation-123",
          "totalInteractions": 1,
          "acceptedInteractions": {
            "count": 1,
            "data": [{ "interactionId": "11111111-1111-1111-1111-111111111111", "index": 0 }]
          },
          "rejectedInteractions": { "count": 0, "data": [] }
        }
        """;

    /// <summary>Minimal request the API accepts.</summary>
    private static InteractionsDto RequestBody() => new(
        interactions: new List<InteractionDto>
        {
            new(
                stateCode: "CA",
                attemptDateTime: new DateTime(2026, 7, 30, 10, 0, 0, DateTimeKind.Utc),
                method: ContactMethod.PhoneCall,
                committee: new List<CommitteeDetails> { new(type: "Matchbook", id: "1") },
                vendorSource: "Matchbook",
                outcome: Outcome.SuccessfulContact),
        });

    private static (InteractionsApi Api, StubHttpMessageHandler Handler) Client()
    {
        var handler = new StubHttpMessageHandler(MockResponse);
        var config = new Configuration
        {
            BasePath = Host,
            // HTTP basic auth, API key in the password field, empty username.
            // The stub ignores it, but this exercises the client's auth path.
            Username = "",
            Password = ApiKey,
        };

        return (new InteractionsApi(new HttpClient(handler), config), handler);
    }

    [Fact]
    public void PostsInteractionsAndDeserializesTheBatchResult()
    {
        var (api, _) = Client();

        var result = api.VversionInteractionsPost(ApiVersion, RequestBody());

        Assert.Equal(1, result.TotalInteractions);
        Assert.Equal("test-correlation-123", result.CorrelationId);
        Assert.Equal(1, result.AcceptedInteractions.Count);
    }

    [Fact]
    public void ResolvesTheTemplatedPathRatherThanALiteralVersionPlaceholder()
    {
        var (api, handler) = Client();

        api.VversionInteractionsPost(ApiVersion, RequestBody());

        Assert.Equal($"{Host}/v1/interactions", handler.LastRequest!.RequestUri!.ToString());
        Assert.DoesNotContain("%7Bversion%7D", handler.LastRequest.RequestUri.ToString());
    }

    [Fact]
    public void SendsTheApiKeyAsBasicAuthWithAnEmptyUsername()
    {
        var (api, handler) = Client();

        api.VversionInteractionsPost(ApiVersion, RequestBody());

        var expected = Convert.ToBase64String(Encoding.UTF8.GetBytes($":{ApiKey}"));
        var authorization = handler.LastRequest!.Headers.Authorization;

        Assert.NotNull(authorization);
        Assert.Equal("Basic", authorization!.Scheme);
        Assert.Equal(expected, authorization.Parameter);
    }

    [Fact]
    public void SerializesTheInteractionBodyTheApiExpects()
    {
        var (api, handler) = Client();

        api.VversionInteractionsPost(ApiVersion, RequestBody());

        using var document = JsonDocument.Parse(handler.LastRequestBody!);
        var interaction = document.RootElement.GetProperty("interactions")[0];

        Assert.Equal("CA", interaction.GetProperty("stateCode").GetString());
        Assert.Equal("phone_call", interaction.GetProperty("method").GetString());
        Assert.Equal("successful_contact", interaction.GetProperty("outcome").GetString());
    }
}
