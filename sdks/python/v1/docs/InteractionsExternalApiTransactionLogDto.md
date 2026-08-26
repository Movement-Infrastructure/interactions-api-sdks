# InteractionsExternalApiTransactionLogDto

Log data for an external API transaction to a configured Interactions API destination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_status_code** | **int** | HTTP response code received for external API request. | [optional] 
**response** | **str** | Response JSON received for external API request. | [optional] 
**date_created_utc** | **datetime** | Timestamp for when the external API request was made. | [optional] 

## Example

```python
from mig_interactions_api.models.interactions_external_api_transaction_log_dto import InteractionsExternalApiTransactionLogDto

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionsExternalApiTransactionLogDto from a JSON string
interactions_external_api_transaction_log_dto_instance = InteractionsExternalApiTransactionLogDto.from_json(json)
# print the JSON string representation of the object
print(InteractionsExternalApiTransactionLogDto.to_json())

# convert the object into a dict
interactions_external_api_transaction_log_dto_dict = interactions_external_api_transaction_log_dto_instance.to_dict()
# create an instance of InteractionsExternalApiTransactionLogDto from a dict
interactions_external_api_transaction_log_dto_from_dict = InteractionsExternalApiTransactionLogDto.from_dict(interactions_external_api_transaction_log_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


