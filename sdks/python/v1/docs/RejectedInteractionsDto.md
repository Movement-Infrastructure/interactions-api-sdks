# RejectedInteractionsDto

Represents a collection of rejected interactions along with their count.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The total number of rejected interactions. | [optional] 
**data** | [**List[RejectedInteractionDto]**](RejectedInteractionDto.md) | The list of rejected interactions. | [optional] 

## Example

```python
from ddx_interactions_api.models.rejected_interactions_dto import RejectedInteractionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of RejectedInteractionsDto from a JSON string
rejected_interactions_dto_instance = RejectedInteractionsDto.from_json(json)
# print the JSON string representation of the object
print(RejectedInteractionsDto.to_json())

# convert the object into a dict
rejected_interactions_dto_dict = rejected_interactions_dto_instance.to_dict()
# create an instance of RejectedInteractionsDto from a dict
rejected_interactions_dto_from_dict = RejectedInteractionsDto.from_dict(rejected_interactions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


