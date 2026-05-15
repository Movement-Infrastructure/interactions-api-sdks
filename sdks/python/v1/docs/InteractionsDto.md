# InteractionsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interactions** | [**List[InteractionDto]**](InteractionDto.md) |  | [optional] 

## Example

```python
from mi_interactions_api.models.interactions_dto import InteractionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionsDto from a JSON string
interactions_dto_instance = InteractionsDto.from_json(json)
# print the JSON string representation of the object
print(InteractionsDto.to_json())

# convert the object into a dict
interactions_dto_dict = interactions_dto_instance.to_dict()
# create an instance of InteractionsDto from a dict
interactions_dto_from_dict = InteractionsDto.from_dict(interactions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


