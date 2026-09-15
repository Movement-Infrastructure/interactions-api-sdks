# DdxInteractionsApi::InteractionsExternalApiTransactionDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **date_created_utc** | **Time** | The UTC date and time at which the request was received. | [optional] |
| **interaction_id** | **String** | ID used to identify the interaction; ID will have been returned from the initial publish response. | [optional] |
| **correlation_id** | **String** | DDx API request identifier, provided as X-Correlation-Id on interactions responses for use linking all interactions in a request. | [optional] |
| **status** | [**ExternalTransactionStatus**](ExternalTransactionStatus.md) |  | [optional] |
| **logs** | [**Array&lt;InteractionsExternalApiTransactionLogDto&gt;**](InteractionsExternalApiTransactionLogDto.md) | Any logs associated with this external API transaction. | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::InteractionsExternalApiTransactionDto.new(
  date_created_utc: null,
  interaction_id: null,
  correlation_id: null,
  status: null,
  logs: null
)
```

