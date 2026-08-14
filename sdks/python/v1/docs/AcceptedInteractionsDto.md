# AcceptedInteractionsDto

Represents a collection of accepted interactions along with their count.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total number of accepted interactions. | [optional] 
**data** | [**List[AcceptedInteractionDto]**](AcceptedInteractionDto.md) | The list of accepted interactions. | [optional] 

## Example

```python
from mig_interactions_api.models.accepted_interactions_dto import AcceptedInteractionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedInteractionsDto from a JSON string
accepted_interactions_dto_instance = AcceptedInteractionsDto.from_json(json)
# print the JSON string representation of the object
print(AcceptedInteractionsDto.to_json())

# convert the object into a dict
accepted_interactions_dto_dict = accepted_interactions_dto_instance.to_dict()
# create an instance of AcceptedInteractionsDto from a dict
accepted_interactions_dto_from_dict = AcceptedInteractionsDto.from_dict(accepted_interactions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


