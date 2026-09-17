using System.Net;
using System.Text;

namespace InteractionsApiSdkTests;

/// <summary>
/// Captures the outgoing request and returns a canned response, so the happy
/// path exercises real serialization, auth and URL building without a network.
/// </summary>
internal sealed class StubHttpMessageHandler : HttpMessageHandler
{
    private readonly string _responseBody;
    private readonly HttpStatusCode _statusCode;

    public StubHttpMessageHandler(string responseBody, HttpStatusCode statusCode = HttpStatusCode.OK)
    {
        _responseBody = responseBody;
        _statusCode = statusCode;
    }

    /// <summary>The request the client actually sent. Null until one is made.</summary>
    public HttpRequestMessage? LastRequest { get; private set; }

    /// <summary>The request body, read before the client disposes the stream.</summary>
    public string? LastRequestBody { get; private set; }

    protected override async Task<HttpResponseMessage> SendAsync(
        HttpRequestMessage request,
        CancellationToken cancellationToken)
    {
        LastRequest = request;

        // Read here, not from LastRequest afterwards: the content stream is
        // disposed once the client finishes with the request.
        if (request.Content is not null)
        {
            LastRequestBody = await request.Content.ReadAsStringAsync(cancellationToken);
        }

        return new HttpResponseMessage(_statusCode)
        {
            Content = new StringContent(_responseBody, Encoding.UTF8, "application/json"),
            RequestMessage = request,
        };
    }
}
