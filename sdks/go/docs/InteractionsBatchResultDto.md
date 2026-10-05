# InteractionsBatchResultDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CorrelationId** | Pointer to **string** | DDx API request identifier, provided as X-Correlation-Id on interactions responses for use linking all interactions in a request. | [optional] 
**TotalInteractions** | Pointer to **int32** | Total number of interactions in the batch. | [optional] 
**AcceptedInteractions** | Pointer to [**AcceptedInteractionsDto**](AcceptedInteractionsDto.md) |  | [optional] 
**RejectedInteractions** | Pointer to [**RejectedInteractionsDto**](RejectedInteractionsDto.md) |  | [optional] 

## Methods

### NewInteractionsBatchResultDto

`func NewInteractionsBatchResultDto() *InteractionsBatchResultDto`

NewInteractionsBatchResultDto instantiates a new InteractionsBatchResultDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInteractionsBatchResultDtoWithDefaults

`func NewInteractionsBatchResultDtoWithDefaults() *InteractionsBatchResultDto`

NewInteractionsBatchResultDtoWithDefaults instantiates a new InteractionsBatchResultDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCorrelationId

`func (o *InteractionsBatchResultDto) GetCorrelationId() string`

GetCorrelationId returns the CorrelationId field if non-nil, zero value otherwise.

### GetCorrelationIdOk

`func (o *InteractionsBatchResultDto) GetCorrelationIdOk() (*string, bool)`

GetCorrelationIdOk returns a tuple with the CorrelationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCorrelationId

`func (o *InteractionsBatchResultDto) SetCorrelationId(v string)`

SetCorrelationId sets CorrelationId field to given value.

### HasCorrelationId

`func (o *InteractionsBatchResultDto) HasCorrelationId() bool`

HasCorrelationId returns a boolean if a field has been set.

### GetTotalInteractions

`func (o *InteractionsBatchResultDto) GetTotalInteractions() int32`

GetTotalInteractions returns the TotalInteractions field if non-nil, zero value otherwise.

### GetTotalInteractionsOk

`func (o *InteractionsBatchResultDto) GetTotalInteractionsOk() (*int32, bool)`

GetTotalInteractionsOk returns a tuple with the TotalInteractions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetTotalInteractions

`func (o *InteractionsBatchResultDto) SetTotalInteractions(v int32)`

SetTotalInteractions sets TotalInteractions field to given value.

### HasTotalInteractions

`func (o *InteractionsBatchResultDto) HasTotalInteractions() bool`

HasTotalInteractions returns a boolean if a field has been set.

### GetAcceptedInteractions

`func (o *InteractionsBatchResultDto) GetAcceptedInteractions() AcceptedInteractionsDto`

GetAcceptedInteractions returns the AcceptedInteractions field if non-nil, zero value otherwise.

### GetAcceptedInteractionsOk

`func (o *InteractionsBatchResultDto) GetAcceptedInteractionsOk() (*AcceptedInteractionsDto, bool)`

GetAcceptedInteractionsOk returns a tuple with the AcceptedInteractions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAcceptedInteractions

`func (o *InteractionsBatchResultDto) SetAcceptedInteractions(v AcceptedInteractionsDto)`

SetAcceptedInteractions sets AcceptedInteractions field to given value.

### HasAcceptedInteractions

`func (o *InteractionsBatchResultDto) HasAcceptedInteractions() bool`

HasAcceptedInteractions returns a boolean if a field has been set.

### GetRejectedInteractions

`func (o *InteractionsBatchResultDto) GetRejectedInteractions() RejectedInteractionsDto`

GetRejectedInteractions returns the RejectedInteractions field if non-nil, zero value otherwise.

### GetRejectedInteractionsOk

`func (o *InteractionsBatchResultDto) GetRejectedInteractionsOk() (*RejectedInteractionsDto, bool)`

GetRejectedInteractionsOk returns a tuple with the RejectedInteractions field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRejectedInteractions

`func (o *InteractionsBatchResultDto) SetRejectedInteractions(v RejectedInteractionsDto)`

SetRejectedInteractions sets RejectedInteractions field to given value.

### HasRejectedInteractions

`func (o *InteractionsBatchResultDto) HasRejectedInteractions() bool`

HasRejectedInteractions returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


