# DdxInteractionsApi::SimpleWorkspaceDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **workspace_id** | **Integer** | Unique identifier for the workspace |  |
| **display_name** | **String** | Display name for the workspace |  |
| **type** | [**WorkspaceTypeDto**](WorkspaceTypeDto.md) |  |  |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::SimpleWorkspaceDto.new(
  workspace_id: null,
  display_name: null,
  type: null
)
```

