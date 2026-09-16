# DdxInteractionsApi::ContactInfo

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **email** | **Array&lt;String&gt;** | Email addresses of the person being interacted with. | [optional] |
| **phone** | **Array&lt;String&gt;** | Phone numbers of the person being interacted with. Should be in E.164 format (e.g. +1234567890). | [optional] |
| **address** | [**Array&lt;Address&gt;**](Address.md) | Physical addresses of the person being interacted with. | [optional] |
| **first_name** | **String** | Optional first name field for person being interacted with. | [optional] |
| **middle_name** | **String** | Optional middle name field for person being interacted with. | [optional] |
| **last_name** | **String** | Optional last name field for person being interacted with. | [optional] |
| **social_handle** | **Array&lt;String&gt;** | Optional social media handles for person being interacted with. | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::ContactInfo.new(
  email: null,
  phone: null,
  address: null,
  first_name: null,
  middle_name: null,
  last_name: null,
  social_handle: null
)
```

