# DdxInteractionsApi::AcceptedInteractionDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **interaction_id** | **String** | ID used to identify the interaction; ID will have been returned from the initial publish response. | [optional] |
| **index** | **Integer** | Index of the accepted interaction in the batch. | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::AcceptedInteractionDto.new(
  interaction_id: null,
  index: null
)
```

