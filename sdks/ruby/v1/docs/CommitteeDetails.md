# DdxInteractionsApi::CommitteeDetails

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **type** | **String** | Type of the committee identifier specified in &#39;id&#39;, representing the source context of the interaction. |  |
| **id** | **String** | The actual committee identifier itself. |  |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::CommitteeDetails.new(
  type: null,
  id: null
)
```

