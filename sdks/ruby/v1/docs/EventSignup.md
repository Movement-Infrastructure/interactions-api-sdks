# DdxInteractionsApi::EventSignup

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **event_id** | [**EventDetails**](EventDetails.md) |  |  |
| **shifts** | [**Array&lt;EventDetails&gt;**](EventDetails.md) | Optional array of shift identifiers for specific shifts within the event | [optional] |
| **role** | [**EventRole**](EventRole.md) |  | [optional] |
| **status** | [**EventSignupStatus**](EventSignupStatus.md) |  | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::EventSignup.new(
  event_id: null,
  shifts: null,
  role: null,
  status: null
)
```

