# SimpleMovementAppDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movement_app_id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from mig_interactions_api.models.simple_movement_app_dto import SimpleMovementAppDto

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleMovementAppDto from a JSON string
simple_movement_app_dto_instance = SimpleMovementAppDto.from_json(json)
# print the JSON string representation of the object
print(SimpleMovementAppDto.to_json())

# convert the object into a dict
simple_movement_app_dto_dict = simple_movement_app_dto_instance.to_dict()
# create an instance of SimpleMovementAppDto from a dict
simple_movement_app_dto_from_dict = SimpleMovementAppDto.from_dict(simple_movement_app_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


