# SimpleWorkspaceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workspace_id** | **int** | Unique identifier for the workspace | 
**display_name** | **str** | Display name for the workspace | 
**type** | [**WorkspaceTypeDto**](WorkspaceTypeDto.md) |  | 

## Example

```python
from mig_interactions_api.models.simple_workspace_dto import SimpleWorkspaceDto

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleWorkspaceDto from a JSON string
simple_workspace_dto_instance = SimpleWorkspaceDto.from_json(json)
# print the JSON string representation of the object
print(SimpleWorkspaceDto.to_json())

# convert the object into a dict
simple_workspace_dto_dict = simple_workspace_dto_instance.to_dict()
# create an instance of SimpleWorkspaceDto from a dict
simple_workspace_dto_from_dict = SimpleWorkspaceDto.from_dict(simple_workspace_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


