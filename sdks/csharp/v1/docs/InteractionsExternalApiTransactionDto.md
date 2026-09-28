# Ddx.InteractionsApi.Model.InteractionsExternalApiTransactionDto
For an interaction request with an external destination configured, this represents the status of the interaction data sent to that destination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DateCreatedUtc** | **DateTime** | The UTC date and time at which the request was received. | [optional] 
**InteractionId** | **Guid** | ID used to identify the interaction; ID will have been returned from the initial publish response. | [optional] 
**CorrelationId** | **string** | DDx API request identifier, provided as X-Correlation-Id on interactions responses for use linking all interactions in a request. | [optional] 
**Status** | **ExternalTransactionStatus** |  | [optional] 
**Logs** | [**List&lt;InteractionsExternalApiTransactionLogDto&gt;**](InteractionsExternalApiTransactionLogDto.md) | Any logs associated with this external API transaction. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

