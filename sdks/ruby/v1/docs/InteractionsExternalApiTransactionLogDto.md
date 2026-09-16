# DdxInteractionsApi::InteractionsExternalApiTransactionLogDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **response_status_code** | **Integer** | HTTP response code received for external API request. | [optional] |
| **response** | **String** | Response JSON received for external API request. | [optional] |
| **date_created_utc** | **Time** | Timestamp for when the external API request was made. | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::InteractionsExternalApiTransactionLogDto.new(
  response_status_code: null,
  response: null,
  date_created_utc: null
)
```

