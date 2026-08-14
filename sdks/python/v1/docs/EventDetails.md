# EventDetails

Represents an identifier and the namespace its value belongs to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier value | 
**type** | **str** | The namespace the id belongs to, scoped to the field this object appears in: an event namespace in event_id (e.g. \&quot;vendor_event_id\&quot;, \&quot;vendor_signup_id\&quot;), or a shift namespace in shifts (e.g. \&quot;vendor_shift_id\&quot;). | 

## Example

```python
from mig_interactions_api.models.event_details import EventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EventDetails from a JSON string
event_details_instance = EventDetails.from_json(json)
# print the JSON string representation of the object
print(EventDetails.to_json())

# convert the object into a dict
event_details_dict = event_details_instance.to_dict()
# create an instance of EventDetails from a dict
event_details_from_dict = EventDetails.from_dict(event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


