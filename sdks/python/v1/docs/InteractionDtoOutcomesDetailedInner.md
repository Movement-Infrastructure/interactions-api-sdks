# InteractionDtoOutcomesDetailedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | This field categorizes the type of detailed outcome information being provided. | 
**value** | **object** |  | 
**operation** | [**OutcomeDetailOperation**](OutcomeDetailOperation.md) |  | [optional] 

## Example

```python
from mig_interactions_api.models.interaction_dto_outcomes_detailed_inner import InteractionDtoOutcomesDetailedInner

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionDtoOutcomesDetailedInner from a JSON string
interaction_dto_outcomes_detailed_inner_instance = InteractionDtoOutcomesDetailedInner.from_json(json)
# print the JSON string representation of the object
print(InteractionDtoOutcomesDetailedInner.to_json())

# convert the object into a dict
interaction_dto_outcomes_detailed_inner_dict = interaction_dto_outcomes_detailed_inner_instance.to_dict()
# create an instance of InteractionDtoOutcomesDetailedInner from a dict
interaction_dto_outcomes_detailed_inner_from_dict = InteractionDtoOutcomesDetailedInner.from_dict(interaction_dto_outcomes_detailed_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


