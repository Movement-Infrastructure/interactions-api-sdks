# CanvasserDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Type of the canvasser identifier specified in &#39;id&#39;.  Required when Canvasser is provided. | 
**Id** | **string** | The actual canvasser identifier used during the outreach attempt.  Examples: user ID, employee number, volunteer ID, etc.  Required when Canvasser is provided. | 

## Methods

### NewCanvasserDetails

`func NewCanvasserDetails(type_ string, id string, ) *CanvasserDetails`

NewCanvasserDetails instantiates a new CanvasserDetails object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCanvasserDetailsWithDefaults

`func NewCanvasserDetailsWithDefaults() *CanvasserDetails`

NewCanvasserDetailsWithDefaults instantiates a new CanvasserDetails object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *CanvasserDetails) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *CanvasserDetails) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *CanvasserDetails) SetType(v string)`

SetType sets Type field to given value.


### GetId

`func (o *CanvasserDetails) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *CanvasserDetails) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *CanvasserDetails) SetId(v string)`

SetId sets Id field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


