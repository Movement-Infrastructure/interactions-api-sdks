# PersonIdentifier

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Id** | **string** | A primary identifier for tracking individual voters. This can be an integer (e.g. for DNC person_ids),  a string (for UUIDs, phone numbers), or other identifier formats depending on the source system.  Used to link voter records across different data sources and track in-state voter history over time. | 
**Type** | **string** | Type of identifier or source system that generated the id.  Examples include \&quot;VAN\&quot;, \&quot;phone\&quot;, \&quot;slimCRM\&quot;, \&quot;DNC\&quot;, \&quot;SOS\&quot;, etc.   This field indicates the origin or authority of the person identifier. | 

## Methods

### NewPersonIdentifier

`func NewPersonIdentifier(id string, type_ string, ) *PersonIdentifier`

NewPersonIdentifier instantiates a new PersonIdentifier object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewPersonIdentifierWithDefaults

`func NewPersonIdentifierWithDefaults() *PersonIdentifier`

NewPersonIdentifierWithDefaults instantiates a new PersonIdentifier object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetId

`func (o *PersonIdentifier) GetId() string`

GetId returns the Id field if non-nil, zero value otherwise.

### GetIdOk

`func (o *PersonIdentifier) GetIdOk() (*string, bool)`

GetIdOk returns a tuple with the Id field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetId

`func (o *PersonIdentifier) SetId(v string)`

SetId sets Id field to given value.


### GetType

`func (o *PersonIdentifier) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *PersonIdentifier) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *PersonIdentifier) SetType(v string)`

SetType sets Type field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


