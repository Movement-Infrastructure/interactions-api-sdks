# ContactInfo

Represents contact information for a person being interacted with, including email, phone, or address.  Can be used to match a person if an Id is not known

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **List[str]** | Email addresses of the person being interacted with. | [optional] 
**phone** | **List[str]** | Phone numbers of the person being interacted with. Should be in E.164 format (e.g. +1234567890). | [optional] 
**address** | [**List[Address]**](Address.md) | Physical addresses of the person being interacted with. | [optional] 
**first_name** | **str** | Optional first name field for person being interacted with. | [optional] 
**middle_name** | **str** | Optional middle name field for person being interacted with. | [optional] 
**last_name** | **str** | Optional last name field for person being interacted with. | [optional] 
**social_handle** | **List[str]** | Optional social media handles for person being interacted with. | [optional] 

## Example

```python
from mig_interactions_api.models.contact_info import ContactInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContactInfo from a JSON string
contact_info_instance = ContactInfo.from_json(json)
# print the JSON string representation of the object
print(ContactInfo.to_json())

# convert the object into a dict
contact_info_dict = contact_info_instance.to_dict()
# create an instance of ContactInfo from a dict
contact_info_from_dict = ContactInfo.from_dict(contact_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


