# DdxInteractionsApi::AcceptedInteractionsDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **count** | **Integer** | The total number of accepted interactions. | [optional] |
| **data** | [**Array&lt;AcceptedInteractionDto&gt;**](AcceptedInteractionDto.md) | The list of accepted interactions. | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::AcceptedInteractionsDto.new(
  count: null,
  data: null
)
```

