# AddressChannelDetails

Represents that an address was used for an interaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Optional; unique identifier for any known id for the channel &#x60;type&#x60; | [optional] 
**type** | **str** | Specifies that the &#x60;type&#x60; of channel used was an &#x60;address&#x60; and a full address must be provided as the &#x60;value&#x60;. | 
**value** | [**Address**](Address.md) |  | 

## Example

```python
from ddx_interactions_api.models.address_channel_details import AddressChannelDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AddressChannelDetails from a JSON string
address_channel_details_instance = AddressChannelDetails.from_json(json)
# print the JSON string representation of the object
print(AddressChannelDetails.to_json())

# convert the object into a dict
address_channel_details_dict = address_channel_details_instance.to_dict()
# create an instance of AddressChannelDetails from a dict
address_channel_details_from_dict = AddressChannelDetails.from_dict(address_channel_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


