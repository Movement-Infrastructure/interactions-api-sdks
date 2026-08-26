# CommitteeDetails

Represents details for the entities that conducted or logged the outreach attempt.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the committee identifier specified in &#39;id&#39;, representing the source context of the interaction. | 
**id** | **str** | The actual committee identifier itself. | 

## Example

```python
from ddx_interactions_api.models.committee_details import CommitteeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CommitteeDetails from a JSON string
committee_details_instance = CommitteeDetails.from_json(json)
# print the JSON string representation of the object
print(CommitteeDetails.to_json())

# convert the object into a dict
committee_details_dict = committee_details_instance.to_dict()
# create an instance of CommitteeDetails from a dict
committee_details_from_dict = CommitteeDetails.from_dict(committee_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


