# DynamicOutcomeDetails

Represents a generic Outcome Details object;  does not have any validation rules or JSON format limitations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**OutcomeDetailOperation**](OutcomeDetailOperation.md) |  | [optional] 
**type** | **str** | This field categorizes the type of detailed outcome information being provided. | [optional] 
**value** | **object** |  Provide additional details of the outreach attempt. This field can be provided as a string or int though only the object form is shown here. | [optional] 

## Example

```python
from mig_interactions_api.models.dynamic_outcome_details import DynamicOutcomeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicOutcomeDetails from a JSON string
dynamic_outcome_details_instance = DynamicOutcomeDetails.from_json(json)
# print the JSON string representation of the object
print(DynamicOutcomeDetails.to_json())

# convert the object into a dict
dynamic_outcome_details_dict = dynamic_outcome_details_instance.to_dict()
# create an instance of DynamicOutcomeDetails from a dict
dynamic_outcome_details_from_dict = DynamicOutcomeDetails.from_dict(dynamic_outcome_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


