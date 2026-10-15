# InteractionDtoChannel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** |  | 
**Value** | **map[string]interface{}** |  | 
**Id** | Pointer to **NullableString** | Optional; unique identifier for any known id for the channel &#x60;type&#x60; | [optional] 

## Methods

### NewInteractionDtoChannel

`func NewInteractionDtoChannel(type_ string, value map[string]interface{}, ) *InteractionDtoChannel`

NewInteractionDtoChannel instantiates a new InteractionDtoChannel object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInteractionDtoChannelWithDefaults

`func NewInteractionDtoChannelWithDefaults() *InteractionDtoChannel`

NewInteractionDtoChannelWithDefaults instantiates a new InteractionDtoChannel object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *InteractionDtoChannel) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *InteractionDtoChannel) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *InteractionDtoChannel) SetType(v string)`

SetType sets Type field to given value.


### GetValue

`func (o *InteractionDtoChannel) GetValue() map[string]interface{}`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *InteractionDtoChannel) GetValueOk() (*map[string]interface{}, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *InteractionDtoChannel) SetValue(v map[string]interface{})`

SetValue sets Value field to given value.


### GetId

`func (o *InteractionDtoChannel) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *InteractionDtoChannel) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *InteractionDtoChannel) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *InteractionDtoChannel) HasId() bool`

HasId returns a boolean if a field has been set.

### SetIdNil

`func (o *InteractionDtoChannel) SetIdNil(b bool)`

 SetIdNil sets the value for Id to be an explicit nil

### UnsetId
`func (o *InteractionDtoChannel) UnsetId()`

UnsetId ensures that no value is present for Id, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


