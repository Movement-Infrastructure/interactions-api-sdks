# ActivistCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activist_code_id** | **str** | Unique identifier for an activist code;  the value may be retrieved from the system that sourced the activist code | [optional] 
**text** | **str** | The question or information prompted during the interaction | 

## Example

```python
from mig_interactions_api.models.activist_code import ActivistCode

# TODO update the JSON string below
json = "{}"
# create an instance of ActivistCode from a JSON string
activist_code_instance = ActivistCode.from_json(json)
# print the JSON string representation of the object
print(ActivistCode.to_json())

# convert the object into a dict
activist_code_dict = activist_code_instance.to_dict()
# create an instance of ActivistCode from a dict
activist_code_from_dict = ActivistCode.from_dict(activist_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


