# SimpleDestinationDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **int32** | Unique identifier for the destination | 
**Name** | Pointer to **NullableString** | Display name for the destination | [optional] 
**IsVanDestination** | Pointer to **bool** | Indicator of whether the destination integrates with NGP VAN  and requires an associated VAN External API Key | [optional] 

## Methods

### NewSimpleDestinationDto

`func NewSimpleDestinationDto(id int32, ) *SimpleDestinationDto`

NewSimpleDestinationDto instantiates a new SimpleDestinationDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSimpleDestinationDtoWithDefaults

`func NewSimpleDestinationDtoWithDefaults() *SimpleDestinationDto`

NewSimpleDestinationDtoWithDefaults instantiates a new SimpleDestinationDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *SimpleDestinationDto) GetId() int32`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *SimpleDestinationDto) GetIdOk() (*int32, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *SimpleDestinationDto) SetId(v int32)`

SetId sets Id field to given value.


### GetName

`func (o *SimpleDestinationDto) GetName() string`

GetName returns the Name field if non-nil, zero value otherwise.

### GetNameOk

`func (o *SimpleDestinationDto) GetNameOk() (*string, bool)`

GetNameOk returns a tuple with the Name field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetName

`func (o *SimpleDestinationDto) SetName(v string)`

SetName sets Name field to given value.

### HasName

`func (o *SimpleDestinationDto) HasName() bool`

HasName returns a boolean if a field has been set.

### SetNameNil

`func (o *SimpleDestinationDto) SetNameNil(b bool)`

 SetNameNil sets the value for Name to be an explicit nil

### UnsetName
`func (o *SimpleDestinationDto) UnsetName()`

UnsetName ensures that no value is present for Name, not even an explicit nil
### GetIsVanDestination

`func (o *SimpleDestinationDto) GetIsVanDestination() bool`

GetIsVanDestination returns the IsVanDestination field if non-nil, zero value otherwise.

### GetIsVanDestinationOk

`func (o *SimpleDestinationDto) GetIsVanDestinationOk() (*bool, bool)`

GetIsVanDestinationOk returns a tuple with the IsVanDestination field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetIsVanDestination

`func (o *SimpleDestinationDto) SetIsVanDestination(v bool)`

SetIsVanDestination sets IsVanDestination field to given value.

### HasIsVanDestination

`func (o *SimpleDestinationDto) HasIsVanDestination() bool`

HasIsVanDestination returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


