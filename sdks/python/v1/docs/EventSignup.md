# EventSignup

Represents an event signup captured during an interaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | [**EventDetails**](EventDetails.md) |  | 
**shifts** | [**List[EventDetails]**](EventDetails.md) | Optional array of shift identifiers for specific shifts within the event | [optional] 
**role** | [**EventRole**](EventRole.md) |  | [optional] 
**status** | [**EventSignupStatus**](EventSignupStatus.md) |  | [optional] 

## Example

```python
from ddx_interactions_api.models.event_signup import EventSignup

# TODO update the JSON string below
json = "{}"
# create an instance of EventSignup from a JSON string
event_signup_instance = EventSignup.from_json(json)
# print the JSON string representation of the object
print(EventSignup.to_json())

# convert the object into a dict
event_signup_dict = event_signup_instance.to_dict()
# create an instance of EventSignup from a dict
event_signup_from_dict = EventSignup.from_dict(event_signup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


