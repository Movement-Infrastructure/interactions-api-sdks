# InteractionVanFieldsDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ContactTypeId** | Pointer to **string** | VAN contact type ID. Must match a Contact Type accessible to the destination VAN committee.  See https://docs.ngpvan.com/reference/canvassresponsescontacttypes for details on retrieving accessible contact types. | [optional] 
**ResultCodeId** | Pointer to **NullableString** | VAN contact attempt result code, representing the result of that contact attempt. Result code availibility varies based on  contact type, so this value must represent a code that is available to the Contact Type ID specified above.  See https://docs.ngpvan.com/reference/canvassresponsesresultcodes to view Result Codes accessible to the destination VAN committee. | [optional] 

## Methods

### NewInteractionVanFieldsDto

`func NewInteractionVanFieldsDto() *InteractionVanFieldsDto`

NewInteractionVanFieldsDto instantiates a new InteractionVanFieldsDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInteractionVanFieldsDtoWithDefaults

`func NewInteractionVanFieldsDtoWithDefaults() *InteractionVanFieldsDto`

NewInteractionVanFieldsDtoWithDefaults instantiates a new InteractionVanFieldsDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetContactTypeId

`func (o *InteractionVanFieldsDto) GetContactTypeId() string`

GetContactTypeId returns the ContactTypeId field if non-nil, zero value otherwise.

### GetContactTypeIdOk

`func (o *InteractionVanFieldsDto) GetContactTypeIdOk() (*string, bool)`

GetContactTypeIdOk returns a tuple with the ContactTypeId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContactTypeId

`func (o *InteractionVanFieldsDto) SetContactTypeId(v string)`

SetContactTypeId sets ContactTypeId field to given value.

### HasContactTypeId

`func (o *InteractionVanFieldsDto) HasContactTypeId() bool`

HasContactTypeId returns a boolean if a field has been set.

### GetResultCodeId

`func (o *InteractionVanFieldsDto) GetResultCodeId() string`

GetResultCodeId returns the ResultCodeId field if non-nil, zero value otherwise.

### GetResultCodeIdOk

`func (o *InteractionVanFieldsDto) GetResultCodeIdOk() (*string, bool)`

GetResultCodeIdOk returns a tuple with the ResultCodeId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetResultCodeId

`func (o *InteractionVanFieldsDto) SetResultCodeId(v string)`

SetResultCodeId sets ResultCodeId field to given value.

### HasResultCodeId

`func (o *InteractionVanFieldsDto) HasResultCodeId() bool`

HasResultCodeId returns a boolean if a field has been set.

### SetResultCodeIdNil

`func (o *InteractionVanFieldsDto) SetResultCodeIdNil(b bool)`

 SetResultCodeIdNil sets the value for ResultCodeId to be an explicit nil

### UnsetResultCodeId
`func (o *InteractionVanFieldsDto) UnsetResultCodeId()`

UnsetResultCodeId ensures that no value is present for ResultCodeId, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


