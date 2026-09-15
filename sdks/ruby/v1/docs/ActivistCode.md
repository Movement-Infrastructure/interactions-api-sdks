# DdxInteractionsApi::ActivistCode

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **activist_code_id** | **String** | Unique identifier for an activist code;  the value may be retrieved from the system that sourced the activist code | [optional] |
| **text** | **String** | The question or information prompted during the interaction |  |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::ActivistCode.new(
  activist_code_id: null,
  text: null
)
```

