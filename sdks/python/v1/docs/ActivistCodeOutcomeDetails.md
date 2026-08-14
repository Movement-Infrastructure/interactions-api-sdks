# ActivistCodeOutcomeDetails

Represents an activist code (e.g. affiliation, activity, or interest) acquired during an interaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This field categorizes the type of detailed outcome information being provided. | [optional] 
**value** | [**ActivistCode**](ActivistCode.md) |  | 

## Example

```python
from mig_interactions_api.models.activist_code_outcome_details import ActivistCodeOutcomeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ActivistCodeOutcomeDetails from a JSON string
activist_code_outcome_details_instance = ActivistCodeOutcomeDetails.from_json(json)
# print the JSON string representation of the object
print(ActivistCodeOutcomeDetails.to_json())

# convert the object into a dict
activist_code_outcome_details_dict = activist_code_outcome_details_instance.to_dict()
# create an instance of ActivistCodeOutcomeDetails from a dict
activist_code_outcome_details_from_dict = ActivistCodeOutcomeDetails.from_dict(activist_code_outcome_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


