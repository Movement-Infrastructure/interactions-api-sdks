# EventSignupStatus

Represents the status of an event signup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**EventSignupStatusValue**](EventSignupStatusValue.md) |  | 
**vendor_reference** | **str** | Open string field for vendor-specific reference information | [optional] 

## Example

```python
from mig_interactions_api.models.event_signup_status import EventSignupStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EventSignupStatus from a JSON string
event_signup_status_instance = EventSignupStatus.from_json(json)
# print the JSON string representation of the object
print(EventSignupStatus.to_json())

# convert the object into a dict
event_signup_status_dict = event_signup_status_instance.to_dict()
# create an instance of EventSignupStatus from a dict
event_signup_status_from_dict = EventSignupStatus.from_dict(event_signup_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


