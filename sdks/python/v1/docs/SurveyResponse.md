# SurveyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question_id** | **str** | Unique identifier for the survey question being asked;  the value may be retrieved from the system that sourced the question | [optional] 
**question_text** | **str** | The question text presented during an interaction | 
**response_id** | **str** | Unique identifier for the survey response associated with the question;  the value may be retrieved from the system that sourced the question | [optional] 
**response_text** | **str** | An answer to the question.  Required when Survey Question text is provided. | 

## Example

```python
from mig_interactions_api.models.survey_response import SurveyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyResponse from a JSON string
survey_response_instance = SurveyResponse.from_json(json)
# print the JSON string representation of the object
print(SurveyResponse.to_json())

# convert the object into a dict
survey_response_dict = survey_response_instance.to_dict()
# create an instance of SurveyResponse from a dict
survey_response_from_dict = SurveyResponse.from_dict(survey_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


