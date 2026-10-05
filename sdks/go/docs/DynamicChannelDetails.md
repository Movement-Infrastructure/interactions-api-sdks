# DynamicChannelDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | Pointer to **NullableString** | Optional; unique identifier for any known id for the channel &#x60;type&#x60; | [optional] 
**Type** | Pointer to **string** | Type of the channel specified in &#39;value&#39;. Required when Channel is provided.                Recognized types:  - \&quot;phone_number\&quot;: Indicates &#x60;value&#x60; is a phone number; &#x60;value&#x60; must be in E.164 format (e.g., +14155552671).  - \&quot;email\&quot;: Indicates &#x60;value&#x60; is an email address.  - [any other identifier]: Any type not listed above. &#x60;value&#x60; can be a string, an int or an arbitrary object. | [optional] 
**Value** | Pointer to **interface{}** |  The actual channel used during the outreach attempt. This field can be provided as a string or int though only the object form is shown here.   Examples: +14155552671, name@org.org, @handle.   Required when Channel is provided. | [optional] 

## Methods

### NewDynamicChannelDetails

`func NewDynamicChannelDetails() *DynamicChannelDetails`

NewDynamicChannelDetails instantiates a new DynamicChannelDetails object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewDynamicChannelDetailsWithDefaults

`func NewDynamicChannelDetailsWithDefaults() *DynamicChannelDetails`

NewDynamicChannelDetailsWithDefaults instantiates a new DynamicChannelDetails object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *DynamicChannelDetails) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *DynamicChannelDetails) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *DynamicChannelDetails) SetId(v string)`

SetId sets Id field to given value.

### HasId

`func (o *DynamicChannelDetails) HasId() bool`

HasId returns a boolean if a field has been set.

### SetIdNil

`func (o *DynamicChannelDetails) SetIdNil(b bool)`

 SetIdNil sets the value for Id to be an explicit nil

### UnsetId
`func (o *DynamicChannelDetails) UnsetId()`

UnsetId ensures that no value is present for Id, not even an explicit nil
### GetType

`func (o *DynamicChannelDetails) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *DynamicChannelDetails) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *DynamicChannelDetails) SetType(v string)`

SetType sets Type field to given value.

### HasType

`func (o *DynamicChannelDetails) HasType() bool`

HasType returns a boolean if a field has been set.

### GetValue

`func (o *DynamicChannelDetails) GetValue() interface{}`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *DynamicChannelDetails) GetValueOk() (*interface{}, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *DynamicChannelDetails) SetValue(v interface{})`

SetValue sets Value field to given value.

### HasValue

`func (o *DynamicChannelDetails) HasValue() bool`

HasValue returns a boolean if a field has been set.

### SetValueNil

`func (o *DynamicChannelDetails) SetValueNil(b bool)`

 SetValueNil sets the value for Value to be an explicit nil

### UnsetValue
`func (o *DynamicChannelDetails) UnsetValue()`

UnsetValue ensures that no value is present for Value, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


