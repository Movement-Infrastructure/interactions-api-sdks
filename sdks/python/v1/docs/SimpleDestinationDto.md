# SimpleDestinationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier for the destination | 
**name** | **str** | Display name for the destination | [optional] 
**is_van_destination** | **bool** | Indicator of whether the destination integrates with NGP VAN  and requires an associated VAN External API Key | [optional] 

## Example

```python
from ddx_interactions_api.models.simple_destination_dto import SimpleDestinationDto

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleDestinationDto from a JSON string
simple_destination_dto_instance = SimpleDestinationDto.from_json(json)
# print the JSON string representation of the object
print(SimpleDestinationDto.to_json())

# convert the object into a dict
simple_destination_dto_dict = simple_destination_dto_instance.to_dict()
# create an instance of SimpleDestinationDto from a dict
simple_destination_dto_from_dict = SimpleDestinationDto.from_dict(simple_destination_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


