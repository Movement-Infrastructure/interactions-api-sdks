# InteractionsBatchResultDto
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **correlationId** | **String** | DDx API request identifier, provided as X-Correlation-Id on interactions responses for use linking all interactions in a request. | [optional] [default to null] |
| **totalInteractions** | **Integer** | Total number of interactions in the batch. | [optional] [default to null] |
| **acceptedInteractions** | [**AcceptedInteractionsDto**](AcceptedInteractionsDto.md) |  | [optional] [default to null] |
| **rejectedInteractions** | [**RejectedInteractionsDto**](RejectedInteractionsDto.md) |  | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

