# DdxInteractionsApi::InteractionVanFieldsDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **contact_type_id** | **String** | VAN contact type ID. Must match a Contact Type accessible to the destination VAN committee.  See https://docs.ngpvan.com/reference/canvassresponsescontacttypes for details on retrieving accessible contact types. | [optional] |
| **result_code_id** | **String** | VAN contact attempt result code, representing the result of that contact attempt. Result code availibility varies based on  contact type, so this value must represent a code that is available to the Contact Type ID specified above.  See https://docs.ngpvan.com/reference/canvassresponsesresultcodes to view Result Codes accessible to the destination VAN committee. | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::InteractionVanFieldsDto.new(
  contact_type_id: null,
  result_code_id: null
)
```

