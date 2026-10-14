# EventSignup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**EventId** | [**EventDetails**](EventDetails.md) |  | 
**Shifts** | Pointer to [**[]EventDetails**](EventDetails.md) | Optional array of shift identifiers for specific shifts within the event | [optional] 
**Role** | Pointer to [**EventRole**](EventRole.md) |  | [optional] 
**Status** | Pointer to [**EventSignupStatus**](EventSignupStatus.md) |  | [optional] 

## Methods

### NewEventSignup

`func NewEventSignup(eventId EventDetails, ) *EventSignup`

NewEventSignup instantiates a new EventSignup object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEventSignupWithDefaults

`func NewEventSignupWithDefaults() *EventSignup`

NewEventSignupWithDefaults instantiates a new EventSignup object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEventId

`func (o *EventSignup) GetEventId() EventDetails`

GetEventId returns the EventId field if non-nil, zero value otherwise.

### GetEventIdOk

`func (o *EventSignup) GetEventIdOk() (*EventDetails, bool)`

GetEventIdOk returns a tuple with the EventId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEventId

`func (o *EventSignup) SetEventId(v EventDetails)`

SetEventId sets EventId field to given value.


### GetShifts

`func (o *EventSignup) GetShifts() []EventDetails`

GetShifts returns the Shifts field if non-nil, zero value otherwise.

### GetShiftsOk

`func (o *EventSignup) GetShiftsOk() (*[]EventDetails, bool)`

GetShiftsOk returns a tuple with the Shifts field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetShifts

`func (o *EventSignup) SetShifts(v []EventDetails)`

SetShifts sets Shifts field to given value.

### HasShifts

`func (o *EventSignup) HasShifts() bool`

HasShifts returns a boolean if a field has been set.

### SetShiftsNil

`func (o *EventSignup) SetShiftsNil(b bool)`

 SetShiftsNil sets the value for Shifts to be an explicit nil

### UnsetShifts
`func (o *EventSignup) UnsetShifts()`

UnsetShifts ensures that no value is present for Shifts, not even an explicit nil
### GetRole

`func (o *EventSignup) GetRole() EventRole`

GetRole returns the Role field if non-nil, zero value otherwise.

### GetRoleOk

`func (o *EventSignup) GetRoleOk() (*EventRole, bool)`

GetRoleOk returns a tuple with the Role field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetRole

`func (o *EventSignup) SetRole(v EventRole)`

SetRole sets Role field to given value.

### HasRole

`func (o *EventSignup) HasRole() bool`

HasRole returns a boolean if a field has been set.

### GetStatus

`func (o *EventSignup) GetStatus() EventSignupStatus`

GetStatus returns the Status field if non-nil, zero value otherwise.

### GetStatusOk

`func (o *EventSignup) GetStatusOk() (*EventSignupStatus, bool)`

GetStatusOk returns a tuple with the Status field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStatus

`func (o *EventSignup) SetStatus(v EventSignupStatus)`

SetStatus sets Status field to given value.

### HasStatus

`func (o *EventSignup) HasStatus() bool`

HasStatus returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


