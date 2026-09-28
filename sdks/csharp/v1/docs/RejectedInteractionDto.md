# Ddx.InteractionsApi.Model.RejectedInteractionDto
Represents a rejected interaction with its associated errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InteractionId** | **Guid** | ID used to identify the interaction; ID will have been returned from the initial publish response. | [optional] 
**Index** | **int** | Index of the rejected interaction in the batch. | [optional] 
**Errors** | [**List&lt;InteractionErrorDto&gt;**](InteractionErrorDto.md) | List of errors associated with the rejected interaction. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

