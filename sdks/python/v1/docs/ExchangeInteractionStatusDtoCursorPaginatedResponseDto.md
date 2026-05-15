# ExchangeInteractionStatusDtoCursorPaginatedResponseDto

Extends Minerva.Dto.Api.GetResponseDto`1 with cursor-based pagination support.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**MinervaMetadataDto**](MinervaMetadataDto.md) |  | [optional] 
**data** | [**List[ExchangeInteractionStatusDto]**](ExchangeInteractionStatusDto.md) |  | [optional] 
**next_cursor** | **str** | Opaque cursor token for fetching the next page. Null if there are no more results. | [optional] 

## Example

```python
from mi_interactions_api.models.exchange_interaction_status_dto_cursor_paginated_response_dto import ExchangeInteractionStatusDtoCursorPaginatedResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeInteractionStatusDtoCursorPaginatedResponseDto from a JSON string
exchange_interaction_status_dto_cursor_paginated_response_dto_instance = ExchangeInteractionStatusDtoCursorPaginatedResponseDto.from_json(json)
# print the JSON string representation of the object
print(ExchangeInteractionStatusDtoCursorPaginatedResponseDto.to_json())

# convert the object into a dict
exchange_interaction_status_dto_cursor_paginated_response_dto_dict = exchange_interaction_status_dto_cursor_paginated_response_dto_instance.to_dict()
# create an instance of ExchangeInteractionStatusDtoCursorPaginatedResponseDto from a dict
exchange_interaction_status_dto_cursor_paginated_response_dto_from_dict = ExchangeInteractionStatusDtoCursorPaginatedResponseDto.from_dict(exchange_interaction_status_dto_cursor_paginated_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


