# DdxInteractionsApi::MercuryDestinationVanApiKeyDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **van_api_key_profile_details** | [**VanApiKeyDto**](VanApiKeyDto.md) |  | [optional] |
| **selected_db_mode_access** | [**VanDatabaseMode**](VanDatabaseMode.md) |  | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::MercuryDestinationVanApiKeyDto.new(
  van_api_key_profile_details: null,
  selected_db_mode_access: null
)
```

