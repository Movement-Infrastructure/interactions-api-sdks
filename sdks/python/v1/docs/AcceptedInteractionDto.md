# AcceptedInteractionDto

Represents an accepted interaction with its associated index.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interaction_id** | **str** | ID used to identify the interaction; ID will have been returned from the initial publish response. | [optional] 
**index** | **int** | Index of the accepted interaction in the batch. | [optional] 

## Example

```python
from ddx_interactions_api.models.accepted_interaction_dto import AcceptedInteractionDto

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedInteractionDto from a JSON string
accepted_interaction_dto_instance = AcceptedInteractionDto.from_json(json)
# print the JSON string representation of the object
print(AcceptedInteractionDto.to_json())

# convert the object into a dict
accepted_interaction_dto_dict = accepted_interaction_dto_instance.to_dict()
# create an instance of AcceptedInteractionDto from a dict
accepted_interaction_dto_from_dict = AcceptedInteractionDto.from_dict(accepted_interaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


