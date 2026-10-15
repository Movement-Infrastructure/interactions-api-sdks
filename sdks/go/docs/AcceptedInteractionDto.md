# AcceptedInteractionDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InteractionId** | Pointer to **string** | ID used to identify the interaction; ID will have been returned from the initial publish response. | [optional] 
**Index** | Pointer to **int32** | Index of the accepted interaction in the batch. | [optional] 

## Methods

### NewAcceptedInteractionDto

`func NewAcceptedInteractionDto() *AcceptedInteractionDto`

NewAcceptedInteractionDto instantiates a new AcceptedInteractionDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAcceptedInteractionDtoWithDefaults

`func NewAcceptedInteractionDtoWithDefaults() *AcceptedInteractionDto`

NewAcceptedInteractionDtoWithDefaults instantiates a new AcceptedInteractionDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInteractionId

`func (o *AcceptedInteractionDto) GetInteractionId() string`

GetInteractionId returns the InteractionId field if non-nil, zero value otherwise.

### GetInteractionIdOk

`func (o *AcceptedInteractionDto) GetInteractionIdOk() (*string, bool)`

GetInteractionIdOk returns a tuple with the InteractionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInteractionId

`func (o *AcceptedInteractionDto) SetInteractionId(v string)`

SetInteractionId sets InteractionId field to given value.

### HasInteractionId

`func (o *AcceptedInteractionDto) HasInteractionId() bool`

HasInteractionId returns a boolean if a field has been set.

### GetIndex

`func (o *AcceptedInteractionDto) GetIndex() int32`

GetIndex returns the Index field if non-nil, zero value otherwise.

### GetIndexOk

`func (o *AcceptedInteractionDto) GetIndexOk() (*int32, bool)`

GetIndexOk returns a tuple with the Index field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIndex

`func (o *AcceptedInteractionDto) SetIndex(v int32)`

SetIndex sets Index field to given value.

### HasIndex

`func (o *AcceptedInteractionDto) HasIndex() bool`

HasIndex returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


