# CommunicationConsentOutcomeDetails

Represents a communication consent response (\"opted_in\" or \"opted_out\").

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | Describes whether this outcome detail is being created, deleted, or updated. Which operations are accepted varies by outcome type. Defaults to create. | [optional] 
**type** | **str** | This field categorizes the type of detailed outcome information being provided. | [optional] 
**value** | [**CommunicationConsent**](CommunicationConsent.md) |  | 

## Example

```python
from mig_interactions_api.models.communication_consent_outcome_details import CommunicationConsentOutcomeDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationConsentOutcomeDetails from a JSON string
communication_consent_outcome_details_instance = CommunicationConsentOutcomeDetails.from_json(json)
# print the JSON string representation of the object
print(CommunicationConsentOutcomeDetails.to_json())

# convert the object into a dict
communication_consent_outcome_details_dict = communication_consent_outcome_details_instance.to_dict()
# create an instance of CommunicationConsentOutcomeDetails from a dict
communication_consent_outcome_details_from_dict = CommunicationConsentOutcomeDetails.from_dict(communication_consent_outcome_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


