# DdxInteractionsApi::InitiativeDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **type** | **String** | Type of the initiative identifier specified in &#39;id&#39;. | [optional] |
| **id** | **String** | The actual initiative identifier, such as a campaign ID. | [optional] |
| **name** | **String** | Descriptive name or title for the initiative. | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::InitiativeDto.new(
  type: null,
  id: null,
  name: null
)
```

