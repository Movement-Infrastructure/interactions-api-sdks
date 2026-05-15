# DynamicChannelDetails

Represents a generic Channel Details object;  does not have any validation rules or JSON format limitations except where noted below.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Optional; unique identifier for any known id for the channel &#x60;type&#x60; | [optional] 
**type** | **str** | Type of the channel specified in &#39;value&#39;. Required when Channel is provided.                Recognized types:  - \&quot;phone_number\&quot;: Indicates &#x60;value&#x60; is a phone number; &#x60;value&#x60; must be in E.164 format (e.g., +14155552671).  - \&quot;email\&quot;: Indicates &#x60;value&#x60; is an email address.  - [any other identifier]: Any type not listed above. &#x60;value&#x60; can be a string, an int or an arbitrary object. | [optional] 
**value** | **object** |  The actual channel used during the outreach attempt. This field can be provided as a string or int though only the object form is shown here.   Examples: +14155552671, name@org.org, @handle.   Required when Channel is provided. | [optional] 

## Example

```python
from mi_interactions_api.models.dynamic_channel_details import DynamicChannelDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicChannelDetails from a JSON string
dynamic_channel_details_instance = DynamicChannelDetails.from_json(json)
# print the JSON string representation of the object
print(DynamicChannelDetails.to_json())

# convert the object into a dict
dynamic_channel_details_dict = dynamic_channel_details_instance.to_dict()
# create an instance of DynamicChannelDetails from a dict
dynamic_channel_details_from_dict = DynamicChannelDetails.from_dict(dynamic_channel_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


