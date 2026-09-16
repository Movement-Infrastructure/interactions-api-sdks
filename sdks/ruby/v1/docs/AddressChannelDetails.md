# DdxInteractionsApi::AddressChannelDetails

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | Optional; unique identifier for any known id for the channel &#x60;type&#x60; | [optional] |
| **type** | **String** | Specifies that the &#x60;type&#x60; of channel used was an &#x60;address&#x60; and a full address must be provided as the &#x60;value&#x60;. |  |
| **value** | [**Address**](Address.md) |  |  |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::AddressChannelDetails.new(
  id: null,
  type: null,
  value: null
)
```

