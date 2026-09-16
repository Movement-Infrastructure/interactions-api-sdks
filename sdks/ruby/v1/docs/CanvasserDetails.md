# DdxInteractionsApi::CanvasserDetails

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **type** | **String** | Type of the canvasser identifier specified in &#39;id&#39;.  Required when Canvasser is provided. |  |
| **id** | **String** | The actual canvasser identifier used during the outreach attempt.  Examples: user ID, employee number, volunteer ID, etc.  Required when Canvasser is provided. |  |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::CanvasserDetails.new(
  type: null,
  id: null
)
```

