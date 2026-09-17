# InteractionsApi

All URIs are relative to *https://api.movementinfrastructure.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vversionInteractionsExchangeStatusGet**](InteractionsApi.md#vversionInteractionsExchangeStatusGet) | **GET** /v{version}/interactions/exchange-status | Get Exchange pipeline statuses by correlation or interaction ID |
| [**vversionInteractionsExchangeStatusRangeGet**](InteractionsApi.md#vversionInteractionsExchangeStatusRangeGet) | **GET** /v{version}/interactions/exchange-status/range | Get Exchange pipeline statuses by date range |
| [**vversionInteractionsInteractionIdTransactionsGet**](InteractionsApi.md#vversionInteractionsInteractionIdTransactionsGet) | **GET** /v{version}/interactions/{interactionId}/transactions | Get external API transactions by interactionId |
| [**vversionInteractionsPost**](InteractionsApi.md#vversionInteractionsPost) | **POST** /v{version}/interactions | Post interactions data |
| [**vversionInteractionsTransactionsGet**](InteractionsApi.md#vversionInteractionsTransactionsGet) | **GET** /v{version}/interactions/transactions | Get external API transaction logs by date range |


<a name="vversionInteractionsExchangeStatusGet"></a>
# **vversionInteractionsExchangeStatusGet**
> ExchangeInteractionStatusDtoCursorPaginatedResponseDto vversionInteractionsExchangeStatusGet(version, correlationId, interactionId, cursor, limit)

Get Exchange pipeline statuses by correlation or interaction ID

    Returns Exchange pipeline statuses filtered by either correlationId or interactionId.  Supports cursor-based pagination.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **version** | **String**|  | [default to 1] |
| **correlationId** | **String**| The correlation ID returned from the initial publish response. | [optional] [default to null] |
| **interactionId** | **UUID**| The interaction&#39;s unique identifier (GUID). | [optional] [default to null] |
| **cursor** | **String**| Opaque pagination token from a previous response&#39;s nextCursor field. | [optional] [default to null] |
| **limit** | **Integer**| Maximum number of results to return (default 100, max 1000). | [optional] [default to null] |

### Return type

[**ExchangeInteractionStatusDtoCursorPaginatedResponseDto**](../Models/ExchangeInteractionStatusDtoCursorPaginatedResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

<a name="vversionInteractionsExchangeStatusRangeGet"></a>
# **vversionInteractionsExchangeStatusRangeGet**
> ExchangeInteractionStatusDtoCursorPaginatedResponseDto vversionInteractionsExchangeStatusRangeGet(version, startDate, endDate, cursor, limit)

Get Exchange pipeline statuses by date range

    Returns Exchange pipeline statuses for interactions published within the specified date range.  Supports cursor-based pagination. Maximum date range is 30 days.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **version** | **String**|  | [default to 1] |
| **startDate** | **Date**| Beginning of date range (inclusive, UTC). | [optional] [default to null] |
| **endDate** | **Date**| End of date range (inclusive, UTC). Defaults to current UTC time. | [optional] [default to null] |
| **cursor** | **String**| Opaque pagination token from a previous response&#39;s nextCursor field. | [optional] [default to null] |
| **limit** | **Integer**| Maximum number of results to return (default 100, max 1000). | [optional] [default to null] |

### Return type

[**ExchangeInteractionStatusDtoCursorPaginatedResponseDto**](../Models/ExchangeInteractionStatusDtoCursorPaginatedResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

<a name="vversionInteractionsInteractionIdTransactionsGet"></a>
# **vversionInteractionsInteractionIdTransactionsGet**
> InteractionsExternalApiTransactionDtoGetResponseDto vversionInteractionsInteractionIdTransactionsGet(interactionId, version, showOnlyFailedTransactions)

Get external API transactions by interactionId

    Get all external API transaction records for the specified interaction.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **interactionId** | **UUID**| ID of the interaction to retrieve records for. | [default to null] |
| **version** | **String**|  | [default to 1] |
| **showOnlyFailedTransactions** | **Boolean**| When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. | [optional] [default to true] |

### Return type

[**InteractionsExternalApiTransactionDtoGetResponseDto**](../Models/InteractionsExternalApiTransactionDtoGetResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

<a name="vversionInteractionsPost"></a>
# **vversionInteractionsPost**
> InteractionsBatchResultDto vversionInteractionsPost(version, InteractionsDto)

Post interactions data

    This endpoint is used to post interactions data to the Interactions API that will be published to Pub/Sub.  A maximum of 100 interactions can be submitted per request.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **version** | **String**|  | [default to 1] |
| **InteractionsDto** | [**InteractionsDto**](../Models/InteractionsDto.md)|  | [optional] |

### Return type

[**InteractionsBatchResultDto**](../Models/InteractionsBatchResultDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/*+json
- **Accept**: text/plain, application/json, text/json

<a name="vversionInteractionsTransactionsGet"></a>
# **vversionInteractionsTransactionsGet**
> InteractionsExternalApiTransactionDtoGetResponseDto vversionInteractionsTransactionsGet(version, startDate, endDate, showOnlyFailedTransactions)

Get external API transaction logs by date range

    Get all external API transaction records within the date range specified, for a maximum of up to a 30 day span.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **version** | **String**|  | [default to 1] |
| **startDate** | **Date**| Beginning of date range to show transactions for (inclusive). Must be provided in UTC, and be within 30 days of endDate. | [optional] [default to null] |
| **endDate** | **Date**| End of date range to show transactions for (inclusive). Defaults to current date/time if not provided. Must be provided in UTC if specified,              and be within 30 days of startDate. | [optional] [default to null] |
| **showOnlyFailedTransactions** | **Boolean**| When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. | [optional] [default to true] |

### Return type

[**InteractionsExternalApiTransactionDtoGetResponseDto**](../Models/InteractionsExternalApiTransactionDtoGetResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

