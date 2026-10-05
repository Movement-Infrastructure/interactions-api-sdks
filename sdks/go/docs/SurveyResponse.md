# SurveyResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**QuestionId** | Pointer to **NullableString** | Unique identifier for the survey question being asked;  the value may be retrieved from the system that sourced the question | [optional] 
**QuestionText** | **string** | The question text presented during an interaction | 
**ResponseId** | Pointer to **NullableString** | Unique identifier for the survey response associated with the question;  the value may be retrieved from the system that sourced the question | [optional] 
**ResponseText** | **string** | An answer to the question.  Required when Survey Question text is provided. | 

## Methods

### NewSurveyResponse

`func NewSurveyResponse(questionText string, responseText string, ) *SurveyResponse`

NewSurveyResponse instantiates a new SurveyResponse object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSurveyResponseWithDefaults

`func NewSurveyResponseWithDefaults() *SurveyResponse`

NewSurveyResponseWithDefaults instantiates a new SurveyResponse object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetQuestionId

`func (o *SurveyResponse) GetQuestionId() string`

GetQuestionId returns the QuestionId field if non-nil, zero value otherwise.

### GetQuestionIdOk

`func (o *SurveyResponse) GetQuestionIdOk() (*string, bool)`

GetQuestionIdOk returns a tuple with the QuestionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQuestionId

`func (o *SurveyResponse) SetQuestionId(v string)`

SetQuestionId sets QuestionId field to given value.

### HasQuestionId

`func (o *SurveyResponse) HasQuestionId() bool`

HasQuestionId returns a boolean if a field has been set.

### SetQuestionIdNil

`func (o *SurveyResponse) SetQuestionIdNil(b bool)`

 SetQuestionIdNil sets the value for QuestionId to be an explicit nil

### UnsetQuestionId
`func (o *SurveyResponse) UnsetQuestionId()`

UnsetQuestionId ensures that no value is present for QuestionId, not even an explicit nil
### GetQuestionText

`func (o *SurveyResponse) GetQuestionText() string`

GetQuestionText returns the QuestionText field if non-nil, zero value otherwise.

### GetQuestionTextOk

`func (o *SurveyResponse) GetQuestionTextOk() (*string, bool)`

GetQuestionTextOk returns a tuple with the QuestionText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetQuestionText

`func (o *SurveyResponse) SetQuestionText(v string)`

SetQuestionText sets QuestionText field to given value.


### GetResponseId

`func (o *SurveyResponse) GetResponseId() string`

GetResponseId returns the ResponseId field if non-nil, zero value otherwise.

### GetResponseIdOk

`func (o *SurveyResponse) GetResponseIdOk() (*string, bool)`

GetResponseIdOk returns a tuple with the ResponseId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseId

`func (o *SurveyResponse) SetResponseId(v string)`

SetResponseId sets ResponseId field to given value.

### HasResponseId

`func (o *SurveyResponse) HasResponseId() bool`

HasResponseId returns a boolean if a field has been set.

### SetResponseIdNil

`func (o *SurveyResponse) SetResponseIdNil(b bool)`

 SetResponseIdNil sets the value for ResponseId to be an explicit nil

### UnsetResponseId
`func (o *SurveyResponse) UnsetResponseId()`

UnsetResponseId ensures that no value is present for ResponseId, not even an explicit nil
### GetResponseText

`func (o *SurveyResponse) GetResponseText() string`

GetResponseText returns the ResponseText field if non-nil, zero value otherwise.

### GetResponseTextOk

`func (o *SurveyResponse) GetResponseTextOk() (*string, bool)`

GetResponseTextOk returns a tuple with the ResponseText field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseText

`func (o *SurveyResponse) SetResponseText(v string)`

SetResponseText sets ResponseText field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


