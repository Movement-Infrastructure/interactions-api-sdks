# ExchangeInteractionStatusDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**CorrelationId** | Pointer to **string** | DDx API request identifier. | [optional] 
**InteractionId** | Pointer to **NullableString** | The interaction&#39;s unique identifier. | [optional] 
**Status** | Pointer to [**ExchangeInteractionStatus**](ExchangeInteractionStatus.md) |  | [optional] 
**ExchangeDataTypes** | Pointer to **string** | The Exchange data types the interaction was transformed into. | [optional] 
**PublishTime** | Pointer to **time.Time** | Timestamp when the interaction was received into the Exchange pipeline (Pub/Sub publish time). | [optional] 

## Methods

### NewExchangeInteractionStatusDto

`func NewExchangeInteractionStatusDto() *ExchangeInteractionStatusDto`

NewExchangeInteractionStatusDto instantiates a new ExchangeInteractionStatusDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewExchangeInteractionStatusDtoWithDefaults

`func NewExchangeInteractionStatusDtoWithDefaults() *ExchangeInteractionStatusDto`

NewExchangeInteractionStatusDtoWithDefaults instantiates a new ExchangeInteractionStatusDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetCorrelationId

`func (o *ExchangeInteractionStatusDto) GetCorrelationId() string`

GetCorrelationId returns the CorrelationId field if non-nil, zero value otherwise.

### GetCorrelationIdOk

`func (o *ExchangeInteractionStatusDto) GetCorrelationIdOk() (*string, bool)`

GetCorrelationIdOk returns a tuple with the CorrelationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCorrelationId

`func (o *ExchangeInteractionStatusDto) SetCorrelationId(v string)`

SetCorrelationId sets CorrelationId field to given value.

### HasCorrelationId

`func (o *ExchangeInteractionStatusDto) HasCorrelationId() bool`

HasCorrelationId returns a boolean if a field has been set.

### GetInteractionId

`func (o *ExchangeInteractionStatusDto) GetInteractionId() string`

GetInteractionId returns the InteractionId field if non-nil, zero value otherwise.

### GetInteractionIdOk

`func (o *ExchangeInteractionStatusDto) GetInteractionIdOk() (*string, bool)`

GetInteractionIdOk returns a tuple with the InteractionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInteractionId

`func (o *ExchangeInteractionStatusDto) SetInteractionId(v string)`

SetInteractionId sets InteractionId field to given value.

### HasInteractionId

`func (o *ExchangeInteractionStatusDto) HasInteractionId() bool`

HasInteractionId returns a boolean if a field has been set.

### SetInteractionIdNil

`func (o *ExchangeInteractionStatusDto) SetInteractionIdNil(b bool)`

 SetInteractionIdNil sets the value for InteractionId to be an explicit nil

### UnsetInteractionId
`func (o *ExchangeInteractionStatusDto) UnsetInteractionId()`

UnsetInteractionId ensures that no value is present for InteractionId, not even an explicit nil
### GetStatus

`func (o *ExchangeInteractionStatusDto) GetStatus() ExchangeInteractionStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *ExchangeInteractionStatusDto) GetStatusOk() (*ExchangeInteractionStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *ExchangeInteractionStatusDto) SetStatus(v ExchangeInteractionStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *ExchangeInteractionStatusDto) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetExchangeDataTypes

`func (o *ExchangeInteractionStatusDto) GetExchangeDataTypes() string`

GetExchangeDataTypes returns the ExchangeDataTypes field if non-nil, zero value otherwise.

### GetExchangeDataTypesOk

`func (o *ExchangeInteractionStatusDto) GetExchangeDataTypesOk() (*string, bool)`

GetExchangeDataTypesOk returns a tuple with the ExchangeDataTypes field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExchangeDataTypes

`func (o *ExchangeInteractionStatusDto) SetExchangeDataTypes(v string)`

SetExchangeDataTypes sets ExchangeDataTypes field to given value.

### HasExchangeDataTypes

`func (o *ExchangeInteractionStatusDto) HasExchangeDataTypes() bool`

HasExchangeDataTypes returns a boolean if a field has been set.

### GetPublishTime

`func (o *ExchangeInteractionStatusDto) GetPublishTime() time.Time`

GetPublishTime returns the PublishTime field if non-nil, zero value otherwise.

### GetPublishTimeOk

`func (o *ExchangeInteractionStatusDto) GetPublishTimeOk() (*time.Time, bool)`

GetPublishTimeOk returns a tuple with the PublishTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublishTime

`func (o *ExchangeInteractionStatusDto) SetPublishTime(v time.Time)`

SetPublishTime sets PublishTime field to given value.

### HasPublishTime

`func (o *ExchangeInteractionStatusDto) HasPublishTime() bool`

HasPublishTime returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


