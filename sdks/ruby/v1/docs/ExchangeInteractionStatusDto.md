# DdxInteractionsApi::ExchangeInteractionStatusDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **correlation_id** | **String** | DDx API request identifier. | [optional] |
| **interaction_id** | **String** | The interaction&#39;s unique identifier. | [optional] |
| **status** | [**ExchangeInteractionStatus**](ExchangeInteractionStatus.md) |  | [optional] |
| **exchange_data_types** | **String** | The Exchange data types the interaction was transformed into. | [optional] |
| **publish_time** | **Time** | Timestamp when the interaction was received into the Exchange pipeline (Pub/Sub publish time). | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::ExchangeInteractionStatusDto.new(
  correlation_id: null,
  interaction_id: null,
  status: null,
  exchange_data_types: null,
  publish_time: null
)
```

