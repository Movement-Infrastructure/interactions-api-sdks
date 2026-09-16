# DdxInteractionsApi::VanApiKeyDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **external_api_key_id** | **Integer** |  | [optional] |
| **type** | [**ExternalApiKeyType**](ExternalApiKeyType.md) |  | [optional] |
| **status** | [**ExternalApiKeyStatus**](ExternalApiKeyStatus.md) |  | [optional] |
| **name** | **String** |  | [optional] |
| **date_created** | **Time** |  | [optional] |
| **connections** | **Integer** |  | [optional] |
| **committee_name** | **String** |  | [optional] |
| **has_my_voters** | **Boolean** |  | [optional] |
| **has_my_campaign** | **Boolean** |  | [optional] |
| **key_ref** | **String** |  | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::VanApiKeyDto.new(
  external_api_key_id: null,
  type: null,
  status: null,
  name: null,
  date_created: null,
  connections: null,
  committee_name: null,
  has_my_voters: null,
  has_my_campaign: null,
  key_ref: null
)
```

