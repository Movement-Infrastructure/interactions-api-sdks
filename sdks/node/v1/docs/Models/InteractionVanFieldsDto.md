# InteractionVanFieldsDto
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **contactTypeId** | **String** | VAN contact type ID. Must match a Contact Type accessible to the destination VAN committee.  See https://docs.ngpvan.com/reference/canvassresponsescontacttypes for details on retrieving accessible contact types. | [optional] [default to null] |
| **resultCodeId** | **String** | VAN contact attempt result code, representing the result of that contact attempt. Result code availibility varies based on  contact type, so this value must represent a code that is available to the Contact Type ID specified above.  See https://docs.ngpvan.com/reference/canvassresponsesresultcodes to view Result Codes accessible to the destination VAN committee. | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

