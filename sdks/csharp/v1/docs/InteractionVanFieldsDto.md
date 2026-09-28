# Ddx.InteractionsApi.Model.InteractionVanFieldsDto
VAN-specific data for an interaction. Must be provided if if the Interactions API Key used on the request  is configured with VAN as a destination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ContactTypeId** | **string** | VAN contact type ID. Must match a Contact Type accessible to the destination VAN committee.  See https://docs.ngpvan.com/reference/canvassresponsescontacttypes for details on retrieving accessible contact types. | [optional] 
**ResultCodeId** | **string** | VAN contact attempt result code, representing the result of that contact attempt. Result code availibility varies based on  contact type, so this value must represent a code that is available to the Contact Type ID specified above.  See https://docs.ngpvan.com/reference/canvassresponsesresultcodes to view Result Codes accessible to the destination VAN committee. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

