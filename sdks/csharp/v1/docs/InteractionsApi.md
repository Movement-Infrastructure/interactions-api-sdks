# Ddx.InteractionsApi.Api.InteractionsApi

All URIs are relative to *https://api.movementinfrastructure.org*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**VversionInteractionsExchangeStatusGet**](InteractionsApi.md#vversioninteractionsexchangestatusget) | **GET** /v{version}/interactions/exchange-status | Get Exchange pipeline statuses by correlation or interaction ID |
| [**VversionInteractionsExchangeStatusRangeGet**](InteractionsApi.md#vversioninteractionsexchangestatusrangeget) | **GET** /v{version}/interactions/exchange-status/range | Get Exchange pipeline statuses by date range |
| [**VversionInteractionsInteractionIdTransactionsGet**](InteractionsApi.md#vversioninteractionsinteractionidtransactionsget) | **GET** /v{version}/interactions/{interactionId}/transactions | Get external API transactions by interactionId |
| [**VversionInteractionsPost**](InteractionsApi.md#vversioninteractionspost) | **POST** /v{version}/interactions | Post interactions data |
| [**VversionInteractionsTransactionsGet**](InteractionsApi.md#vversioninteractionstransactionsget) | **GET** /v{version}/interactions/transactions | Get external API transaction logs by date range |

<a id="vversioninteractionsexchangestatusget"></a>
# **VversionInteractionsExchangeStatusGet**
> ExchangeInteractionStatusDtoCursorPaginatedResponseDto VversionInteractionsExchangeStatusGet (string version, string? correlationId = null, Guid? interactionId = null, string? cursor = null, int? limit = null)

Get Exchange pipeline statuses by correlation or interaction ID

Returns Exchange pipeline statuses filtered by either correlationId or interactionId.  Supports cursor-based pagination.

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
    public class VversionInteractionsExchangeStatusGetExample
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
            var apiInstance = new InteractionsApi(httpClient, config, httpClientHandler);
            var version = "\"1\"";  // string |  (default to "1")
            var correlationId = "correlationId_example";  // string? | The correlation ID returned from the initial publish response. (optional) 
            var interactionId = "interactionId_example";  // Guid? | The interaction's unique identifier (GUID). (optional) 
            var cursor = "cursor_example";  // string? | Opaque pagination token from a previous response's nextCursor field. (optional) 
            var limit = 56;  // int? | Maximum number of results to return (default 100, max 1000). (optional) 

            try
            {
                // Get Exchange pipeline statuses by correlation or interaction ID
                ExchangeInteractionStatusDtoCursorPaginatedResponseDto result = apiInstance.VversionInteractionsExchangeStatusGet(version, correlationId, interactionId, cursor, limit);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling InteractionsApi.VversionInteractionsExchangeStatusGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the VversionInteractionsExchangeStatusGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get Exchange pipeline statuses by correlation or interaction ID
    ApiResponse<ExchangeInteractionStatusDtoCursorPaginatedResponseDto> response = apiInstance.VversionInteractionsExchangeStatusGetWithHttpInfo(version, correlationId, interactionId, cursor, limit);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling InteractionsApi.VversionInteractionsExchangeStatusGetWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** |  | [default to &quot;1&quot;] |
| **correlationId** | **string?** | The correlation ID returned from the initial publish response. | [optional]  |
| **interactionId** | **Guid?** | The interaction&#39;s unique identifier (GUID). | [optional]  |
| **cursor** | **string?** | Opaque pagination token from a previous response&#39;s nextCursor field. | [optional]  |
| **limit** | **int?** | Maximum number of results to return (default 100, max 1000). | [optional]  |

### Return type

[**ExchangeInteractionStatusDtoCursorPaginatedResponseDto**](ExchangeInteractionStatusDtoCursorPaginatedResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated list of Exchange statuses |  -  |
| **400** | Invalid or ambiguous filter parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="vversioninteractionsexchangestatusrangeget"></a>
# **VversionInteractionsExchangeStatusRangeGet**
> ExchangeInteractionStatusDtoCursorPaginatedResponseDto VversionInteractionsExchangeStatusRangeGet (string version, DateTime? startDate = null, DateTime? endDate = null, string? cursor = null, int? limit = null)

Get Exchange pipeline statuses by date range

Returns Exchange pipeline statuses for interactions published within the specified date range.  Supports cursor-based pagination. Maximum date range is 30 days.

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
    public class VversionInteractionsExchangeStatusRangeGetExample
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
            var apiInstance = new InteractionsApi(httpClient, config, httpClientHandler);
            var version = "\"1\"";  // string |  (default to "1")
            var startDate = DateTime.Parse("2013-10-20T19:20:30+01:00");  // DateTime? | Beginning of date range (inclusive, UTC). (optional) 
            var endDate = DateTime.Parse("2013-10-20T19:20:30+01:00");  // DateTime? | End of date range (inclusive, UTC). Defaults to current UTC time. (optional) 
            var cursor = "cursor_example";  // string? | Opaque pagination token from a previous response's nextCursor field. (optional) 
            var limit = 56;  // int? | Maximum number of results to return (default 100, max 1000). (optional) 

            try
            {
                // Get Exchange pipeline statuses by date range
                ExchangeInteractionStatusDtoCursorPaginatedResponseDto result = apiInstance.VversionInteractionsExchangeStatusRangeGet(version, startDate, endDate, cursor, limit);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling InteractionsApi.VversionInteractionsExchangeStatusRangeGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the VversionInteractionsExchangeStatusRangeGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get Exchange pipeline statuses by date range
    ApiResponse<ExchangeInteractionStatusDtoCursorPaginatedResponseDto> response = apiInstance.VversionInteractionsExchangeStatusRangeGetWithHttpInfo(version, startDate, endDate, cursor, limit);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling InteractionsApi.VversionInteractionsExchangeStatusRangeGetWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** |  | [default to &quot;1&quot;] |
| **startDate** | **DateTime?** | Beginning of date range (inclusive, UTC). | [optional]  |
| **endDate** | **DateTime?** | End of date range (inclusive, UTC). Defaults to current UTC time. | [optional]  |
| **cursor** | **string?** | Opaque pagination token from a previous response&#39;s nextCursor field. | [optional]  |
| **limit** | **int?** | Maximum number of results to return (default 100, max 1000). | [optional]  |

### Return type

[**ExchangeInteractionStatusDtoCursorPaginatedResponseDto**](ExchangeInteractionStatusDtoCursorPaginatedResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Paginated list of Exchange statuses |  -  |
| **400** | Invalid date range, limit, or cursor |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="vversioninteractionsinteractionidtransactionsget"></a>
# **VversionInteractionsInteractionIdTransactionsGet**
> InteractionsExternalApiTransactionDtoGetResponseDto VversionInteractionsInteractionIdTransactionsGet (Guid interactionId, string version, bool? showOnlyFailedTransactions = null)

Get external API transactions by interactionId

Get all external API transaction records for the specified interaction.

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
    public class VversionInteractionsInteractionIdTransactionsGetExample
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
            var apiInstance = new InteractionsApi(httpClient, config, httpClientHandler);
            var interactionId = "interactionId_example";  // Guid | ID of the interaction to retrieve records for.
            var version = "\"1\"";  // string |  (default to "1")
            var showOnlyFailedTransactions = true;  // bool? | When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. (optional)  (default to true)

            try
            {
                // Get external API transactions by interactionId
                InteractionsExternalApiTransactionDtoGetResponseDto result = apiInstance.VversionInteractionsInteractionIdTransactionsGet(interactionId, version, showOnlyFailedTransactions);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling InteractionsApi.VversionInteractionsInteractionIdTransactionsGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the VversionInteractionsInteractionIdTransactionsGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get external API transactions by interactionId
    ApiResponse<InteractionsExternalApiTransactionDtoGetResponseDto> response = apiInstance.VversionInteractionsInteractionIdTransactionsGetWithHttpInfo(interactionId, version, showOnlyFailedTransactions);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling InteractionsApi.VversionInteractionsInteractionIdTransactionsGetWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **interactionId** | **Guid** | ID of the interaction to retrieve records for. |  |
| **version** | **string** |  | [default to &quot;1&quot;] |
| **showOnlyFailedTransactions** | **bool?** | When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. | [optional] [default to true] |

### Return type

[**InteractionsExternalApiTransactionDtoGetResponseDto**](InteractionsExternalApiTransactionDtoGetResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="vversioninteractionspost"></a>
# **VversionInteractionsPost**
> InteractionsBatchResultDto VversionInteractionsPost (string version, InteractionsDto? interactionsDto = null)

Post interactions data

This endpoint is used to post interactions data to the Interactions API that will be published to Pub/Sub.  A maximum of 100 interactions can be submitted per request.

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
    public class VversionInteractionsPostExample
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
            var apiInstance = new InteractionsApi(httpClient, config, httpClientHandler);
            var version = "\"1\"";  // string |  (default to "1")
            var interactionsDto = new InteractionsDto?(); // InteractionsDto? |  (optional) 

            try
            {
                // Post interactions data
                InteractionsBatchResultDto result = apiInstance.VversionInteractionsPost(version, interactionsDto);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling InteractionsApi.VversionInteractionsPost: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the VversionInteractionsPostWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Post interactions data
    ApiResponse<InteractionsBatchResultDto> response = apiInstance.VversionInteractionsPostWithHttpInfo(version, interactionsDto);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling InteractionsApi.VversionInteractionsPostWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** |  | [default to &quot;1&quot;] |
| **interactionsDto** | [**InteractionsDto?**](InteractionsDto?.md) |  | [optional]  |

### Return type

[**InteractionsBatchResultDto**](InteractionsBatchResultDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All interactions were valid and successfully published |  -  |
| **207** | Some interactions were rejected; see response body for details |  -  |
| **400** | Invalid interactions data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="vversioninteractionstransactionsget"></a>
# **VversionInteractionsTransactionsGet**
> InteractionsExternalApiTransactionDtoGetResponseDto VversionInteractionsTransactionsGet (string version, DateTime? startDate = null, DateTime? endDate = null, bool? showOnlyFailedTransactions = null)

Get external API transaction logs by date range

Get all external API transaction records within the date range specified, for a maximum of up to a 30 day span.

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
    public class VversionInteractionsTransactionsGetExample
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
            var apiInstance = new InteractionsApi(httpClient, config, httpClientHandler);
            var version = "\"1\"";  // string |  (default to "1")
            var startDate = DateTime.Parse("2013-10-20T19:20:30+01:00");  // DateTime? | Beginning of date range to show transactions for (inclusive). Must be provided in UTC, and be within 30 days of endDate. (optional) 
            var endDate = DateTime.Parse("2013-10-20T19:20:30+01:00");  // DateTime? | End of date range to show transactions for (inclusive). Defaults to current date/time if not provided. Must be provided in UTC if specified,              and be within 30 days of startDate. (optional) 
            var showOnlyFailedTransactions = true;  // bool? | When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. (optional)  (default to true)

            try
            {
                // Get external API transaction logs by date range
                InteractionsExternalApiTransactionDtoGetResponseDto result = apiInstance.VversionInteractionsTransactionsGet(version, startDate, endDate, showOnlyFailedTransactions);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling InteractionsApi.VversionInteractionsTransactionsGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the VversionInteractionsTransactionsGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get external API transaction logs by date range
    ApiResponse<InteractionsExternalApiTransactionDtoGetResponseDto> response = apiInstance.VversionInteractionsTransactionsGetWithHttpInfo(version, startDate, endDate, showOnlyFailedTransactions);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling InteractionsApi.VversionInteractionsTransactionsGetWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **version** | **string** |  | [default to &quot;1&quot;] |
| **startDate** | **DateTime?** | Beginning of date range to show transactions for (inclusive). Must be provided in UTC, and be within 30 days of endDate. | [optional]  |
| **endDate** | **DateTime?** | End of date range to show transactions for (inclusive). Defaults to current date/time if not provided. Must be provided in UTC if specified,              and be within 30 days of startDate. | [optional]  |
| **showOnlyFailedTransactions** | **bool?** | When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. | [optional] [default to true] |

### Return type

[**InteractionsExternalApiTransactionDtoGetResponseDto**](InteractionsExternalApiTransactionDtoGetResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

