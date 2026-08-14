# SurveyResponseOutcomeDetails

Represents a survey question and response obtained from an interaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | Describes whether this outcome detail is being created, deleted, or updated. Which operations are accepted varies by outcome type. Defaults to create. | [optional] 
**type** | **str** | This field categorizes the type of detailed outcome information being provided. | [optional] 
**value** | [**SurveyResponse**](SurveyResponse.md) |  | 

## Example

```python
from mig_interactions_api.models.survey_response_outcome_details import SurveyResponseOutcomeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyResponseOutcomeDetails from a JSON string
survey_response_outcome_details_instance = SurveyResponseOutcomeDetails.from_json(json)
# print the JSON string representation of the object
print(SurveyResponseOutcomeDetails.to_json())

# convert the object into a dict
survey_response_outcome_details_dict = survey_response_outcome_details_instance.to_dict()
# create an instance of SurveyResponseOutcomeDetails from a dict
survey_response_outcome_details_from_dict = SurveyResponseOutcomeDetails.from_dict(survey_response_outcome_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


