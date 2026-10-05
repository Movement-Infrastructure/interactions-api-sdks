# ActivistCode

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ActivistCodeId** | Pointer to **NullableString** | Unique identifier for an activist code;  the value may be retrieved from the system that sourced the activist code | [optional] 
**Text** | **string** | The question or information prompted during the interaction | 

## Methods

### NewActivistCode

`func NewActivistCode(text string, ) *ActivistCode`

NewActivistCode instantiates a new ActivistCode object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewActivistCodeWithDefaults

`func NewActivistCodeWithDefaults() *ActivistCode`

NewActivistCodeWithDefaults instantiates a new ActivistCode object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetActivistCodeId

`func (o *ActivistCode) GetActivistCodeId() string`

GetActivistCodeId returns the ActivistCodeId field if non-nil, zero value otherwise.

### GetActivistCodeIdOk

`func (o *ActivistCode) GetActivistCodeIdOk() (*string, bool)`

GetActivistCodeIdOk returns a tuple with the ActivistCodeId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetActivistCodeId

`func (o *ActivistCode) SetActivistCodeId(v string)`

SetActivistCodeId sets ActivistCodeId field to given value.

### HasActivistCodeId

`func (o *ActivistCode) HasActivistCodeId() bool`

HasActivistCodeId returns a boolean if a field has been set.

### SetActivistCodeIdNil

`func (o *ActivistCode) SetActivistCodeIdNil(b bool)`

 SetActivistCodeIdNil sets the value for ActivistCodeId to be an explicit nil

### UnsetActivistCodeId
`func (o *ActivistCode) UnsetActivistCodeId()`

UnsetActivistCodeId ensures that no value is present for ActivistCodeId, not even an explicit nil
### GetText

`func (o *ActivistCode) GetText() string`

GetText returns the Text field if non-nil, zero value otherwise.

### GetTextOk

`func (o *ActivistCode) GetTextOk() (*string, bool)`

GetTextOk returns a tuple with the Text field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetText

`func (o *ActivistCode) SetText(v string)`

SetText sets Text field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


