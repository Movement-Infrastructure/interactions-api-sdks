# InteractionVanFieldsDto

VAN-specific data for an interaction. Must be provided if if the Interactions API Key used on the request  is configured with VAN as a destination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_type_id** | **str** | VAN contact type ID. Must match a Contact Type accessible to the destination VAN committee.  See https://docs.ngpvan.com/reference/canvassresponsescontacttypes for details on retrieving accessible contact types. | [optional] 
**result_code_id** | **str** | VAN contact attempt result code, representing the result of that contact attempt. Result code availibility varies based on  contact type, so this value must represent a code that is available to the Contact Type ID specified above.  See https://docs.ngpvan.com/reference/canvassresponsesresultcodes to view Result Codes accessible to the destination VAN committee. | [optional] 

## Example

```python
from mi_interactions_api.models.interaction_van_fields_dto import InteractionVanFieldsDto

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionVanFieldsDto from a JSON string
interaction_van_fields_dto_instance = InteractionVanFieldsDto.from_json(json)
# print the JSON string representation of the object
print(InteractionVanFieldsDto.to_json())

# convert the object into a dict
interaction_van_fields_dto_dict = interaction_van_fields_dto_instance.to_dict()
# create an instance of InteractionVanFieldsDto from a dict
interaction_van_fields_dto_from_dict = InteractionVanFieldsDto.from_dict(interaction_van_fields_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


