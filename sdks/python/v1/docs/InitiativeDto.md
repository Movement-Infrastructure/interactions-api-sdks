# InitiativeDto

Represents an initiative associated with an interaction, such as a campaign identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the initiative identifier specified in &#39;id&#39;. | [optional] 
**id** | **str** | The actual initiative identifier, such as a campaign ID. | [optional] 

## Example

```python
from mi_interactions_api.models.initiative_dto import InitiativeDto

# TODO update the JSON string below
json = "{}"
# create an instance of InitiativeDto from a JSON string
initiative_dto_instance = InitiativeDto.from_json(json)
# print the JSON string representation of the object
print(InitiativeDto.to_json())

# convert the object into a dict
initiative_dto_dict = initiative_dto_instance.to_dict()
# create an instance of InitiativeDto from a dict
initiative_dto_from_dict = InitiativeDto.from_dict(initiative_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


