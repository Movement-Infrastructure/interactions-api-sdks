# Ddx.InteractionsApi.Model.CommunicationConsentOutcomeDetails
Represents a communication consent response (\"opted_in\" or \"opted_out\").

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Operation** | **string** | Describes whether this outcome detail is being created, deleted, or updated. Which operations are accepted varies by outcome type. Defaults to create. | [optional] 
**Type** | **string** | This field categorizes the type of detailed outcome information being provided. | [optional] 
**Value** | [**CommunicationConsent**](CommunicationConsent.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

