# InteractionsExternalApiTransactionDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**DateCreatedUtc** | Pointer to **time.Time** | The UTC date and time at which the request was received. | [optional] 
**InteractionId** | Pointer to **string** | ID used to identify the interaction; ID will have been returned from the initial publish response. | [optional] 
**CorrelationId** | Pointer to **string** | DDx API request identifier, provided as X-Correlation-Id on interactions responses for use linking all interactions in a request. | [optional] 
**Status** | Pointer to [**ExternalTransactionStatus**](ExternalTransactionStatus.md) |  | [optional] 
**Logs** | Pointer to [**[]InteractionsExternalApiTransactionLogDto**](InteractionsExternalApiTransactionLogDto.md) | Any logs associated with this external API transaction. | [optional] 

## Methods

### NewInteractionsExternalApiTransactionDto

`func NewInteractionsExternalApiTransactionDto() *InteractionsExternalApiTransactionDto`

NewInteractionsExternalApiTransactionDto instantiates a new InteractionsExternalApiTransactionDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInteractionsExternalApiTransactionDtoWithDefaults

`func NewInteractionsExternalApiTransactionDtoWithDefaults() *InteractionsExternalApiTransactionDto`

NewInteractionsExternalApiTransactionDtoWithDefaults instantiates a new InteractionsExternalApiTransactionDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetDateCreatedUtc

`func (o *InteractionsExternalApiTransactionDto) GetDateCreatedUtc() time.Time`

GetDateCreatedUtc returns the DateCreatedUtc field if non-nil, zero value otherwise.

### GetDateCreatedUtcOk

`func (o *InteractionsExternalApiTransactionDto) GetDateCreatedUtcOk() (*time.Time, bool)`

GetDateCreatedUtcOk returns a tuple with the DateCreatedUtc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDateCreatedUtc

`func (o *InteractionsExternalApiTransactionDto) SetDateCreatedUtc(v time.Time)`

SetDateCreatedUtc sets DateCreatedUtc field to given value.

### HasDateCreatedUtc

`func (o *InteractionsExternalApiTransactionDto) HasDateCreatedUtc() bool`

HasDateCreatedUtc returns a boolean if a field has been set.

### GetInteractionId

`func (o *InteractionsExternalApiTransactionDto) GetInteractionId() string`

GetInteractionId returns the InteractionId field if non-nil, zero value otherwise.

### GetInteractionIdOk

`func (o *InteractionsExternalApiTransactionDto) GetInteractionIdOk() (*string, bool)`

GetInteractionIdOk returns a tuple with the InteractionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInteractionId

`func (o *InteractionsExternalApiTransactionDto) SetInteractionId(v string)`

SetInteractionId sets InteractionId field to given value.

### HasInteractionId

`func (o *InteractionsExternalApiTransactionDto) HasInteractionId() bool`

HasInteractionId returns a boolean if a field has been set.

### GetCorrelationId

`func (o *InteractionsExternalApiTransactionDto) GetCorrelationId() string`

GetCorrelationId returns the CorrelationId field if non-nil, zero value otherwise.

### GetCorrelationIdOk

`func (o *InteractionsExternalApiTransactionDto) GetCorrelationIdOk() (*string, bool)`

GetCorrelationIdOk returns a tuple with the CorrelationId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCorrelationId

`func (o *InteractionsExternalApiTransactionDto) SetCorrelationId(v string)`

SetCorrelationId sets CorrelationId field to given value.

### HasCorrelationId

`func (o *InteractionsExternalApiTransactionDto) HasCorrelationId() bool`

HasCorrelationId returns a boolean if a field has been set.

### GetStatus

`func (o *InteractionsExternalApiTransactionDto) GetStatus() ExternalTransactionStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *InteractionsExternalApiTransactionDto) GetStatusOk() (*ExternalTransactionStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *InteractionsExternalApiTransactionDto) SetStatus(v ExternalTransactionStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *InteractionsExternalApiTransactionDto) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetLogs

`func (o *InteractionsExternalApiTransactionDto) GetLogs() []InteractionsExternalApiTransactionLogDto`

GetLogs returns the Logs field if non-nil, zero value otherwise.

### GetLogsOk

`func (o *InteractionsExternalApiTransactionDto) GetLogsOk() (*[]InteractionsExternalApiTransactionLogDto, bool)`

GetLogsOk returns a tuple with the Logs field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLogs

`func (o *InteractionsExternalApiTransactionDto) SetLogs(v []InteractionsExternalApiTransactionLogDto)`

SetLogs sets Logs field to given value.

### HasLogs

`func (o *InteractionsExternalApiTransactionDto) HasLogs() bool`

HasLogs returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


