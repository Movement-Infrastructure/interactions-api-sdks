# InitiativeDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | Pointer to **NullableString** | Type of the initiative identifier specified in &#39;id&#39;. | [optional] 
**Id** | Pointer to **NullableString** | The actual initiative identifier, such as a campaign ID. | [optional] 
**Name** | Pointer to **NullableString** | Descriptive name or title for the initiative. | [optional] 

## Methods

### NewInitiativeDto

`func NewInitiativeDto() *InitiativeDto`

NewInitiativeDto instantiates a new InitiativeDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInitiativeDtoWithDefaults

`func NewInitiativeDtoWithDefaults() *InitiativeDto`

NewInitiativeDtoWithDefaults instantiates a new InitiativeDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *InitiativeDto) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *InitiativeDto) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *InitiativeDto) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *InitiativeDto) HasType() bool`

HasType returns a boolean if a field has been set.

### SetTypeNil

`func (o *InitiativeDto) SetTypeNil(b bool)`

 SetTypeNil sets the value for Type to be an explicit nil

### UnsetType
`func (o *InitiativeDto) UnsetType()`

UnsetType ensures that no value is present for Type, not even an explicit nil
### GetId

`func (o *InitiativeDto) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *InitiativeDto) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *InitiativeDto) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *InitiativeDto) HasId() bool`

HasId returns a boolean if a field has been set.

### SetIdNil

`func (o *InitiativeDto) SetIdNil(b bool)`

 SetIdNil sets the value for Id to be an explicit nil

### UnsetId
`func (o *InitiativeDto) UnsetId()`

UnsetId ensures that no value is present for Id, not even an explicit nil
### GetName

`func (o *InitiativeDto) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *InitiativeDto) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *InitiativeDto) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *InitiativeDto) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *InitiativeDto) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *InitiativeDto) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


