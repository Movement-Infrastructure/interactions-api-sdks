# DdxInteractionsApi::RejectedInteractionsDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **count** | **Integer** | The total number of rejected interactions. | [optional] |
| **data** | [**Array&lt;RejectedInteractionDto&gt;**](RejectedInteractionDto.md) | The list of rejected interactions. | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::RejectedInteractionsDto.new(
  count: null,
  data: null
)
```

