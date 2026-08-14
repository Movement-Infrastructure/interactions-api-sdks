# PersonIdentifier

Represents a person involved in an interaction, including their identifier and optional contact information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A primary identifier for tracking individual voters. This can be an integer (e.g. for DNC person_ids),  a string (for UUIDs, phone numbers), or other identifier formats depending on the source system.  Used to link voter records across different data sources and track in-state voter history over time. | 
**type** | **str** | Type of identifier or source system that generated the id.  Examples include \&quot;VAN\&quot;, \&quot;phone\&quot;, \&quot;slimCRM\&quot;, \&quot;DNC\&quot;, \&quot;SOS\&quot;, etc.   This field indicates the origin or authority of the person identifier. | 

## Example

```python
from mig_interactions_api.models.person_identifier import PersonIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of PersonIdentifier from a JSON string
person_identifier_instance = PersonIdentifier.from_json(json)
# print the JSON string representation of the object
print(PersonIdentifier.to_json())

# convert the object into a dict
person_identifier_dict = person_identifier_instance.to_dict()
# create an instance of PersonIdentifier from a dict
person_identifier_from_dict = PersonIdentifier.from_dict(person_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


