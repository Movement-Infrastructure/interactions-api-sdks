# SurveyResponseOutcomeDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Operation** | Pointer to **string** | Describes whether this outcome detail is being created, deleted, or updated. Which operations are accepted varies by outcome type. Defaults to create. | [optional] 
**Type** | Pointer to **string** | This field categorizes the type of detailed outcome information being provided. | [optional] 
**Value** | [**SurveyResponse**](SurveyResponse.md) |  | 

## Methods

### NewSurveyResponseOutcomeDetails

`func NewSurveyResponseOutcomeDetails(value SurveyResponse, ) *SurveyResponseOutcomeDetails`

NewSurveyResponseOutcomeDetails instantiates a new SurveyResponseOutcomeDetails object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSurveyResponseOutcomeDetailsWithDefaults

`func NewSurveyResponseOutcomeDetailsWithDefaults() *SurveyResponseOutcomeDetails`

NewSurveyResponseOutcomeDetailsWithDefaults instantiates a new SurveyResponseOutcomeDetails object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOperation

`func (o *SurveyResponseOutcomeDetails) GetOperation() string`

GetOperation returns the Operation field if non-nil, zero value otherwise.

### GetOperationOk

`func (o *SurveyResponseOutcomeDetails) GetOperationOk() (*string, bool)`

GetOperationOk returns a tuple with the Operation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOperation

`func (o *SurveyResponseOutcomeDetails) SetOperation(v string)`

SetOperation sets Operation field to given value.

### HasOperation

`func (o *SurveyResponseOutcomeDetails) HasOperation() bool`

HasOperation returns a boolean if a field has been set.

### GetType

`func (o *SurveyResponseOutcomeDetails) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *SurveyResponseOutcomeDetails) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *SurveyResponseOutcomeDetails) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *SurveyResponseOutcomeDetails) HasType() bool`

HasType returns a boolean if a field has been set.

### GetValue

`func (o *SurveyResponseOutcomeDetails) GetValue() SurveyResponse`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *SurveyResponseOutcomeDetails) GetValueOk() (*SurveyResponse, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *SurveyResponseOutcomeDetails) SetValue(v SurveyResponse)`

SetValue sets Value field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


