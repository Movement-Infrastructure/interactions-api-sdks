# DdxInteractionsApi::CommunicationConsentOutcomeDetails

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **operation** | **String** | Describes whether this outcome detail is being created, deleted, or updated. Which operations are accepted varies by outcome type. Defaults to create. | [optional] |
| **type** | **String** | This field categorizes the type of detailed outcome information being provided. | [optional] |
| **value** | [**CommunicationConsent**](CommunicationConsent.md) |  |  |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::CommunicationConsentOutcomeDetails.new(
  operation: null,
  type: null,
  value: null
)
```

