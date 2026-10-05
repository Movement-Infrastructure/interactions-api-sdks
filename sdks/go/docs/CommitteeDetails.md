# CommitteeDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | Type of the committee identifier specified in &#39;id&#39;, representing the source context of the interaction. | 
**Id** | **string** | The actual committee identifier itself. | 

## Methods

### NewCommitteeDetails

`func NewCommitteeDetails(type_ string, id string, ) *CommitteeDetails`

NewCommitteeDetails instantiates a new CommitteeDetails object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewCommitteeDetailsWithDefaults

`func NewCommitteeDetailsWithDefaults() *CommitteeDetails`

NewCommitteeDetailsWithDefaults instantiates a new CommitteeDetails object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *CommitteeDetails) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *CommitteeDetails) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *CommitteeDetails) SetType(v string)`

SetType sets Type field to given value.


### GetId

`func (o *CommitteeDetails) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *CommitteeDetails) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *CommitteeDetails) SetId(v string)`

SetId sets Id field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


