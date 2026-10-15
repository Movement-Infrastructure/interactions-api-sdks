# RejectedInteractionDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InteractionId** | Pointer to **string** | ID used to identify the interaction; ID will have been returned from the initial publish response. | [optional] 
**Index** | Pointer to **int32** | Index of the rejected interaction in the batch. | [optional] 
**Errors** | Pointer to [**[]InteractionErrorDto**](InteractionErrorDto.md) | List of errors associated with the rejected interaction. | [optional] 

## Methods

### NewRejectedInteractionDto

`func NewRejectedInteractionDto() *RejectedInteractionDto`

NewRejectedInteractionDto instantiates a new RejectedInteractionDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewRejectedInteractionDtoWithDefaults

`func NewRejectedInteractionDtoWithDefaults() *RejectedInteractionDto`

NewRejectedInteractionDtoWithDefaults instantiates a new RejectedInteractionDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInteractionId

`func (o *RejectedInteractionDto) GetInteractionId() string`

GetInteractionId returns the InteractionId field if non-nil, zero value otherwise.

### GetInteractionIdOk

`func (o *RejectedInteractionDto) GetInteractionIdOk() (*string, bool)`

GetInteractionIdOk returns a tuple with the InteractionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInteractionId

`func (o *RejectedInteractionDto) SetInteractionId(v string)`

SetInteractionId sets InteractionId field to given value.

### HasInteractionId

`func (o *RejectedInteractionDto) HasInteractionId() bool`

HasInteractionId returns a boolean if a field has been set.

### GetIndex

`func (o *RejectedInteractionDto) GetIndex() int32`

GetIndex returns the Index field if non-nil, zero value otherwise.

### GetIndexOk

`func (o *RejectedInteractionDto) GetIndexOk() (*int32, bool)`

GetIndexOk returns a tuple with the Index field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIndex

`func (o *RejectedInteractionDto) SetIndex(v int32)`

SetIndex sets Index field to given value.

### HasIndex

`func (o *RejectedInteractionDto) HasIndex() bool`

HasIndex returns a boolean if a field has been set.

### GetErrors

`func (o *RejectedInteractionDto) GetErrors() []InteractionErrorDto`

GetErrors returns the Errors field if non-nil, zero value otherwise.

### GetErrorsOk

`func (o *RejectedInteractionDto) GetErrorsOk() (*[]InteractionErrorDto, bool)`

GetErrorsOk returns a tuple with the Errors field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetErrors

`func (o *RejectedInteractionDto) SetErrors(v []InteractionErrorDto)`

SetErrors sets Errors field to given value.

### HasErrors

`func (o *RejectedInteractionDto) HasErrors() bool`

HasErrors returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


