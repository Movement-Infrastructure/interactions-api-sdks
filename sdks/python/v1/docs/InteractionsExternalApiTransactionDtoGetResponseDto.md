# InteractionsExternalApiTransactionDtoGetResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**MinervaMetadataDto**](MinervaMetadataDto.md) |  | [optional] 
**data** | [**List[InteractionsExternalApiTransactionDto]**](InteractionsExternalApiTransactionDto.md) |  | [optional] 

## Example

```python
from ddx_interactions_api.models.interactions_external_api_transaction_dto_get_response_dto import InteractionsExternalApiTransactionDtoGetResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionsExternalApiTransactionDtoGetResponseDto from a JSON string
interactions_external_api_transaction_dto_get_response_dto_instance = InteractionsExternalApiTransactionDtoGetResponseDto.from_json(json)
# print the JSON string representation of the object
print(InteractionsExternalApiTransactionDtoGetResponseDto.to_json())

# convert the object into a dict
interactions_external_api_transaction_dto_get_response_dto_dict = interactions_external_api_transaction_dto_get_response_dto_instance.to_dict()
# create an instance of InteractionsExternalApiTransactionDtoGetResponseDto from a dict
interactions_external_api_transaction_dto_get_response_dto_from_dict = InteractionsExternalApiTransactionDtoGetResponseDto.from_dict(interactions_external_api_transaction_dto_get_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


