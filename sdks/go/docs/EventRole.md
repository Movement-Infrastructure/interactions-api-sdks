# EventRole

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Name** | Pointer to **NullableString** | The role name or description | [optional] 

## Methods

### NewEventRole

`func NewEventRole() *EventRole`

NewEventRole instantiates a new EventRole object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEventRoleWithDefaults

`func NewEventRoleWithDefaults() *EventRole`

NewEventRoleWithDefaults instantiates a new EventRole object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetName

`func (o *EventRole) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *EventRole) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *EventRole) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *EventRole) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *EventRole) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *EventRole) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


