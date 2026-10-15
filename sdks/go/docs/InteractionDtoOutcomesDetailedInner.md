# InteractionDtoOutcomesDetailedInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Type** | **string** | This field categorizes the type of detailed outcome information being provided. | 
**Value** | **map[string]interface{}** |  | 
**Operation** | Pointer to [**OutcomeDetailOperation**](OutcomeDetailOperation.md) |  | [optional] 

## Methods

### NewInteractionDtoOutcomesDetailedInner

`func NewInteractionDtoOutcomesDetailedInner(type_ string, value map[string]interface{}, ) *InteractionDtoOutcomesDetailedInner`

NewInteractionDtoOutcomesDetailedInner instantiates a new InteractionDtoOutcomesDetailedInner object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInteractionDtoOutcomesDetailedInnerWithDefaults

`func NewInteractionDtoOutcomesDetailedInnerWithDefaults() *InteractionDtoOutcomesDetailedInner`

NewInteractionDtoOutcomesDetailedInnerWithDefaults instantiates a new InteractionDtoOutcomesDetailedInner object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetType

`func (o *InteractionDtoOutcomesDetailedInner) GetType() string`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *InteractionDtoOutcomesDetailedInner) GetTypeOk() (*string, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *InteractionDtoOutcomesDetailedInner) SetType(v string)`

SetType sets Type field to given value.


### GetValue

`func (o *InteractionDtoOutcomesDetailedInner) GetValue() map[string]interface{}`

GetValue returns the Value field if non-nil, zero value otherwise.

### GetValueOk

`func (o *InteractionDtoOutcomesDetailedInner) GetValueOk() (*map[string]interface{}, bool)`

GetValueOk returns a tuple with the Value field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetValue

`func (o *InteractionDtoOutcomesDetailedInner) SetValue(v map[string]interface{})`

SetValue sets Value field to given value.


### GetOperation

`func (o *InteractionDtoOutcomesDetailedInner) GetOperation() OutcomeDetailOperation`

GetOperation returns the Operation field if non-nil, zero value otherwise.

### GetOperationOk

`func (o *InteractionDtoOutcomesDetailedInner) GetOperationOk() (*OutcomeDetailOperation, bool)`

GetOperationOk returns a tuple with the Operation field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOperation

`func (o *InteractionDtoOutcomesDetailedInner) SetOperation(v OutcomeDetailOperation)`

SetOperation sets Operation field to given value.

### HasOperation

`func (o *InteractionDtoOutcomesDetailedInner) HasOperation() bool`

HasOperation returns a boolean if a field has been set.


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


