# InteractionsExternalApiTransactionDto

For an interaction request with an external destination configured, this represents the status of the interaction data sent to that destination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_created_utc** | **datetime** | The UTC date and time at which the request was received. | [optional] 
**interaction_id** | **str** | ID used to identify the interaction; ID will have been returned from the initial publish response. | [optional] 
**correlation_id** | **str** | DDx API request identifier, provided as X-Correlation-Id on interactions responses for use linking all interactions in a request. | [optional] 
**status** | [**ExternalTransactionStatus**](ExternalTransactionStatus.md) |  | [optional] 
**logs** | [**List[InteractionsExternalApiTransactionLogDto]**](InteractionsExternalApiTransactionLogDto.md) | Any logs associated with this external API transaction. | [optional] 

## Example

```python
from ddx_interactions_api.models.interactions_external_api_transaction_dto import InteractionsExternalApiTransactionDto

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionsExternalApiTransactionDto from a JSON string
interactions_external_api_transaction_dto_instance = InteractionsExternalApiTransactionDto.from_json(json)
# print the JSON string representation of the object
print(InteractionsExternalApiTransactionDto.to_json())

# convert the object into a dict
interactions_external_api_transaction_dto_dict = interactions_external_api_transaction_dto_instance.to_dict()
# create an instance of InteractionsExternalApiTransactionDto from a dict
interactions_external_api_transaction_dto_from_dict = InteractionsExternalApiTransactionDto.from_dict(interactions_external_api_transaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


