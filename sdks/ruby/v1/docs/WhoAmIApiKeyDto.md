# DdxInteractionsApi::WhoAmIApiKeyDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **public_key_id** | **Integer** | Unique identifier that specifies which API Key is being used |  |
| **source** | [**SimpleMovementAppDto**](SimpleMovementAppDto.md) |  |  |
| **workspace** | [**SimpleWorkspaceDto**](SimpleWorkspaceDto.md) |  |  |
| **expire_date** | **Time** | The date and time the API Key is set to expire. The time should be evaluated in Eastern Time. | [optional] |
| **destinations** | [**Array&lt;SimpleDestinationDto&gt;**](SimpleDestinationDto.md) | The destinations enabled for this API key | [optional] |
| **van_api_key** | [**MercuryDestinationVanApiKeyDto**](MercuryDestinationVanApiKeyDto.md) |  | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::WhoAmIApiKeyDto.new(
  public_key_id: null,
  source: null,
  workspace: null,
  expire_date: null,
  destinations: null,
  van_api_key: null
)
```

