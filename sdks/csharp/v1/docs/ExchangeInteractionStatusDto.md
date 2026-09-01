# Ddx.InteractionsApi.Model.ExchangeInteractionStatusDto
Per-interaction status through the Exchange data pipeline.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CorrelationId** | **string** | DDx API request identifier. | [optional] 
**InteractionId** | **Guid?** | The interaction&#39;s unique identifier. | [optional] 
**Status** | **ExchangeInteractionStatus** |  | [optional] 
**ExchangeDataTypes** | **string** | The Exchange data types the interaction was transformed into. | [optional] 
**PublishTime** | **DateTime** | Timestamp when the interaction was received into the Exchange pipeline (Pub/Sub publish time). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

