# RejectedInteractionDto

Represents a rejected interaction with its associated errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interaction_id** | **str** | ID used to identify the interaction; ID will have been returned from the initial publish response. | [optional] 
**index** | **int** | Index of the rejected interaction in the batch. | [optional] 
**errors** | [**List[InteractionErrorDto]**](InteractionErrorDto.md) | List of errors associated with the rejected interaction. | [optional] 

## Example

```python
from mig_interactions_api.models.rejected_interaction_dto import RejectedInteractionDto

# TODO update the JSON string below
json = "{}"
# create an instance of RejectedInteractionDto from a JSON string
rejected_interaction_dto_instance = RejectedInteractionDto.from_json(json)
# print the JSON string representation of the object
print(RejectedInteractionDto.to_json())

# convert the object into a dict
rejected_interaction_dto_dict = rejected_interaction_dto_instance.to_dict()
# create an instance of RejectedInteractionDto from a dict
rejected_interaction_dto_from_dict = RejectedInteractionDto.from_dict(rejected_interaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


