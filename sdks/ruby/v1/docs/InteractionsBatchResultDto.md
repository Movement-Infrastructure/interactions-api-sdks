# DdxInteractionsApi::InteractionsBatchResultDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **correlation_id** | **String** | DDx API request identifier, provided as X-Correlation-Id on interactions responses for use linking all interactions in a request. | [optional] |
| **total_interactions** | **Integer** | Total number of interactions in the batch. | [optional] |
| **accepted_interactions** | [**AcceptedInteractionsDto**](AcceptedInteractionsDto.md) |  | [optional] |
| **rejected_interactions** | [**RejectedInteractionsDto**](RejectedInteractionsDto.md) |  | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::InteractionsBatchResultDto.new(
  correlation_id: null,
  total_interactions: null,
  accepted_interactions: null,
  rejected_interactions: null
)
```

