# WhoAmIApiKeyDto
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **publicKeyId** | **Integer** | Unique identifier that specifies which API Key is being used | [default to null] |
| **source** | [**SimpleMovementAppDto**](SimpleMovementAppDto.md) |  | [default to null] |
| **workspace** | [**SimpleWorkspaceDto**](SimpleWorkspaceDto.md) |  | [default to null] |
| **expireDate** | **Date** | The date and time the API Key is set to expire. The time should be evaluated in Eastern Time. | [optional] [default to null] |
| **destinations** | [**List**](SimpleDestinationDto.md) | The destinations enabled for this API key | [optional] [default to null] |
| **vanApiKey** | [**MercuryDestinationVanApiKeyDto**](MercuryDestinationVanApiKeyDto.md) |  | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

