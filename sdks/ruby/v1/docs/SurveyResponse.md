# DdxInteractionsApi::SurveyResponse

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **question_id** | **String** | Unique identifier for the survey question being asked;  the value may be retrieved from the system that sourced the question.  Must be an integer when VAN or DDx Exchange is a destination. | [optional] |
| **question_text** | **String** | The question text presented during an interaction |  |
| **response_id** | **String** | Unique identifier for the survey response associated with the question;  the value may be retrieved from the system that sourced the question.  Must be an integer when VAN or DDx Exchange is a destination. | [optional] |
| **response_text** | **String** | An answer to the question.  Required when Survey Question text is provided. |  |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::SurveyResponse.new(
  question_id: null,
  question_text: null,
  response_id: null,
  response_text: null
)
```

