# VanApiKeyDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ExternalApiKeyId** | Pointer to **int32** |  | [optional] 
**Type** | Pointer to [**ExternalApiKeyType**](ExternalApiKeyType.md) |  | [optional] 
**Status** | Pointer to [**ExternalApiKeyStatus**](ExternalApiKeyStatus.md) |  | [optional] 
**Name** | Pointer to **NullableString** |  | [optional] 
**DateCreated** | Pointer to **time.Time** |  | [optional] 
**Connections** | Pointer to **int32** |  | [optional] 
**CommitteeName** | Pointer to **string** |  | [optional] 
**HasMyVoters** | Pointer to **bool** |  | [optional] 
**HasMyCampaign** | Pointer to **bool** |  | [optional] 
**KeyRef** | Pointer to **string** |  | [optional] 

## Methods

### NewVanApiKeyDto

`func NewVanApiKeyDto() *VanApiKeyDto`

NewVanApiKeyDto instantiates a new VanApiKeyDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewVanApiKeyDtoWithDefaults

`func NewVanApiKeyDtoWithDefaults() *VanApiKeyDto`

NewVanApiKeyDtoWithDefaults instantiates a new VanApiKeyDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetExternalApiKeyId

`func (o *VanApiKeyDto) GetExternalApiKeyId() int32`

GetExternalApiKeyId returns the ExternalApiKeyId field if non-nil, zero value otherwise.

### GetExternalApiKeyIdOk

`func (o *VanApiKeyDto) GetExternalApiKeyIdOk() (*int32, bool)`

GetExternalApiKeyIdOk returns a tuple with the ExternalApiKeyId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetExternalApiKeyId

`func (o *VanApiKeyDto) SetExternalApiKeyId(v int32)`

SetExternalApiKeyId sets ExternalApiKeyId field to given value.

### HasExternalApiKeyId

`func (o *VanApiKeyDto) HasExternalApiKeyId() bool`

HasExternalApiKeyId returns a boolean if a field has been set.

### GetType

`func (o *VanApiKeyDto) GetType() ExternalApiKeyType`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *VanApiKeyDto) GetTypeOk() (*ExternalApiKeyType, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *VanApiKeyDto) SetType(v ExternalApiKeyType)`

SetType sets Type field to given value.

### HasType

`func (o *VanApiKeyDto) HasType() bool`

HasType returns a boolean if a field has been set.

### GetStatus

`func (o *VanApiKeyDto) GetStatus() ExternalApiKeyStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *VanApiKeyDto) GetStatusOk() (*ExternalApiKeyStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *VanApiKeyDto) SetStatus(v ExternalApiKeyStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *VanApiKeyDto) HasStatus() bool`

HasStatus returns a boolean if a field has been set.

### GetName

`func (o *VanApiKeyDto) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *VanApiKeyDto) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *VanApiKeyDto) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *VanApiKeyDto) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *VanApiKeyDto) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *VanApiKeyDto) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetDateCreated

`func (o *VanApiKeyDto) GetDateCreated() time.Time`

GetDateCreated returns the DateCreated field if non-nil, zero value otherwise.

### GetDateCreatedOk

`func (o *VanApiKeyDto) GetDateCreatedOk() (*time.Time, bool)`

GetDateCreatedOk returns a tuple with the DateCreated field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDateCreated

`func (o *VanApiKeyDto) SetDateCreated(v time.Time)`

SetDateCreated sets DateCreated field to given value.

### HasDateCreated

`func (o *VanApiKeyDto) HasDateCreated() bool`

HasDateCreated returns a boolean if a field has been set.

### GetConnections

`func (o *VanApiKeyDto) GetConnections() int32`

GetConnections returns the Connections field if non-nil, zero value otherwise.

### GetConnectionsOk

`func (o *VanApiKeyDto) GetConnectionsOk() (*int32, bool)`

GetConnectionsOk returns a tuple with the Connections field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetConnections

`func (o *VanApiKeyDto) SetConnections(v int32)`

SetConnections sets Connections field to given value.

### HasConnections

`func (o *VanApiKeyDto) HasConnections() bool`

HasConnections returns a boolean if a field has been set.

### GetCommitteeName

`func (o *VanApiKeyDto) GetCommitteeName() string`

GetCommitteeName returns the CommitteeName field if non-nil, zero value otherwise.

### GetCommitteeNameOk

`func (o *VanApiKeyDto) GetCommitteeNameOk() (*string, bool)`

GetCommitteeNameOk returns a tuple with the CommitteeName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommitteeName

`func (o *VanApiKeyDto) SetCommitteeName(v string)`

SetCommitteeName sets CommitteeName field to given value.

### HasCommitteeName

`func (o *VanApiKeyDto) HasCommitteeName() bool`

HasCommitteeName returns a boolean if a field has been set.

### GetHasMyVoters

`func (o *VanApiKeyDto) GetHasMyVoters() bool`

GetHasMyVoters returns the HasMyVoters field if non-nil, zero value otherwise.

### GetHasMyVotersOk

`func (o *VanApiKeyDto) GetHasMyVotersOk() (*bool, bool)`

GetHasMyVotersOk returns a tuple with the HasMyVoters field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasMyVoters

`func (o *VanApiKeyDto) SetHasMyVoters(v bool)`

SetHasMyVoters sets HasMyVoters field to given value.

### HasHasMyVoters

`func (o *VanApiKeyDto) HasHasMyVoters() bool`

HasHasMyVoters returns a boolean if a field has been set.

### GetHasMyCampaign

`func (o *VanApiKeyDto) GetHasMyCampaign() bool`

GetHasMyCampaign returns the HasMyCampaign field if non-nil, zero value otherwise.

### GetHasMyCampaignOk

`func (o *VanApiKeyDto) GetHasMyCampaignOk() (*bool, bool)`

GetHasMyCampaignOk returns a tuple with the HasMyCampaign field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetHasMyCampaign

`func (o *VanApiKeyDto) SetHasMyCampaign(v bool)`

SetHasMyCampaign sets HasMyCampaign field to given value.

### HasHasMyCampaign

`func (o *VanApiKeyDto) HasHasMyCampaign() bool`

HasHasMyCampaign returns a boolean if a field has been set.

### GetKeyRef

`func (o *VanApiKeyDto) GetKeyRef() string`

GetKeyRef returns the KeyRef field if non-nil, zero value otherwise.

### GetKeyRefOk

`func (o *VanApiKeyDto) GetKeyRefOk() (*string, bool)`

GetKeyRefOk returns a tuple with the KeyRef field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetKeyRef

`func (o *VanApiKeyDto) SetKeyRef(v string)`

SetKeyRef sets KeyRef field to given value.

### HasKeyRef

`func (o *VanApiKeyDto) HasKeyRef() bool`

HasKeyRef returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


