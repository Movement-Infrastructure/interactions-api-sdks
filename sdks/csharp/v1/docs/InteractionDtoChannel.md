# Ddx.InteractionsApi.Model.InteractionDtoChannel
Channel-of-contact details used during the outreach attempt.  If the `type` is recognized as an Address Channel (type = \"address\"), the `value` will be deserialized to that object type.  Other string-based types have specific validation documented in the \"Channel\" section below, like \"phone_number\".  If the `type` is unrecognized, the payload will be deserialized to an unvalidated, loosely typed object for flexibility.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | 
**Value** | **Object** |  | 
**Id** | **string** | Optional; unique identifier for any known id for the channel &#x60;type&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

