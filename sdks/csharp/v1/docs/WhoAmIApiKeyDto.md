# Ddx.InteractionsApi.Model.WhoAmIApiKeyDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PublicKeyId** | **int** | Unique identifier that specifies which API Key is being used | 
**Source** | [**SimpleMovementAppDto**](SimpleMovementAppDto.md) |  | 
**Workspace** | [**SimpleWorkspaceDto**](SimpleWorkspaceDto.md) |  | 
**ExpireDate** | **DateTime?** | The date and time the API Key is set to expire. The time should be evaluated in Eastern Time. | [optional] 
**Destinations** | [**List&lt;SimpleDestinationDto&gt;**](SimpleDestinationDto.md) | The destinations enabled for this API key | [optional] 
**VanApiKey** | [**MercuryDestinationVanApiKeyDto**](MercuryDestinationVanApiKeyDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

