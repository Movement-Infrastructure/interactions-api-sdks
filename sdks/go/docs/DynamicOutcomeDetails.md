# DynamicOutcomeDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Operation** | Pointer to [**OutcomeDetailOperation**](OutcomeDetailOperation.md) |  | [optional] 
**Type** | Pointer to **string** | This field categorizes the type of detailed outcome information being provided. | [optional] 
**Value** | Pointer to **interface{}** |  Provide additional details of the outreach attempt. This field can be provided as a string or int though only the object form is shown here. | [optional] 

## Methods

### NewDynamicOutcomeDetails

`func NewDynamicOutcomeDetails() *DynamicOutcomeDetails`

NewDynamicOutcomeDetails instantiates a new DynamicOutcomeDetails object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDynamicOutcomeDetailsWithDefaults

`func NewDynamicOutcomeDetailsWithDefaults() *DynamicOutcomeDetails`

NewDynamicOutcomeDetailsWithDefaults instantiates a new DynamicOutcomeDetails object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetOperation

`func (o *DynamicOutcomeDetails) GetOperation() OutcomeDetailOperation`

GetOperation returns the Operation field if non-nil, zero value otherwise.

### GetOperationOk

`func (o *DynamicOutcomeDetails) GetOperationOk() (*OutcomeDetailOperation, bool)`

GetOperationOk returns a tuple with the Operation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOperation

`func (o *DynamicOutcomeDetails) SetOperation(v OutcomeDetailOperation)`

SetOperation sets Operation field to given value.

### HasOperation

`func (o *DynamicOutcomeDetails) HasOperation() bool`

HasOperation returns a boolean if a field has been set.

### GetType

`func (o *DynamicOutcomeDetails) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *DynamicOutcomeDetails) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *DynamicOutcomeDetails) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *DynamicOutcomeDetails) HasType() bool`

HasType returns a boolean if a field has been set.

### GetValue

`func (o *DynamicOutcomeDetails) GetValue() interface{}`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *DynamicOutcomeDetails) GetValueOk() (*interface{}, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *DynamicOutcomeDetails) SetValue(v interface{})`

SetValue sets Value field to given value.

### HasValue

`func (o *DynamicOutcomeDetails) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValueNil

`func (o *DynamicOutcomeDetails) SetValueNil(b bool)`

 SetValueNil sets the value for Value to be an explicit nil

### UnsetValue
`func (o *DynamicOutcomeDetails) UnsetValue()`

UnsetValue ensures that no value is present for Value, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


