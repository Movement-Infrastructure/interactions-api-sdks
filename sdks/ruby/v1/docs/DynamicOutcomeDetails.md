# DdxInteractionsApi::DynamicOutcomeDetails

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **operation** | [**OutcomeDetailOperation**](OutcomeDetailOperation.md) |  | [optional] |
| **type** | **String** | This field categorizes the type of detailed outcome information being provided. | [optional] |
| **value** | **Object** |  Provide additional details of the outreach attempt. This field can be provided as a string or int though only the object form is shown here. | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::DynamicOutcomeDetails.new(
  operation: null,
  type: null,
  value: null
)
```

