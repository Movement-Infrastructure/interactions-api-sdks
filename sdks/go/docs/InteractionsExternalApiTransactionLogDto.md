# InteractionsExternalApiTransactionLogDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ResponseStatusCode** | Pointer to **NullableInt32** | HTTP response code received for external API request. | [optional] 
**Response** | Pointer to **NullableString** | Response JSON received for external API request. | [optional] 
**DateCreatedUtc** | Pointer to **time.Time** | Timestamp for when the external API request was made. | [optional] 

## Methods

### NewInteractionsExternalApiTransactionLogDto

`func NewInteractionsExternalApiTransactionLogDto() *InteractionsExternalApiTransactionLogDto`

NewInteractionsExternalApiTransactionLogDto instantiates a new InteractionsExternalApiTransactionLogDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInteractionsExternalApiTransactionLogDtoWithDefaults

`func NewInteractionsExternalApiTransactionLogDtoWithDefaults() *InteractionsExternalApiTransactionLogDto`

NewInteractionsExternalApiTransactionLogDtoWithDefaults instantiates a new InteractionsExternalApiTransactionLogDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetResponseStatusCode

`func (o *InteractionsExternalApiTransactionLogDto) GetResponseStatusCode() int32`

GetResponseStatusCode returns the ResponseStatusCode field if non-nil, zero value otherwise.

### GetResponseStatusCodeOk

`func (o *InteractionsExternalApiTransactionLogDto) GetResponseStatusCodeOk() (*int32, bool)`

GetResponseStatusCodeOk returns a tuple with the ResponseStatusCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponseStatusCode

`func (o *InteractionsExternalApiTransactionLogDto) SetResponseStatusCode(v int32)`

SetResponseStatusCode sets ResponseStatusCode field to given value.

### HasResponseStatusCode

`func (o *InteractionsExternalApiTransactionLogDto) HasResponseStatusCode() bool`

HasResponseStatusCode returns a boolean if a field has been set.

### SetResponseStatusCodeNil

`func (o *InteractionsExternalApiTransactionLogDto) SetResponseStatusCodeNil(b bool)`

 SetResponseStatusCodeNil sets the value for ResponseStatusCode to be an explicit nil

### UnsetResponseStatusCode
`func (o *InteractionsExternalApiTransactionLogDto) UnsetResponseStatusCode()`

UnsetResponseStatusCode ensures that no value is present for ResponseStatusCode, not even an explicit nil
### GetResponse

`func (o *InteractionsExternalApiTransactionLogDto) GetResponse() string`

GetResponse returns the Response field if non-nil, zero value otherwise.

### GetResponseOk

`func (o *InteractionsExternalApiTransactionLogDto) GetResponseOk() (*string, bool)`

GetResponseOk returns a tuple with the Response field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResponse

`func (o *InteractionsExternalApiTransactionLogDto) SetResponse(v string)`

SetResponse sets Response field to given value.

### HasResponse

`func (o *InteractionsExternalApiTransactionLogDto) HasResponse() bool`

HasResponse returns a boolean if a field has been set.

### SetResponseNil

`func (o *InteractionsExternalApiTransactionLogDto) SetResponseNil(b bool)`

 SetResponseNil sets the value for Response to be an explicit nil

### UnsetResponse
`func (o *InteractionsExternalApiTransactionLogDto) UnsetResponse()`

UnsetResponse ensures that no value is present for Response, not even an explicit nil
### GetDateCreatedUtc

`func (o *InteractionsExternalApiTransactionLogDto) GetDateCreatedUtc() time.Time`

GetDateCreatedUtc returns the DateCreatedUtc field if non-nil, zero value otherwise.

### GetDateCreatedUtcOk

`func (o *InteractionsExternalApiTransactionLogDto) GetDateCreatedUtcOk() (*time.Time, bool)`

GetDateCreatedUtcOk returns a tuple with the DateCreatedUtc field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDateCreatedUtc

`func (o *InteractionsExternalApiTransactionLogDto) SetDateCreatedUtc(v time.Time)`

SetDateCreatedUtc sets DateCreatedUtc field to given value.

### HasDateCreatedUtc

`func (o *InteractionsExternalApiTransactionLogDto) HasDateCreatedUtc() bool`

HasDateCreatedUtc returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


