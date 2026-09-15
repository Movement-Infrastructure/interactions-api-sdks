# DdxInteractionsApi::InteractionDtoOutcomesDetailedInner

## Class instance methods

### `openapi_one_of`

Returns the list of classes defined in oneOf.

#### Example

```ruby
require 'ddx_interactions_api'

DdxInteractionsApi::InteractionDtoOutcomesDetailedInner.openapi_one_of
# =>
# [
#   :'ActivistCodeOutcomeDetails',
#   :'CommunicationConsentOutcomeDetails',
#   :'DynamicOutcomeDetails',
#   :'EventSignupOutcomeDetails',
#   :'SurveyResponseOutcomeDetails'
# ]
```

### `openapi_discriminator_name`

Returns the discriminator's property name.

#### Example

```ruby
require 'ddx_interactions_api'

DdxInteractionsApi::InteractionDtoOutcomesDetailedInner.openapi_discriminator_name
# => :'type'
```

### `openapi_discriminator_name`

Returns the discriminator's mapping.

#### Example

```ruby
require 'ddx_interactions_api'

DdxInteractionsApi::InteractionDtoOutcomesDetailedInner.openapi_discriminator_mapping
# =>
# {
#   :'activist_code' => :'ActivistCodeOutcomeDetails',
#   :'communication_consent' => :'CommunicationConsentOutcomeDetails',
#   :'event_signup' => :'EventSignupOutcomeDetails',
#   :'example_type' => :'DynamicOutcomeDetails',
#   :'survey_response' => :'SurveyResponseOutcomeDetails'
# }
```

### build

Find the appropriate object from the `openapi_one_of` list and casts the data into it.

#### Example

```ruby
require 'ddx_interactions_api'

DdxInteractionsApi::InteractionDtoOutcomesDetailedInner.build(data)
# => #<ActivistCodeOutcomeDetails:0x00007fdd4aab02a0>

DdxInteractionsApi::InteractionDtoOutcomesDetailedInner.build(data_that_doesnt_match)
# => nil
```

#### Parameters

| Name | Type | Description |
| ---- | ---- | ----------- |
| **data** | **Mixed** | data to be matched against the list of oneOf items |

#### Return type

- `ActivistCodeOutcomeDetails`
- `CommunicationConsentOutcomeDetails`
- `DynamicOutcomeDetails`
- `EventSignupOutcomeDetails`
- `SurveyResponseOutcomeDetails`
- `nil` (if no type matches)

