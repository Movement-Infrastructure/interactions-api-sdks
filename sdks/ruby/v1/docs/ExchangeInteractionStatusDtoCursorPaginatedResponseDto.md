# DdxInteractionsApi::ExchangeInteractionStatusDtoCursorPaginatedResponseDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **metadata** | [**MinervaMetadataDto**](MinervaMetadataDto.md) |  | [optional] |
| **data** | [**Array&lt;ExchangeInteractionStatusDto&gt;**](ExchangeInteractionStatusDto.md) |  | [optional] |
| **next_cursor** | **String** | Opaque cursor token for fetching the next page. Null if there are no more results. | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::ExchangeInteractionStatusDtoCursorPaginatedResponseDto.new(
  metadata: null,
  data: null,
  next_cursor: null
)
```

