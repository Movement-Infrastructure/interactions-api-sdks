# DdxInteractionsApi::SimpleDestinationDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **Integer** | Unique identifier for the destination |  |
| **name** | **String** | Display name for the destination | [optional] |
| **is_van_destination** | **Boolean** | Indicator of whether the destination integrates with NGP VAN  and requires an associated VAN External API Key | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::SimpleDestinationDto.new(
  id: null,
  name: null,
  is_van_destination: null
)
```

