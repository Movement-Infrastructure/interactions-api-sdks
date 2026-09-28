# Ddx.InteractionsApi.Model.ContactInfo
Represents contact information for a person being interacted with, including email, phone, or address.  Can be used to match a person if an Id is not known

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Email** | **List&lt;string&gt;** | Email addresses of the person being interacted with. | [optional] 
**Phone** | **List&lt;string&gt;** | Phone numbers of the person being interacted with. Should be in E.164 format (e.g. +1234567890). | [optional] 
**Address** | [**List&lt;Address&gt;**](Address.md) | Physical addresses of the person being interacted with. | [optional] 
**FirstName** | **string** | Optional first name field for person being interacted with. | [optional] 
**MiddleName** | **string** | Optional middle name field for person being interacted with. | [optional] 
**LastName** | **string** | Optional last name field for person being interacted with. | [optional] 
**SocialHandle** | **List&lt;string&gt;** | Optional social media handles for person being interacted with. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

