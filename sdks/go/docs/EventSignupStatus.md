# EventSignupStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Status** | [**EventSignupStatusValue**](EventSignupStatusValue.md) |  | 
**VendorReference** | Pointer to **NullableString** | Open string field for vendor-specific reference information | [optional] 

## Methods

### NewEventSignupStatus

`func NewEventSignupStatus(status EventSignupStatusValue, ) *EventSignupStatus`

NewEventSignupStatus instantiates a new EventSignupStatus object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEventSignupStatusWithDefaults

`func NewEventSignupStatusWithDefaults() *EventSignupStatus`

NewEventSignupStatusWithDefaults instantiates a new EventSignupStatus object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetStatus

`func (o *EventSignupStatus) GetStatus() EventSignupStatusValue`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *EventSignupStatus) GetStatusOk() (*EventSignupStatusValue, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *EventSignupStatus) SetStatus(v EventSignupStatusValue)`

SetStatus sets Status field to given value.


### GetVendorReference

`func (o *EventSignupStatus) GetVendorReference() string`

GetVendorReference returns the VendorReference field if non-nil, zero value otherwise.

### GetVendorReferenceOk

`func (o *EventSignupStatus) GetVendorReferenceOk() (*string, bool)`

GetVendorReferenceOk returns a tuple with the VendorReference field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVendorReference

`func (o *EventSignupStatus) SetVendorReference(v string)`

SetVendorReference sets VendorReference field to given value.

### HasVendorReference

`func (o *EventSignupStatus) HasVendorReference() bool`

HasVendorReference returns a boolean if a field has been set.

### SetVendorReferenceNil

`func (o *EventSignupStatus) SetVendorReferenceNil(b bool)`

 SetVendorReferenceNil sets the value for VendorReference to be an explicit nil

### UnsetVendorReference
`func (o *EventSignupStatus) UnsetVendorReference()`

UnsetVendorReference ensures that no value is present for VendorReference, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


