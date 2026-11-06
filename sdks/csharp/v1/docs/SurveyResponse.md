# Ddx.InteractionsApi.Model.SurveyResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**QuestionId** | **string** | Unique identifier for the survey question being asked;  the value may be retrieved from the system that sourced the question.  Must be an integer when VAN or DDx Exchange is a destination. | [optional] 
**QuestionText** | **string** | The question text presented during an interaction | 
**ResponseId** | **string** | Unique identifier for the survey response associated with the question;  the value may be retrieved from the system that sourced the question.  Must be an integer when VAN or DDx Exchange is a destination. | [optional] 
**ResponseText** | **string** | An answer to the question.  Required when Survey Question text is provided. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

