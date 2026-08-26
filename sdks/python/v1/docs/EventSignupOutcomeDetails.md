# EventSignupOutcomeDetails

Represents an event signup acquired during an interaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | Describes whether this outcome detail is being created, deleted, or updated. Which operations are accepted varies by outcome type. Defaults to create. | [optional] 
**type** | **str** | This field categorizes the type of detailed outcome information being provided. | [optional] 
**value** | [**EventSignup**](EventSignup.md) |  | 

## Example

```python
from ddx_interactions_api.models.event_signup_outcome_details import EventSignupOutcomeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EventSignupOutcomeDetails from a JSON string
event_signup_outcome_details_instance = EventSignupOutcomeDetails.from_json(json)
# print the JSON string representation of the object
print(EventSignupOutcomeDetails.to_json())

# convert the object into a dict
event_signup_outcome_details_dict = event_signup_outcome_details_instance.to_dict()
# create an instance of EventSignupOutcomeDetails from a dict
event_signup_outcome_details_from_dict = EventSignupOutcomeDetails.from_dict(event_signup_outcome_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


