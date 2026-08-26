# InteractionsBatchResultDto

Represents the result of processing a batch of interactions, including accepted and rejected interactions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | DDx API request identifier, provided as X-Correlation-Id on interactions responses for use linking all interactions in a request. | [optional] 
**total_interactions** | **int** | Total number of interactions in the batch. | [optional] 
**accepted_interactions** | [**AcceptedInteractionsDto**](AcceptedInteractionsDto.md) |  | [optional] 
**rejected_interactions** | [**RejectedInteractionsDto**](RejectedInteractionsDto.md) |  | [optional] 

## Example

```python
from mig_interactions_api.models.interactions_batch_result_dto import InteractionsBatchResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionsBatchResultDto from a JSON string
interactions_batch_result_dto_instance = InteractionsBatchResultDto.from_json(json)
# print the JSON string representation of the object
print(InteractionsBatchResultDto.to_json())

# convert the object into a dict
interactions_batch_result_dto_dict = interactions_batch_result_dto_instance.to_dict()
# create an instance of InteractionsBatchResultDto from a dict
interactions_batch_result_dto_from_dict = InteractionsBatchResultDto.from_dict(interactions_batch_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


