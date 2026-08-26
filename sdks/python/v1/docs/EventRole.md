# EventRole

Represents the role of a participant in an event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The role name or description | [optional] 

## Example

```python
from ddx_interactions_api.models.event_role import EventRole

# TODO update the JSON string below
json = "{}"
# create an instance of EventRole from a JSON string
event_role_instance = EventRole.from_json(json)
# print the JSON string representation of the object
print(EventRole.to_json())

# convert the object into a dict
event_role_dict = event_role_instance.to_dict()
# create an instance of EventRole from a dict
event_role_from_dict = EventRole.from_dict(event_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


