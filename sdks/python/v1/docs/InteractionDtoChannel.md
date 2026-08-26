# InteractionDtoChannel

Channel-of-contact details used during the outreach attempt.  If the `type` is recognized as an Address Channel (type = \"address\"), the `value` will be deserialized to that object type.  Other string-based types have specific validation documented in the \"Channel\" section below, like \"phone_number\".  If the `type` is unrecognized, the payload will be deserialized to an unvalidated, loosely typed object for flexibility.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **object** |  | 
**id** | **str** | Optional; unique identifier for any known id for the channel &#x60;type&#x60; | [optional] 

## Example

```python
from ddx_interactions_api.models.interaction_dto_channel import InteractionDtoChannel

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionDtoChannel from a JSON string
interaction_dto_channel_instance = InteractionDtoChannel.from_json(json)
# print the JSON string representation of the object
print(InteractionDtoChannel.to_json())

# convert the object into a dict
interaction_dto_channel_dict = interaction_dto_channel_instance.to_dict()
# create an instance of InteractionDtoChannel from a dict
interaction_dto_channel_from_dict = InteractionDtoChannel.from_dict(interaction_dto_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


