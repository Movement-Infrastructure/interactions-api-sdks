# Address


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line1** | **str** | The primary street address (e.g., house number and street name). | 
**address_line2** | **str** | The secondary address information (e.g., apartment, suite, unit number). | [optional] 
**city** | **str** | The city of the address. | 
**state** | **str** | The state or region of the address. | 
**postal_code** | **str** | The postal (ZIP) code for the address. Can accept ZIP5, ZIP+4, or ZIP9 format. | 

## Example

```python
from mi_interactions_api.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


