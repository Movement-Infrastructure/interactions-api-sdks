# DdxInteractionsApi::RejectedInteractionDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **interaction_id** | **String** | ID used to identify the interaction; ID will have been returned from the initial publish response. | [optional] |
| **index** | **Integer** | Index of the rejected interaction in the batch. | [optional] |
| **errors** | [**Array&lt;InteractionErrorDto&gt;**](InteractionErrorDto.md) | List of errors associated with the rejected interaction. | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::RejectedInteractionDto.new(
  interaction_id: null,
  index: null,
  errors: null
)
```

