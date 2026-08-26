# WhoAmIApiKeyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_key_id** | **int** | Unique identifier that specifies which API Key is being used | 
**source** | [**SimpleMovementAppDto**](SimpleMovementAppDto.md) |  | 
**workspace** | [**SimpleWorkspaceDto**](SimpleWorkspaceDto.md) |  | 
**expire_date** | **datetime** | The date and time the API Key is set to expire. The time should be evaluated in Eastern Time. | [optional] 
**destinations** | [**List[SimpleDestinationDto]**](SimpleDestinationDto.md) | The destinations enabled for this API key | [optional] 
**van_api_key** | [**MercuryDestinationVanApiKeyDto**](MercuryDestinationVanApiKeyDto.md) |  | [optional] 

## Example

```python
from mig_interactions_api.models.who_am_i_api_key_dto import WhoAmIApiKeyDto

# TODO update the JSON string below
json = "{}"
# create an instance of WhoAmIApiKeyDto from a JSON string
who_am_i_api_key_dto_instance = WhoAmIApiKeyDto.from_json(json)
# print the JSON string representation of the object
print(WhoAmIApiKeyDto.to_json())

# convert the object into a dict
who_am_i_api_key_dto_dict = who_am_i_api_key_dto_instance.to_dict()
# create an instance of WhoAmIApiKeyDto from a dict
who_am_i_api_key_dto_from_dict = WhoAmIApiKeyDto.from_dict(who_am_i_api_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


