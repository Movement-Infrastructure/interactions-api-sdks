# \InteractionsAPI

All URIs are relative to *https://api.movementinfrastructure.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**VversionInteractionsExchangeStatusGet**](InteractionsAPI.md#VversionInteractionsExchangeStatusGet) | **Get** /v{version}/interactions/exchange-status | Get Exchange pipeline statuses by correlation or interaction ID
[**VversionInteractionsExchangeStatusRangeGet**](InteractionsAPI.md#VversionInteractionsExchangeStatusRangeGet) | **Get** /v{version}/interactions/exchange-status/range | Get Exchange pipeline statuses by date range
[**VversionInteractionsInteractionIdTransactionsGet**](InteractionsAPI.md#VversionInteractionsInteractionIdTransactionsGet) | **Get** /v{version}/interactions/{interactionId}/transactions | Get external API transactions by interactionId
[**VversionInteractionsPost**](InteractionsAPI.md#VversionInteractionsPost) | **Post** /v{version}/interactions | Post interactions data
[**VversionInteractionsTransactionsGet**](InteractionsAPI.md#VversionInteractionsTransactionsGet) | **Get** /v{version}/interactions/transactions | Get external API transaction logs by date range



## VversionInteractionsExchangeStatusGet

> ExchangeInteractionStatusDtoCursorPaginatedResponseDto VversionInteractionsExchangeStatusGet(ctx, version).CorrelationId(correlationId).InteractionId(interactionId).Cursor(cursor).Limit(limit).Execute()

Get Exchange pipeline statuses by correlation or interaction ID



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go"
)

func main() {
	version := "version_example" // string |  (default to "1")
	correlationId := "correlationId_example" // string | The correlation ID returned from the initial publish response. (optional)
	interactionId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | The interaction's unique identifier (GUID). (optional)
	cursor := "cursor_example" // string | Opaque pagination token from a previous response's nextCursor field. (optional)
	limit := int32(56) // int32 | Maximum number of results to return (default 100, max 1000). (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InteractionsAPI.VversionInteractionsExchangeStatusGet(context.Background(), version).CorrelationId(correlationId).InteractionId(interactionId).Cursor(cursor).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InteractionsAPI.VversionInteractionsExchangeStatusGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VversionInteractionsExchangeStatusGet`: ExchangeInteractionStatusDtoCursorPaginatedResponseDto
	fmt.Fprintf(os.Stdout, "Response from `InteractionsAPI.VversionInteractionsExchangeStatusGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**version** | **string** |  | [default to &quot;1&quot;]

### Other Parameters

Other parameters are passed through a pointer to a apiVversionInteractionsExchangeStatusGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **correlationId** | **string** | The correlation ID returned from the initial publish response. | 
 **interactionId** | **string** | The interaction&#39;s unique identifier (GUID). | 
 **cursor** | **string** | Opaque pagination token from a previous response&#39;s nextCursor field. | 
 **limit** | **int32** | Maximum number of results to return (default 100, max 1000). | 

### Return type

[**ExchangeInteractionStatusDtoCursorPaginatedResponseDto**](ExchangeInteractionStatusDtoCursorPaginatedResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VversionInteractionsExchangeStatusRangeGet

> ExchangeInteractionStatusDtoCursorPaginatedResponseDto VversionInteractionsExchangeStatusRangeGet(ctx, version).StartDate(startDate).EndDate(endDate).Cursor(cursor).Limit(limit).Execute()

Get Exchange pipeline statuses by date range



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go"
)

func main() {
	version := "version_example" // string |  (default to "1")
	startDate := time.Now() // time.Time | Beginning of date range (inclusive, UTC). (optional)
	endDate := time.Now() // time.Time | End of date range (inclusive, UTC). Defaults to current UTC time. (optional)
	cursor := "cursor_example" // string | Opaque pagination token from a previous response's nextCursor field. (optional)
	limit := int32(56) // int32 | Maximum number of results to return (default 100, max 1000). (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InteractionsAPI.VversionInteractionsExchangeStatusRangeGet(context.Background(), version).StartDate(startDate).EndDate(endDate).Cursor(cursor).Limit(limit).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InteractionsAPI.VversionInteractionsExchangeStatusRangeGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VversionInteractionsExchangeStatusRangeGet`: ExchangeInteractionStatusDtoCursorPaginatedResponseDto
	fmt.Fprintf(os.Stdout, "Response from `InteractionsAPI.VversionInteractionsExchangeStatusRangeGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**version** | **string** |  | [default to &quot;1&quot;]

### Other Parameters

Other parameters are passed through a pointer to a apiVversionInteractionsExchangeStatusRangeGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **startDate** | **time.Time** | Beginning of date range (inclusive, UTC). | 
 **endDate** | **time.Time** | End of date range (inclusive, UTC). Defaults to current UTC time. | 
 **cursor** | **string** | Opaque pagination token from a previous response&#39;s nextCursor field. | 
 **limit** | **int32** | Maximum number of results to return (default 100, max 1000). | 

### Return type

[**ExchangeInteractionStatusDtoCursorPaginatedResponseDto**](ExchangeInteractionStatusDtoCursorPaginatedResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VversionInteractionsInteractionIdTransactionsGet

> InteractionsExternalApiTransactionDtoGetResponseDto VversionInteractionsInteractionIdTransactionsGet(ctx, interactionId, version).ShowOnlyFailedTransactions(showOnlyFailedTransactions).Execute()

Get external API transactions by interactionId



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go"
)

func main() {
	interactionId := "38400000-8cf0-11bd-b23e-10b96e4ef00d" // string | ID of the interaction to retrieve records for.
	version := "version_example" // string |  (default to "1")
	showOnlyFailedTransactions := true // bool | When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. (optional) (default to true)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InteractionsAPI.VversionInteractionsInteractionIdTransactionsGet(context.Background(), interactionId, version).ShowOnlyFailedTransactions(showOnlyFailedTransactions).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InteractionsAPI.VversionInteractionsInteractionIdTransactionsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VversionInteractionsInteractionIdTransactionsGet`: InteractionsExternalApiTransactionDtoGetResponseDto
	fmt.Fprintf(os.Stdout, "Response from `InteractionsAPI.VversionInteractionsInteractionIdTransactionsGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**interactionId** | **string** | ID of the interaction to retrieve records for. | 
**version** | **string** |  | [default to &quot;1&quot;]

### Other Parameters

Other parameters are passed through a pointer to a apiVversionInteractionsInteractionIdTransactionsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


 **showOnlyFailedTransactions** | **bool** | When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. | [default to true]

### Return type

[**InteractionsExternalApiTransactionDtoGetResponseDto**](InteractionsExternalApiTransactionDtoGetResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VversionInteractionsPost

> InteractionsBatchResultDto VversionInteractionsPost(ctx, version).InteractionsDto(interactionsDto).Execute()

Post interactions data



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go"
)

func main() {
	version := "version_example" // string |  (default to "1")
	interactionsDto := *openapiclient.NewInteractionsDto() // InteractionsDto |  (optional)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InteractionsAPI.VversionInteractionsPost(context.Background(), version).InteractionsDto(interactionsDto).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InteractionsAPI.VversionInteractionsPost``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VversionInteractionsPost`: InteractionsBatchResultDto
	fmt.Fprintf(os.Stdout, "Response from `InteractionsAPI.VversionInteractionsPost`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**version** | **string** |  | [default to &quot;1&quot;]

### Other Parameters

Other parameters are passed through a pointer to a apiVversionInteractionsPostRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **interactionsDto** | [**InteractionsDto**](InteractionsDto.md) |  | 

### Return type

[**InteractionsBatchResultDto**](InteractionsBatchResultDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/*+json
- **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)


## VversionInteractionsTransactionsGet

> InteractionsExternalApiTransactionDtoGetResponseDto VversionInteractionsTransactionsGet(ctx, version).StartDate(startDate).EndDate(endDate).ShowOnlyFailedTransactions(showOnlyFailedTransactions).Execute()

Get external API transaction logs by date range



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
    "time"
	openapiclient "github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go"
)

func main() {
	version := "version_example" // string |  (default to "1")
	startDate := time.Now() // time.Time | Beginning of date range to show transactions for (inclusive). Must be provided in UTC, and be within 30 days of endDate. (optional)
	endDate := time.Now() // time.Time | End of date range to show transactions for (inclusive). Defaults to current date/time if not provided. Must be provided in UTC if specified,              and be within 30 days of startDate. (optional)
	showOnlyFailedTransactions := true // bool | When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. (optional) (default to true)

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.InteractionsAPI.VversionInteractionsTransactionsGet(context.Background(), version).StartDate(startDate).EndDate(endDate).ShowOnlyFailedTransactions(showOnlyFailedTransactions).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `InteractionsAPI.VversionInteractionsTransactionsGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VversionInteractionsTransactionsGet`: InteractionsExternalApiTransactionDtoGetResponseDto
	fmt.Fprintf(os.Stdout, "Response from `InteractionsAPI.VversionInteractionsTransactionsGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**version** | **string** |  | [default to &quot;1&quot;]

### Other Parameters

Other parameters are passed through a pointer to a apiVversionInteractionsTransactionsGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------

 **startDate** | **time.Time** | Beginning of date range to show transactions for (inclusive). Must be provided in UTC, and be within 30 days of endDate. | 
 **endDate** | **time.Time** | End of date range to show transactions for (inclusive). Defaults to current date/time if not provided. Must be provided in UTC if specified,              and be within 30 days of startDate. | 
 **showOnlyFailedTransactions** | **bool** | When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. | [default to true]

### Return type

[**InteractionsExternalApiTransactionDtoGetResponseDto**](InteractionsExternalApiTransactionDtoGetResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

