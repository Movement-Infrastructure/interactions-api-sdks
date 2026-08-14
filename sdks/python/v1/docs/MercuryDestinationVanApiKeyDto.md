# MercuryDestinationVanApiKeyDto

VAN-specific DTO containing VAN key profile details along with DDx configuration for that VAN key for the linked destination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**van_api_key_profile_details** | [**VanApiKeyDto**](VanApiKeyDto.md) |  | [optional] 
**selected_db_mode_access** | [**VanDatabaseMode**](VanDatabaseMode.md) |  | [optional] 

## Example

```python
from mig_interactions_api.models.mercury_destination_van_api_key_dto import MercuryDestinationVanApiKeyDto

# TODO update the JSON string below
json = "{}"
# create an instance of MercuryDestinationVanApiKeyDto from a JSON string
mercury_destination_van_api_key_dto_instance = MercuryDestinationVanApiKeyDto.from_json(json)
# print the JSON string representation of the object
print(MercuryDestinationVanApiKeyDto.to_json())

# convert the object into a dict
mercury_destination_van_api_key_dto_dict = mercury_destination_van_api_key_dto_instance.to_dict()
# create an instance of MercuryDestinationVanApiKeyDto from a dict
mercury_destination_van_api_key_dto_from_dict = MercuryDestinationVanApiKeyDto.from_dict(mercury_destination_van_api_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


