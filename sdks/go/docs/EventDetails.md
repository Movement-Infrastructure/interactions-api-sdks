# EventDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | The identifier value | 
**Type** | **string** | The namespace the id belongs to, scoped to the field this object appears in: an event namespace in event_id (e.g. \&quot;vendor_event_id\&quot;, \&quot;vendor_signup_id\&quot;), or a shift namespace in shifts (e.g. \&quot;vendor_shift_id\&quot;). | 

## Methods

### NewEventDetails

`func NewEventDetails(id string, type_ string, ) *EventDetails`

NewEventDetails instantiates a new EventDetails object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewEventDetailsWithDefaults

`func NewEventDetailsWithDefaults() *EventDetails`

NewEventDetailsWithDefaults instantiates a new EventDetails object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *EventDetails) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *EventDetails) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *EventDetails) SetId(v string)`

SetId sets Id field to given value.


### GetType

`func (o *EventDetails) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *EventDetails) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *EventDetails) SetType(v string)`

SetType sets Type field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


