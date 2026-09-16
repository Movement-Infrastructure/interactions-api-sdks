# DdxInteractionsApi::Address

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **address_line1** | **String** | The primary street address (e.g., house number and street name). |  |
| **address_line2** | **String** | The secondary address information (e.g., apartment, suite, unit number). | [optional] |
| **city** | **String** | The city of the address. |  |
| **state** | **String** | The state or region of the address. |  |
| **postal_code** | **String** | The postal (ZIP) code for the address. Can accept ZIP5, ZIP+4, or ZIP9 format. |  |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::Address.new(
  address_line1: null,
  address_line2: null,
  city: null,
  state: null,
  postal_code: null
)
```

