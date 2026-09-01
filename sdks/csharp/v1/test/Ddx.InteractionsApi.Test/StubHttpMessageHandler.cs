using System.Net;
using System.Text;

namespace InteractionsApiSdkTests;

/// <summary>
/// Captures the outgoing request and returns a canned response, so the happy
/// path exercises the client's real serialization, auth and URL building
/// without a network or a mocking dependency.
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

    /// <summary>The request body as a string, read before the client disposes it.</summary>
    public string? LastRequestBody { get; private set; }

    protected override async Task<HttpResponseMessage> SendAsync(
        HttpRequestMessage request,
        CancellationToken cancellationToken)
    {
        LastRequest = request;

        // Read the body here rather than from LastRequest afterwards: the
        // content stream is disposed once the client finishes with the request.
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
