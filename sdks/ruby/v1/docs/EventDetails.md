# DdxInteractionsApi::EventDetails

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | The identifier value |  |
| **type** | **String** | The namespace the id belongs to, scoped to the field this object appears in: an event namespace in event_id (e.g. \&quot;vendor_event_id\&quot;, \&quot;vendor_signup_id\&quot;), or a shift namespace in shifts (e.g. \&quot;vendor_shift_id\&quot;). |  |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::EventDetails.new(
  id: null,
  type: null
)
```

