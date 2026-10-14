# RejectedInteractionsDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Count** | Pointer to **int32** | The total number of rejected interactions. | [optional] 
**Data** | Pointer to [**[]RejectedInteractionDto**](RejectedInteractionDto.md) | The list of rejected interactions. | [optional] 

## Methods

### NewRejectedInteractionsDto

`func NewRejectedInteractionsDto() *RejectedInteractionsDto`

NewRejectedInteractionsDto instantiates a new RejectedInteractionsDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRejectedInteractionsDtoWithDefaults

`func NewRejectedInteractionsDtoWithDefaults() *RejectedInteractionsDto`

NewRejectedInteractionsDtoWithDefaults instantiates a new RejectedInteractionsDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCount

`func (o *RejectedInteractionsDto) GetCount() int32`

GetCount returns the Count field if non-nil, zero value otherwise.

### GetCountOk

`func (o *RejectedInteractionsDto) GetCountOk() (*int32, bool)`

GetCountOk returns a tuple with the Count field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCount

`func (o *RejectedInteractionsDto) SetCount(v int32)`

SetCount sets Count field to given value.

### HasCount

`func (o *RejectedInteractionsDto) HasCount() bool`

HasCount returns a boolean if a field has been set.

### GetData

`func (o *RejectedInteractionsDto) GetData() []RejectedInteractionDto`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *RejectedInteractionsDto) GetDataOk() (*[]RejectedInteractionDto, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *RejectedInteractionsDto) SetData(v []RejectedInteractionDto)`

SetData sets Data field to given value.

### HasData

`func (o *RejectedInteractionsDto) HasData() bool`

HasData returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


