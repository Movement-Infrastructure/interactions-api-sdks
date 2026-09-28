# ExchangeInteractionStatusDto
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **correlationId** | **String** | DDx API request identifier. | [optional] [default to null] |
| **interactionId** | **UUID** | The interaction&#39;s unique identifier. | [optional] [default to null] |
| **status** | [**ExchangeInteractionStatus**](ExchangeInteractionStatus.md) |  | [optional] [default to null] |
| **exchangeDataTypes** | **String** | The Exchange data types the interaction was transformed into. | [optional] [default to null] |
| **publishTime** | **Date** | Timestamp when the interaction was received into the Exchange pipeline (Pub/Sub publish time). | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

