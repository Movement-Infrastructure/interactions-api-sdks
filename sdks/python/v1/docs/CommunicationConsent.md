# CommunicationConsent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consent_status** | [**CommunicationConsentStatus**](CommunicationConsentStatus.md) |  | 

## Example

```python
from mig_interactions_api.models.communication_consent import CommunicationConsent

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationConsent from a JSON string
communication_consent_instance = CommunicationConsent.from_json(json)
# print the JSON string representation of the object
print(CommunicationConsent.to_json())

# convert the object into a dict
communication_consent_dict = communication_consent_instance.to_dict()
# create an instance of CommunicationConsent from a dict
communication_consent_from_dict = CommunicationConsent.from_dict(communication_consent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


