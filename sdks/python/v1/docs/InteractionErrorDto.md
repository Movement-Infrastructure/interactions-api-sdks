# InteractionErrorDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 

## Example

```python
from mig_interactions_api.models.interaction_error_dto import InteractionErrorDto

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionErrorDto from a JSON string
interaction_error_dto_instance = InteractionErrorDto.from_json(json)
# print the JSON string representation of the object
print(InteractionErrorDto.to_json())

# convert the object into a dict
interaction_error_dto_dict = interaction_error_dto_instance.to_dict()
# create an instance of InteractionErrorDto from a dict
interaction_error_dto_from_dict = InteractionErrorDto.from_dict(interaction_error_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


