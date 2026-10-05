# ExchangeInteractionStatusDtoCursorPaginatedResponseDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Metadata** | Pointer to [**MinervaMetadataDto**](MinervaMetadataDto.md) |  | [optional] 
**Data** | Pointer to [**[]ExchangeInteractionStatusDto**](ExchangeInteractionStatusDto.md) |  | [optional] 
**NextCursor** | Pointer to **NullableString** | Opaque cursor token for fetching the next page. Null if there are no more results. | [optional] 

## Methods

### NewExchangeInteractionStatusDtoCursorPaginatedResponseDto

`func NewExchangeInteractionStatusDtoCursorPaginatedResponseDto() *ExchangeInteractionStatusDtoCursorPaginatedResponseDto`

NewExchangeInteractionStatusDtoCursorPaginatedResponseDto instantiates a new ExchangeInteractionStatusDtoCursorPaginatedResponseDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewExchangeInteractionStatusDtoCursorPaginatedResponseDtoWithDefaults

`func NewExchangeInteractionStatusDtoCursorPaginatedResponseDtoWithDefaults() *ExchangeInteractionStatusDtoCursorPaginatedResponseDto`

NewExchangeInteractionStatusDtoCursorPaginatedResponseDtoWithDefaults instantiates a new ExchangeInteractionStatusDtoCursorPaginatedResponseDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetMetadata

`func (o *ExchangeInteractionStatusDtoCursorPaginatedResponseDto) GetMetadata() MinervaMetadataDto`

GetMetadata returns the Metadata field if non-nil, zero value otherwise.

### GetMetadataOk

`func (o *ExchangeInteractionStatusDtoCursorPaginatedResponseDto) GetMetadataOk() (*MinervaMetadataDto, bool)`

GetMetadataOk returns a tuple with the Metadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMetadata

`func (o *ExchangeInteractionStatusDtoCursorPaginatedResponseDto) SetMetadata(v MinervaMetadataDto)`

SetMetadata sets Metadata field to given value.

### HasMetadata

`func (o *ExchangeInteractionStatusDtoCursorPaginatedResponseDto) HasMetadata() bool`

HasMetadata returns a boolean if a field has been set.

### GetData

`func (o *ExchangeInteractionStatusDtoCursorPaginatedResponseDto) GetData() []ExchangeInteractionStatusDto`

GetData returns the Data field if non-nil, zero value otherwise.

### GetDataOk

`func (o *ExchangeInteractionStatusDtoCursorPaginatedResponseDto) GetDataOk() (*[]ExchangeInteractionStatusDto, bool)`

GetDataOk returns a tuple with the Data field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetData

`func (o *ExchangeInteractionStatusDtoCursorPaginatedResponseDto) SetData(v []ExchangeInteractionStatusDto)`

SetData sets Data field to given value.

### HasData

`func (o *ExchangeInteractionStatusDtoCursorPaginatedResponseDto) HasData() bool`

HasData returns a boolean if a field has been set.

### GetNextCursor

`func (o *ExchangeInteractionStatusDtoCursorPaginatedResponseDto) GetNextCursor() string`

GetNextCursor returns the NextCursor field if non-nil, zero value otherwise.

### GetNextCursorOk

`func (o *ExchangeInteractionStatusDtoCursorPaginatedResponseDto) GetNextCursorOk() (*string, bool)`

GetNextCursorOk returns a tuple with the NextCursor field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetNextCursor

`func (o *ExchangeInteractionStatusDtoCursorPaginatedResponseDto) SetNextCursor(v string)`

SetNextCursor sets NextCursor field to given value.

### HasNextCursor

`func (o *ExchangeInteractionStatusDtoCursorPaginatedResponseDto) HasNextCursor() bool`

HasNextCursor returns a boolean if a field has been set.

### SetNextCursorNil

`func (o *ExchangeInteractionStatusDtoCursorPaginatedResponseDto) SetNextCursorNil(b bool)`

 SetNextCursorNil sets the value for NextCursor to be an explicit nil

### UnsetNextCursor
`func (o *ExchangeInteractionStatusDtoCursorPaginatedResponseDto) UnsetNextCursor()`

UnsetNextCursor ensures that no value is present for NextCursor, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


