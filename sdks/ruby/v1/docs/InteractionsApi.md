# DdxInteractionsApi::InteractionsApi

All URIs are relative to *https://api.movementinfrastructure.org*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**vversion_interactions_exchange_status_get**](InteractionsApi.md#vversion_interactions_exchange_status_get) | **GET** /v{version}/interactions/exchange-status | Get Exchange pipeline statuses by correlation or interaction ID |
| [**vversion_interactions_exchange_status_range_get**](InteractionsApi.md#vversion_interactions_exchange_status_range_get) | **GET** /v{version}/interactions/exchange-status/range | Get Exchange pipeline statuses by date range |
| [**vversion_interactions_interaction_id_transactions_get**](InteractionsApi.md#vversion_interactions_interaction_id_transactions_get) | **GET** /v{version}/interactions/{interactionId}/transactions | Get external API transactions by interactionId |
| [**vversion_interactions_post**](InteractionsApi.md#vversion_interactions_post) | **POST** /v{version}/interactions | Post interactions data |
| [**vversion_interactions_transactions_get**](InteractionsApi.md#vversion_interactions_transactions_get) | **GET** /v{version}/interactions/transactions | Get external API transaction logs by date range |


## vversion_interactions_exchange_status_get

> <ExchangeInteractionStatusDtoCursorPaginatedResponseDto> vversion_interactions_exchange_status_get(version, opts)

Get Exchange pipeline statuses by correlation or interaction ID

Returns Exchange pipeline statuses filtered by either correlationId or interactionId.  Supports cursor-based pagination.

### Examples

```ruby
require 'time'
require 'ddx_interactions_api'
# setup authorization
DdxInteractionsApi.configure do |config|
  # Configure HTTP basic authorization: Basic
  config.username = 'YOUR USERNAME'
  config.password = 'YOUR PASSWORD'
end

api_instance = DdxInteractionsApi::InteractionsApi.new
version = 'version_example' # String | 
opts = {
  correlation_id: 'correlation_id_example', # String | The correlation ID returned from the initial publish response.
  interaction_id: '38400000-8cf0-11bd-b23e-10b96e4ef00d', # String | The interaction's unique identifier (GUID).
  cursor: 'cursor_example', # String | Opaque pagination token from a previous response's nextCursor field.
  limit: 56 # Integer | Maximum number of results to return (default 100, max 1000).
}

begin
  # Get Exchange pipeline statuses by correlation or interaction ID
  result = api_instance.vversion_interactions_exchange_status_get(version, opts)
  p result
rescue DdxInteractionsApi::ApiError => e
  puts "Error when calling InteractionsApi->vversion_interactions_exchange_status_get: #{e}"
end
```

#### Using the vversion_interactions_exchange_status_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ExchangeInteractionStatusDtoCursorPaginatedResponseDto>, Integer, Hash)> vversion_interactions_exchange_status_get_with_http_info(version, opts)

```ruby
begin
  # Get Exchange pipeline statuses by correlation or interaction ID
  data, status_code, headers = api_instance.vversion_interactions_exchange_status_get_with_http_info(version, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ExchangeInteractionStatusDtoCursorPaginatedResponseDto>
rescue DdxInteractionsApi::ApiError => e
  puts "Error when calling InteractionsApi->vversion_interactions_exchange_status_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **version** | **String** |  | [default to &#39;1&#39;] |
| **correlation_id** | **String** | The correlation ID returned from the initial publish response. | [optional] |
| **interaction_id** | **String** | The interaction&#39;s unique identifier (GUID). | [optional] |
| **cursor** | **String** | Opaque pagination token from a previous response&#39;s nextCursor field. | [optional] |
| **limit** | **Integer** | Maximum number of results to return (default 100, max 1000). | [optional] |

### Return type

[**ExchangeInteractionStatusDtoCursorPaginatedResponseDto**](ExchangeInteractionStatusDtoCursorPaginatedResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json


## vversion_interactions_exchange_status_range_get

> <ExchangeInteractionStatusDtoCursorPaginatedResponseDto> vversion_interactions_exchange_status_range_get(version, opts)

Get Exchange pipeline statuses by date range

Returns Exchange pipeline statuses for interactions published within the specified date range.  Supports cursor-based pagination. Maximum date range is 30 days.

### Examples

```ruby
require 'time'
require 'ddx_interactions_api'
# setup authorization
DdxInteractionsApi.configure do |config|
  # Configure HTTP basic authorization: Basic
  config.username = 'YOUR USERNAME'
  config.password = 'YOUR PASSWORD'
end

api_instance = DdxInteractionsApi::InteractionsApi.new
version = 'version_example' # String | 
opts = {
  start_date: Time.parse('2013-10-20T19:20:30+01:00'), # Time | Beginning of date range (inclusive, UTC).
  end_date: Time.parse('2013-10-20T19:20:30+01:00'), # Time | End of date range (inclusive, UTC). Defaults to current UTC time.
  cursor: 'cursor_example', # String | Opaque pagination token from a previous response's nextCursor field.
  limit: 56 # Integer | Maximum number of results to return (default 100, max 1000).
}

begin
  # Get Exchange pipeline statuses by date range
  result = api_instance.vversion_interactions_exchange_status_range_get(version, opts)
  p result
rescue DdxInteractionsApi::ApiError => e
  puts "Error when calling InteractionsApi->vversion_interactions_exchange_status_range_get: #{e}"
end
```

#### Using the vversion_interactions_exchange_status_range_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ExchangeInteractionStatusDtoCursorPaginatedResponseDto>, Integer, Hash)> vversion_interactions_exchange_status_range_get_with_http_info(version, opts)

```ruby
begin
  # Get Exchange pipeline statuses by date range
  data, status_code, headers = api_instance.vversion_interactions_exchange_status_range_get_with_http_info(version, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ExchangeInteractionStatusDtoCursorPaginatedResponseDto>
rescue DdxInteractionsApi::ApiError => e
  puts "Error when calling InteractionsApi->vversion_interactions_exchange_status_range_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **version** | **String** |  | [default to &#39;1&#39;] |
| **start_date** | **Time** | Beginning of date range (inclusive, UTC). | [optional] |
| **end_date** | **Time** | End of date range (inclusive, UTC). Defaults to current UTC time. | [optional] |
| **cursor** | **String** | Opaque pagination token from a previous response&#39;s nextCursor field. | [optional] |
| **limit** | **Integer** | Maximum number of results to return (default 100, max 1000). | [optional] |

### Return type

[**ExchangeInteractionStatusDtoCursorPaginatedResponseDto**](ExchangeInteractionStatusDtoCursorPaginatedResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json


## vversion_interactions_interaction_id_transactions_get

> <InteractionsExternalApiTransactionDtoGetResponseDto> vversion_interactions_interaction_id_transactions_get(interaction_id, version, opts)

Get external API transactions by interactionId

Get all external API transaction records for the specified interaction.

### Examples

```ruby
require 'time'
require 'ddx_interactions_api'
# setup authorization
DdxInteractionsApi.configure do |config|
  # Configure HTTP basic authorization: Basic
  config.username = 'YOUR USERNAME'
  config.password = 'YOUR PASSWORD'
end

api_instance = DdxInteractionsApi::InteractionsApi.new
interaction_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | ID of the interaction to retrieve records for.
version = 'version_example' # String | 
opts = {
  show_only_failed_transactions: true # Boolean | When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default.
}

begin
  # Get external API transactions by interactionId
  result = api_instance.vversion_interactions_interaction_id_transactions_get(interaction_id, version, opts)
  p result
rescue DdxInteractionsApi::ApiError => e
  puts "Error when calling InteractionsApi->vversion_interactions_interaction_id_transactions_get: #{e}"
end
```

#### Using the vversion_interactions_interaction_id_transactions_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<InteractionsExternalApiTransactionDtoGetResponseDto>, Integer, Hash)> vversion_interactions_interaction_id_transactions_get_with_http_info(interaction_id, version, opts)

```ruby
begin
  # Get external API transactions by interactionId
  data, status_code, headers = api_instance.vversion_interactions_interaction_id_transactions_get_with_http_info(interaction_id, version, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <InteractionsExternalApiTransactionDtoGetResponseDto>
rescue DdxInteractionsApi::ApiError => e
  puts "Error when calling InteractionsApi->vversion_interactions_interaction_id_transactions_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **interaction_id** | **String** | ID of the interaction to retrieve records for. |  |
| **version** | **String** |  | [default to &#39;1&#39;] |
| **show_only_failed_transactions** | **Boolean** | When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. | [optional][default to true] |

### Return type

[**InteractionsExternalApiTransactionDtoGetResponseDto**](InteractionsExternalApiTransactionDtoGetResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json


## vversion_interactions_post

> <InteractionsBatchResultDto> vversion_interactions_post(version, opts)

Post interactions data

This endpoint is used to post interactions data to the Interactions API that will be published to Pub/Sub.  A maximum of 100 interactions can be submitted per request.

### Examples

```ruby
require 'time'
require 'ddx_interactions_api'
# setup authorization
DdxInteractionsApi.configure do |config|
  # Configure HTTP basic authorization: Basic
  config.username = 'YOUR USERNAME'
  config.password = 'YOUR PASSWORD'
end

api_instance = DdxInteractionsApi::InteractionsApi.new
version = 'version_example' # String | 
opts = {
  interactions_dto: DdxInteractionsApi::InteractionsDto.new # InteractionsDto | 
}

begin
  # Post interactions data
  result = api_instance.vversion_interactions_post(version, opts)
  p result
rescue DdxInteractionsApi::ApiError => e
  puts "Error when calling InteractionsApi->vversion_interactions_post: #{e}"
end
```

#### Using the vversion_interactions_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<InteractionsBatchResultDto>, Integer, Hash)> vversion_interactions_post_with_http_info(version, opts)

```ruby
begin
  # Post interactions data
  data, status_code, headers = api_instance.vversion_interactions_post_with_http_info(version, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <InteractionsBatchResultDto>
rescue DdxInteractionsApi::ApiError => e
  puts "Error when calling InteractionsApi->vversion_interactions_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **version** | **String** |  | [default to &#39;1&#39;] |
| **interactions_dto** | [**InteractionsDto**](InteractionsDto.md) |  | [optional] |

### Return type

[**InteractionsBatchResultDto**](InteractionsBatchResultDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/*+json
- **Accept**: text/plain, application/json, text/json


## vversion_interactions_transactions_get

> <InteractionsExternalApiTransactionDtoGetResponseDto> vversion_interactions_transactions_get(version, opts)

Get external API transaction logs by date range

Get all external API transaction records within the date range specified, for a maximum of up to a 30 day span.

### Examples

```ruby
require 'time'
require 'ddx_interactions_api'
# setup authorization
DdxInteractionsApi.configure do |config|
  # Configure HTTP basic authorization: Basic
  config.username = 'YOUR USERNAME'
  config.password = 'YOUR PASSWORD'
end

api_instance = DdxInteractionsApi::InteractionsApi.new
version = 'version_example' # String | 
opts = {
  start_date: Time.parse('2013-10-20T19:20:30+01:00'), # Time | Beginning of date range to show transactions for (inclusive). Must be provided in UTC, and be within 30 days of endDate.
  end_date: Time.parse('2013-10-20T19:20:30+01:00'), # Time | End of date range to show transactions for (inclusive). Defaults to current date/time if not provided. Must be provided in UTC if specified,              and be within 30 days of startDate.
  show_only_failed_transactions: true # Boolean | When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default.
}

begin
  # Get external API transaction logs by date range
  result = api_instance.vversion_interactions_transactions_get(version, opts)
  p result
rescue DdxInteractionsApi::ApiError => e
  puts "Error when calling InteractionsApi->vversion_interactions_transactions_get: #{e}"
end
```

#### Using the vversion_interactions_transactions_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<InteractionsExternalApiTransactionDtoGetResponseDto>, Integer, Hash)> vversion_interactions_transactions_get_with_http_info(version, opts)

```ruby
begin
  # Get external API transaction logs by date range
  data, status_code, headers = api_instance.vversion_interactions_transactions_get_with_http_info(version, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <InteractionsExternalApiTransactionDtoGetResponseDto>
rescue DdxInteractionsApi::ApiError => e
  puts "Error when calling InteractionsApi->vversion_interactions_transactions_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **version** | **String** |  | [default to &#39;1&#39;] |
| **start_date** | **Time** | Beginning of date range to show transactions for (inclusive). Must be provided in UTC, and be within 30 days of endDate. | [optional] |
| **end_date** | **Time** | End of date range to show transactions for (inclusive). Defaults to current date/time if not provided. Must be provided in UTC if specified,              and be within 30 days of startDate. | [optional] |
| **show_only_failed_transactions** | **Boolean** | When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. | [optional][default to true] |

### Return type

[**InteractionsExternalApiTransactionDtoGetResponseDto**](InteractionsExternalApiTransactionDtoGetResponseDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

