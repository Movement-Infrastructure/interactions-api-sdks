# Ddx.InteractionsApi.Api.AuthenticationDetailsApi

All URIs are relative to *https://api.movementinfrastructure.org*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**VversionAuthMeGet**](AuthenticationDetailsApi.md#vversionauthmeget) | **GET** /v{version}/auth/me | Get authentication context |

<a id="vversionauthmeget"></a>
# **VversionAuthMeGet**
> WhoAmIApiKeyDto VversionAuthMeGet (string version)

Get authentication context

Returns details about the authenticated API key including vendor, organization, committee, and state information.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using System.Net.Http;
using Ddx.InteractionsApi.Api;
using Ddx.InteractionsApi.Client;
using Ddx.InteractionsApi.Model;

namespace Example
{
    public class VversionAuthMeGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "https://api.movementinfrastructure.org";
            // Configure HTTP basic authorization: Basic
            config.Username = "YOUR_USERNAME";
            config.Password = "YOUR_PASSWORD";

            // create instances of HttpClient, HttpClientHandler to be reused later with different Api classes
            HttpClient httpClient = new HttpClient();
            HttpClientHandler httpClientHandler = new HttpClientHandler();
            var apiInstance = new AuthenticationDetailsApi(httpClient, config, httpClientHandler);
            var version = "\"1\"";  // string |  (default to "1")

            try
            {
                // Get authentication context
                WhoAmIApiKeyDto result = apiInstance.VversionAuthMeGet(version);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling AuthenticationDetailsApi.VversionAuthMeGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the VversionAuthMeGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get authentication context
    ApiResponse<WhoAmIApiKeyDto> response = apiInstance.VversionAuthMeGetWithHttpInfo(version);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling AuthenticationDetailsApi.VversionAuthMeGetWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** |  | [default to &quot;1&quot;] |

### Return type

[**WhoAmIApiKeyDto**](WhoAmIApiKeyDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved API key information |  -  |
| **401** | Unauthorized - invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

