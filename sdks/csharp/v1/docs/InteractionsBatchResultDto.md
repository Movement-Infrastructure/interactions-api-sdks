# Ddx.InteractionsApi.Model.InteractionsBatchResultDto
Represents the result of processing a batch of interactions, including accepted and rejected interactions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CorrelationId** | **string** | DDx API request identifier, provided as X-Correlation-Id on interactions responses for use linking all interactions in a request. | [optional] 
**TotalInteractions** | **int** | Total number of interactions in the batch. | [optional] 
**AcceptedInteractions** | [**AcceptedInteractionsDto**](AcceptedInteractionsDto.md) |  | [optional] 
**RejectedInteractions** | [**RejectedInteractionsDto**](RejectedInteractionsDto.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

