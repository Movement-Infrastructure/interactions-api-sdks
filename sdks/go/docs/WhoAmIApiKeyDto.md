# WhoAmIApiKeyDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**PublicKeyId** | **int32** | Unique identifier that specifies which API Key is being used | 
**Source** | [**SimpleMovementAppDto**](SimpleMovementAppDto.md) |  | 
**Workspace** | [**SimpleWorkspaceDto**](SimpleWorkspaceDto.md) |  | 
**ExpireDate** | Pointer to **NullableTime** | The date and time the API Key is set to expire. The time should be evaluated in Eastern Time. | [optional] 
**Destinations** | Pointer to [**[]SimpleDestinationDto**](SimpleDestinationDto.md) | The destinations enabled for this API key | [optional] 
**VanApiKey** | Pointer to [**MercuryDestinationVanApiKeyDto**](MercuryDestinationVanApiKeyDto.md) |  | [optional] 

## Methods

### NewWhoAmIApiKeyDto

`func NewWhoAmIApiKeyDto(publicKeyId int32, source SimpleMovementAppDto, workspace SimpleWorkspaceDto, ) *WhoAmIApiKeyDto`

NewWhoAmIApiKeyDto instantiates a new WhoAmIApiKeyDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewWhoAmIApiKeyDtoWithDefaults

`func NewWhoAmIApiKeyDtoWithDefaults() *WhoAmIApiKeyDto`

NewWhoAmIApiKeyDtoWithDefaults instantiates a new WhoAmIApiKeyDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetPublicKeyId

`func (o *WhoAmIApiKeyDto) GetPublicKeyId() int32`

GetPublicKeyId returns the PublicKeyId field if non-nil, zero value otherwise.

### GetPublicKeyIdOk

`func (o *WhoAmIApiKeyDto) GetPublicKeyIdOk() (*int32, bool)`

GetPublicKeyIdOk returns a tuple with the PublicKeyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPublicKeyId

`func (o *WhoAmIApiKeyDto) SetPublicKeyId(v int32)`

SetPublicKeyId sets PublicKeyId field to given value.


### GetSource

`func (o *WhoAmIApiKeyDto) GetSource() SimpleMovementAppDto`

GetSource returns the Source field if non-nil, zero value otherwise.

### GetSourceOk

`func (o *WhoAmIApiKeyDto) GetSourceOk() (*SimpleMovementAppDto, bool)`

GetSourceOk returns a tuple with the Source field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSource

`func (o *WhoAmIApiKeyDto) SetSource(v SimpleMovementAppDto)`

SetSource sets Source field to given value.


### GetWorkspace

`func (o *WhoAmIApiKeyDto) GetWorkspace() SimpleWorkspaceDto`

GetWorkspace returns the Workspace field if non-nil, zero value otherwise.

### GetWorkspaceOk

`func (o *WhoAmIApiKeyDto) GetWorkspaceOk() (*SimpleWorkspaceDto, bool)`

GetWorkspaceOk returns a tuple with the Workspace field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWorkspace

`func (o *WhoAmIApiKeyDto) SetWorkspace(v SimpleWorkspaceDto)`

SetWorkspace sets Workspace field to given value.


### GetExpireDate

`func (o *WhoAmIApiKeyDto) GetExpireDate() time.Time`

GetExpireDate returns the ExpireDate field if non-nil, zero value otherwise.

### GetExpireDateOk

`func (o *WhoAmIApiKeyDto) GetExpireDateOk() (*time.Time, bool)`

GetExpireDateOk returns a tuple with the ExpireDate field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExpireDate

`func (o *WhoAmIApiKeyDto) SetExpireDate(v time.Time)`

SetExpireDate sets ExpireDate field to given value.

### HasExpireDate

`func (o *WhoAmIApiKeyDto) HasExpireDate() bool`

HasExpireDate returns a boolean if a field has been set.

### SetExpireDateNil

`func (o *WhoAmIApiKeyDto) SetExpireDateNil(b bool)`

 SetExpireDateNil sets the value for ExpireDate to be an explicit nil

### UnsetExpireDate
`func (o *WhoAmIApiKeyDto) UnsetExpireDate()`

UnsetExpireDate ensures that no value is present for ExpireDate, not even an explicit nil
### GetDestinations

`func (o *WhoAmIApiKeyDto) GetDestinations() []SimpleDestinationDto`

GetDestinations returns the Destinations field if non-nil, zero value otherwise.

### GetDestinationsOk

`func (o *WhoAmIApiKeyDto) GetDestinationsOk() (*[]SimpleDestinationDto, bool)`

GetDestinationsOk returns a tuple with the Destinations field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDestinations

`func (o *WhoAmIApiKeyDto) SetDestinations(v []SimpleDestinationDto)`

SetDestinations sets Destinations field to given value.

### HasDestinations

`func (o *WhoAmIApiKeyDto) HasDestinations() bool`

HasDestinations returns a boolean if a field has been set.

### GetVanApiKey

`func (o *WhoAmIApiKeyDto) GetVanApiKey() MercuryDestinationVanApiKeyDto`

GetVanApiKey returns the VanApiKey field if non-nil, zero value otherwise.

### GetVanApiKeyOk

`func (o *WhoAmIApiKeyDto) GetVanApiKeyOk() (*MercuryDestinationVanApiKeyDto, bool)`

GetVanApiKeyOk returns a tuple with the VanApiKey field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVanApiKey

`func (o *WhoAmIApiKeyDto) SetVanApiKey(v MercuryDestinationVanApiKeyDto)`

SetVanApiKey sets VanApiKey field to given value.

### HasVanApiKey

`func (o *WhoAmIApiKeyDto) HasVanApiKey() bool`

HasVanApiKey returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


