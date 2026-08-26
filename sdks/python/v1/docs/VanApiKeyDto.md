# VanApiKeyDto

VAN-specific external key fields, for display and other front-end use

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_api_key_id** | **int** |  | [optional] 
**type** | [**ExternalApiKeyType**](ExternalApiKeyType.md) |  | [optional] 
**status** | [**ExternalApiKeyStatus**](ExternalApiKeyStatus.md) |  | [optional] 
**name** | **str** |  | [optional] 
**date_created** | **datetime** |  | [optional] 
**connections** | **int** |  | [optional] 
**committee_name** | **str** |  | [optional] 
**has_my_voters** | **bool** |  | [optional] 
**has_my_campaign** | **bool** |  | [optional] 
**key_ref** | **str** |  | [optional] 

## Example

```python
from ddx_interactions_api.models.van_api_key_dto import VanApiKeyDto

# TODO update the JSON string below
json = "{}"
# create an instance of VanApiKeyDto from a JSON string
van_api_key_dto_instance = VanApiKeyDto.from_json(json)
# print the JSON string representation of the object
print(VanApiKeyDto.to_json())

# convert the object into a dict
van_api_key_dto_dict = van_api_key_dto_instance.to_dict()
# create an instance of VanApiKeyDto from a dict
van_api_key_dto_from_dict = VanApiKeyDto.from_dict(van_api_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


