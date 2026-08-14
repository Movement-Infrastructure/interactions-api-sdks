# ExchangeInteractionStatusDto

Per-interaction status through the Exchange data pipeline.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | DDx API request identifier. | [optional] 
**interaction_id** | **str** | The interaction&#39;s unique identifier. | [optional] 
**status** | [**ExchangeInteractionStatus**](ExchangeInteractionStatus.md) |  | [optional] 
**publish_time** | **datetime** | Timestamp when the interaction was received into the Exchange pipeline (Pub/Sub publish time). | [optional] 

## Example

```python
from mig_interactions_api.models.exchange_interaction_status_dto import ExchangeInteractionStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeInteractionStatusDto from a JSON string
exchange_interaction_status_dto_instance = ExchangeInteractionStatusDto.from_json(json)
# print the JSON string representation of the object
print(ExchangeInteractionStatusDto.to_json())

# convert the object into a dict
exchange_interaction_status_dto_dict = exchange_interaction_status_dto_instance.to_dict()
# create an instance of ExchangeInteractionStatusDto from a dict
exchange_interaction_status_dto_from_dict = ExchangeInteractionStatusDto.from_dict(exchange_interaction_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


