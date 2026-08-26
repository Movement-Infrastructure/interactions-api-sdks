# CanvasserDetails

Represents canvasser details for the individual who conducted the outreach attempt.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the canvasser identifier specified in &#39;id&#39;.  Required when Canvasser is provided. | 
**id** | **str** | The actual canvasser identifier used during the outreach attempt.  Examples: user ID, employee number, volunteer ID, etc.  Required when Canvasser is provided. | 

## Example

```python
from ddx_interactions_api.models.canvasser_details import CanvasserDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CanvasserDetails from a JSON string
canvasser_details_instance = CanvasserDetails.from_json(json)
# print the JSON string representation of the object
print(CanvasserDetails.to_json())

# convert the object into a dict
canvasser_details_dict = canvasser_details_instance.to_dict()
# create an instance of CanvasserDetails from a dict
canvasser_details_from_dict = CanvasserDetails.from_dict(canvasser_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


