# AddressChannelDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **NullableString** | Optional; unique identifier for any known id for the channel &#x60;type&#x60; | [optional] 
**Type** | **string** | Specifies that the &#x60;type&#x60; of channel used was an &#x60;address&#x60; and a full address must be provided as the &#x60;value&#x60;. | 
**Value** | [**Address**](Address.md) |  | 

## Methods

### NewAddressChannelDetails

`func NewAddressChannelDetails(type_ string, value Address, ) *AddressChannelDetails`

NewAddressChannelDetails instantiates a new AddressChannelDetails object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewAddressChannelDetailsWithDefaults

`func NewAddressChannelDetailsWithDefaults() *AddressChannelDetails`

NewAddressChannelDetailsWithDefaults instantiates a new AddressChannelDetails object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *AddressChannelDetails) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *AddressChannelDetails) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *AddressChannelDetails) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *AddressChannelDetails) HasId() bool`

HasId returns a boolean if a field has been set.

### SetIdNil

`func (o *AddressChannelDetails) SetIdNil(b bool)`

 SetIdNil sets the value for Id to be an explicit nil

### UnsetId
`func (o *AddressChannelDetails) UnsetId()`

UnsetId ensures that no value is present for Id, not even an explicit nil
### GetType

`func (o *AddressChannelDetails) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *AddressChannelDetails) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *AddressChannelDetails) SetType(v string)`

SetType sets Type field to given value.


### GetValue

`func (o *AddressChannelDetails) GetValue() Address`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *AddressChannelDetails) GetValueOk() (*Address, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *AddressChannelDetails) SetValue(v Address)`

SetValue sets Value field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


