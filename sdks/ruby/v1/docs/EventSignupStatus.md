# DdxInteractionsApi::EventSignupStatus

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **status** | [**EventSignupStatusValue**](EventSignupStatusValue.md) |  |  |
| **vendor_reference** | **String** | Open string field for vendor-specific reference information | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::EventSignupStatus.new(
  status: null,
  vendor_reference: null
)
```

