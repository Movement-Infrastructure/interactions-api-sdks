# ddx_interactions_api.InteractionsApi

All URIs are relative to *https://api.movementinfrastructure.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vversion_interactions_exchange_status_get**](InteractionsApi.md#vversion_interactions_exchange_status_get) | **GET** /v{version}/interactions/exchange-status | Get Exchange pipeline statuses by correlation or interaction ID
[**vversion_interactions_exchange_status_range_get**](InteractionsApi.md#vversion_interactions_exchange_status_range_get) | **GET** /v{version}/interactions/exchange-status/range | Get Exchange pipeline statuses by date range
[**vversion_interactions_interaction_id_transactions_get**](InteractionsApi.md#vversion_interactions_interaction_id_transactions_get) | **GET** /v{version}/interactions/{interactionId}/transactions | Get external API transactions by interactionId
[**vversion_interactions_post**](InteractionsApi.md#vversion_interactions_post) | **POST** /v{version}/interactions | Post interactions data
[**vversion_interactions_transactions_get**](InteractionsApi.md#vversion_interactions_transactions_get) | **GET** /v{version}/interactions/transactions | Get external API transaction logs by date range


# **vversion_interactions_exchange_status_get**
> ExchangeInteractionStatusDtoCursorPaginatedResponseDto vversion_interactions_exchange_status_get(version, correlation_id=correlation_id, interaction_id=interaction_id, cursor=cursor, limit=limit)

Get Exchange pipeline statuses by correlation or interaction ID

Returns Exchange pipeline statuses filtered by either correlationId or interactionId.  Supports cursor-based pagination.

### Example

* Basic Authentication (Basic):

```python
import ddx_interactions_api
from ddx_interactions_api.models.exchange_interaction_status_dto_cursor_paginated_response_dto import ExchangeInteractionStatusDtoCursorPaginatedResponseDto
from ddx_interactions_api.rest import ApiException
from pprint import pprint

# Authentication is HTTP basic, with your API key in the password field and an
# empty username. The key has the form "<keyId>.<secret>".
#
# The host defaults to https://api.movementinfrastructure.org. Pass host= to target another server.
# See configuration.py for all supported parameters.
import os

configuration = ddx_interactions_api.Configuration(
    username = "",
    password = os.environ["DDX_API_KEY"],
)

# Enter a context with an instance of the API client
with ddx_interactions_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ddx_interactions_api.InteractionsApi(api_client)
    version = '1' # str |  (default to '1')
    correlation_id = 'correlation_id_example' # str | The correlation ID returned from the initial publish response. (optional)
    interaction_id = 'interaction_id_example' # str | The interaction's unique identifier (GUID). (optional)
    cursor = 'cursor_example' # str | Opaque pagination token from a previous response's nextCursor field. (optional)
    limit = 56 # int | Maximum number of results to return (default 100, max 1000). (optional)

    try:
        # Get Exchange pipeline statuses by correlation or interaction ID
        api_response = api_instance.vversion_interactions_exchange_status_get(version, correlation_id=correlation_id, interaction_id=interaction_id, cursor=cursor, limit=limit)
        print("The response of InteractionsApi->vversion_interactions_exchange_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->vversion_interactions_exchange_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;1&#39;]
 **correlation_id** | **str**| The correlation ID returned from the initial publish response. | [optional] 
 **interaction_id** | **str**| The interaction&#39;s unique identifier (GUID). | [optional] 
 **cursor** | **str**| Opaque pagination token from a previous response&#39;s nextCursor field. | [optional] 
 **limit** | **int**| Maximum number of results to return (default 100, max 1000). | [optional] 

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
**200** | Paginated list of Exchange statuses |  -  |
**400** | Invalid or ambiguous filter parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vversion_interactions_exchange_status_range_get**
> ExchangeInteractionStatusDtoCursorPaginatedResponseDto vversion_interactions_exchange_status_range_get(version, start_date=start_date, end_date=end_date, cursor=cursor, limit=limit)

Get Exchange pipeline statuses by date range

Returns Exchange pipeline statuses for interactions published within the specified date range.  Supports cursor-based pagination. Maximum date range is 30 days.

### Example

* Basic Authentication (Basic):

```python
import ddx_interactions_api
from ddx_interactions_api.models.exchange_interaction_status_dto_cursor_paginated_response_dto import ExchangeInteractionStatusDtoCursorPaginatedResponseDto
from ddx_interactions_api.rest import ApiException
from pprint import pprint

# Authentication is HTTP basic, with your API key in the password field and an
# empty username. The key has the form "<keyId>.<secret>".
#
# The host defaults to https://api.movementinfrastructure.org. Pass host= to target another server.
# See configuration.py for all supported parameters.
import os

configuration = ddx_interactions_api.Configuration(
    username = "",
    password = os.environ["DDX_API_KEY"],
)

# Enter a context with an instance of the API client
with ddx_interactions_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ddx_interactions_api.InteractionsApi(api_client)
    version = '1' # str |  (default to '1')
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Beginning of date range (inclusive, UTC). (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | End of date range (inclusive, UTC). Defaults to current UTC time. (optional)
    cursor = 'cursor_example' # str | Opaque pagination token from a previous response's nextCursor field. (optional)
    limit = 56 # int | Maximum number of results to return (default 100, max 1000). (optional)

    try:
        # Get Exchange pipeline statuses by date range
        api_response = api_instance.vversion_interactions_exchange_status_range_get(version, start_date=start_date, end_date=end_date, cursor=cursor, limit=limit)
        print("The response of InteractionsApi->vversion_interactions_exchange_status_range_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->vversion_interactions_exchange_status_range_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;1&#39;]
 **start_date** | **datetime**| Beginning of date range (inclusive, UTC). | [optional] 
 **end_date** | **datetime**| End of date range (inclusive, UTC). Defaults to current UTC time. | [optional] 
 **cursor** | **str**| Opaque pagination token from a previous response&#39;s nextCursor field. | [optional] 
 **limit** | **int**| Maximum number of results to return (default 100, max 1000). | [optional] 

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
**200** | Paginated list of Exchange statuses |  -  |
**400** | Invalid date range, limit, or cursor |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vversion_interactions_interaction_id_transactions_get**
> InteractionsExternalApiTransactionDtoGetResponseDto vversion_interactions_interaction_id_transactions_get(interaction_id, version, show_only_failed_transactions=show_only_failed_transactions)

Get external API transactions by interactionId

Get all external API transaction records for the specified interaction.

### Example

* Basic Authentication (Basic):

```python
import ddx_interactions_api
from ddx_interactions_api.models.interactions_external_api_transaction_dto_get_response_dto import InteractionsExternalApiTransactionDtoGetResponseDto
from ddx_interactions_api.rest import ApiException
from pprint import pprint

# Authentication is HTTP basic, with your API key in the password field and an
# empty username. The key has the form "<keyId>.<secret>".
#
# The host defaults to https://api.movementinfrastructure.org. Pass host= to target another server.
# See configuration.py for all supported parameters.
import os

configuration = ddx_interactions_api.Configuration(
    username = "",
    password = os.environ["DDX_API_KEY"],
)

# Enter a context with an instance of the API client
with ddx_interactions_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ddx_interactions_api.InteractionsApi(api_client)
    interaction_id = 'interaction_id_example' # str | ID of the interaction to retrieve records for.
    version = '1' # str |  (default to '1')
    show_only_failed_transactions = True # bool | When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. (optional) (default to True)

    try:
        # Get external API transactions by interactionId
        api_response = api_instance.vversion_interactions_interaction_id_transactions_get(interaction_id, version, show_only_failed_transactions=show_only_failed_transactions)
        print("The response of InteractionsApi->vversion_interactions_interaction_id_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->vversion_interactions_interaction_id_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interaction_id** | **str**| ID of the interaction to retrieve records for. | 
 **version** | **str**|  | [default to &#39;1&#39;]
 **show_only_failed_transactions** | **bool**| When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. | [optional] [default to True]

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vversion_interactions_post**
> InteractionsBatchResultDto vversion_interactions_post(version, interactions_dto=interactions_dto)

Post interactions data

This endpoint is used to post interactions data to the Interactions API that will be published to Pub/Sub.  A maximum of 100 interactions can be submitted per request.

### Example

* Basic Authentication (Basic):

```python
import ddx_interactions_api
from ddx_interactions_api.models.interactions_batch_result_dto import InteractionsBatchResultDto
from ddx_interactions_api.models.interactions_dto import InteractionsDto
from ddx_interactions_api.rest import ApiException
from pprint import pprint

# Authentication is HTTP basic, with your API key in the password field and an
# empty username. The key has the form "<keyId>.<secret>".
#
# The host defaults to https://api.movementinfrastructure.org. Pass host= to target another server.
# See configuration.py for all supported parameters.
import os

configuration = ddx_interactions_api.Configuration(
    username = "",
    password = os.environ["DDX_API_KEY"],
)

# Enter a context with an instance of the API client
with ddx_interactions_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ddx_interactions_api.InteractionsApi(api_client)
    version = '1' # str |  (default to '1')
    interactions_dto = ddx_interactions_api.InteractionsDto() # InteractionsDto |  (optional)

    try:
        # Post interactions data
        api_response = api_instance.vversion_interactions_post(version, interactions_dto=interactions_dto)
        print("The response of InteractionsApi->vversion_interactions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->vversion_interactions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;1&#39;]
 **interactions_dto** | [**InteractionsDto**](InteractionsDto.md)|  | [optional] 

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
**200** | All interactions were valid and successfully published |  -  |
**207** | Some interactions were rejected; see response body for details |  -  |
**400** | Invalid interactions data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vversion_interactions_transactions_get**
> InteractionsExternalApiTransactionDtoGetResponseDto vversion_interactions_transactions_get(version, start_date=start_date, end_date=end_date, show_only_failed_transactions=show_only_failed_transactions)

Get external API transaction logs by date range

Get all external API transaction records within the date range specified, for a maximum of up to a 30 day span.

### Example

* Basic Authentication (Basic):

```python
import ddx_interactions_api
from ddx_interactions_api.models.interactions_external_api_transaction_dto_get_response_dto import InteractionsExternalApiTransactionDtoGetResponseDto
from ddx_interactions_api.rest import ApiException
from pprint import pprint

# Authentication is HTTP basic, with your API key in the password field and an
# empty username. The key has the form "<keyId>.<secret>".
#
# The host defaults to https://api.movementinfrastructure.org. Pass host= to target another server.
# See configuration.py for all supported parameters.
import os

configuration = ddx_interactions_api.Configuration(
    username = "",
    password = os.environ["DDX_API_KEY"],
)

# Enter a context with an instance of the API client
with ddx_interactions_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ddx_interactions_api.InteractionsApi(api_client)
    version = '1' # str |  (default to '1')
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Beginning of date range to show transactions for (inclusive). Must be provided in UTC, and be within 30 days of endDate. (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | End of date range to show transactions for (inclusive). Defaults to current date/time if not provided. Must be provided in UTC if specified,              and be within 30 days of startDate. (optional)
    show_only_failed_transactions = True # bool | When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. (optional) (default to True)

    try:
        # Get external API transaction logs by date range
        api_response = api_instance.vversion_interactions_transactions_get(version, start_date=start_date, end_date=end_date, show_only_failed_transactions=show_only_failed_transactions)
        print("The response of InteractionsApi->vversion_interactions_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InteractionsApi->vversion_interactions_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;1&#39;]
 **start_date** | **datetime**| Beginning of date range to show transactions for (inclusive). Must be provided in UTC, and be within 30 days of endDate. | [optional] 
 **end_date** | **datetime**| End of date range to show transactions for (inclusive). Defaults to current date/time if not provided. Must be provided in UTC if specified,              and be within 30 days of startDate. | [optional] 
 **show_only_failed_transactions** | **bool**| When true, will return only transactions with Failed, Invalid, or Duplicate status. True by default. | [optional] [default to True]

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

