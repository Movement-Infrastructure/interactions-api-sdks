# MinervaMetadataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of records returned in the response &#x60;data&#x60; array | [optional] 

## Example

```python
from mi_interactions_api.models.minerva_metadata_dto import MinervaMetadataDto

# TODO update the JSON string below
json = "{}"
# create an instance of MinervaMetadataDto from a JSON string
minerva_metadata_dto_instance = MinervaMetadataDto.from_json(json)
# print the JSON string representation of the object
print(MinervaMetadataDto.to_json())

# convert the object into a dict
minerva_metadata_dto_dict = minerva_metadata_dto_instance.to_dict()
# create an instance of MinervaMetadataDto from a dict
minerva_metadata_dto_from_dict = MinervaMetadataDto.from_dict(minerva_metadata_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


