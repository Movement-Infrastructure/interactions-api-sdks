# InteractionsExternalApiTransactionDto
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **dateCreatedUtc** | **Date** | The UTC date and time at which the request was received. | [optional] [default to null] |
| **interactionId** | **UUID** | ID used to identify the interaction; ID will have been returned from the initial publish response. | [optional] [default to null] |
| **correlationId** | **String** | DDx API request identifier, provided as X-Correlation-Id on interactions responses for use linking all interactions in a request. | [optional] [default to null] |
| **status** | [**ExternalTransactionStatus**](ExternalTransactionStatus.md) |  | [optional] [default to null] |
| **logs** | [**List**](InteractionsExternalApiTransactionLogDto.md) | Any logs associated with this external API transaction. | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

