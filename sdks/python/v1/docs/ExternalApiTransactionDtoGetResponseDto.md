# ExternalApiTransactionDtoGetResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**MinervaMetadataDto**](MinervaMetadataDto.md) |  | [optional] 
**data** | [**List[ExternalApiTransactionDto]**](ExternalApiTransactionDto.md) |  | [optional] 

## Example

```python
from mig_interactions_api.models.external_api_transaction_dto_get_response_dto import ExternalApiTransactionDtoGetResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalApiTransactionDtoGetResponseDto from a JSON string
external_api_transaction_dto_get_response_dto_instance = ExternalApiTransactionDtoGetResponseDto.from_json(json)
# print the JSON string representation of the object
print(ExternalApiTransactionDtoGetResponseDto.to_json())

# convert the object into a dict
external_api_transaction_dto_get_response_dto_dict = external_api_transaction_dto_get_response_dto_instance.to_dict()
# create an instance of ExternalApiTransactionDtoGetResponseDto from a dict
external_api_transaction_dto_get_response_dto_from_dict = ExternalApiTransactionDtoGetResponseDto.from_dict(external_api_transaction_dto_get_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


