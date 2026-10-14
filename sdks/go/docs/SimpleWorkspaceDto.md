# SimpleWorkspaceDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**WorkspaceId** | **int32** | Unique identifier for the workspace | 
**DisplayName** | **string** | Display name for the workspace | 
**Type** | [**WorkspaceTypeDto**](WorkspaceTypeDto.md) |  | 

## Methods

### NewSimpleWorkspaceDto

`func NewSimpleWorkspaceDto(workspaceId int32, displayName string, type_ WorkspaceTypeDto, ) *SimpleWorkspaceDto`

NewSimpleWorkspaceDto instantiates a new SimpleWorkspaceDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewSimpleWorkspaceDtoWithDefaults

`func NewSimpleWorkspaceDtoWithDefaults() *SimpleWorkspaceDto`

NewSimpleWorkspaceDtoWithDefaults instantiates a new SimpleWorkspaceDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetWorkspaceId

`func (o *SimpleWorkspaceDto) GetWorkspaceId() int32`

GetWorkspaceId returns the WorkspaceId field if non-nil, zero value otherwise.

### GetWorkspaceIdOk

`func (o *SimpleWorkspaceDto) GetWorkspaceIdOk() (*int32, bool)`

GetWorkspaceIdOk returns a tuple with the WorkspaceId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetWorkspaceId

`func (o *SimpleWorkspaceDto) SetWorkspaceId(v int32)`

SetWorkspaceId sets WorkspaceId field to given value.


### GetDisplayName

`func (o *SimpleWorkspaceDto) GetDisplayName() string`

GetDisplayName returns the DisplayName field if non-nil, zero value otherwise.

### GetDisplayNameOk

`func (o *SimpleWorkspaceDto) GetDisplayNameOk() (*string, bool)`

GetDisplayNameOk returns a tuple with the DisplayName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetDisplayName

`func (o *SimpleWorkspaceDto) SetDisplayName(v string)`

SetDisplayName sets DisplayName field to given value.


### GetType

`func (o *SimpleWorkspaceDto) GetType() WorkspaceTypeDto`

GetType returns the Type field if non-nil, zero value otherwise.

### GetTypeOk

`func (o *SimpleWorkspaceDto) GetTypeOk() (*WorkspaceTypeDto, bool)`

GetTypeOk returns a tuple with the Type field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetType

`func (o *SimpleWorkspaceDto) SetType(v WorkspaceTypeDto)`

SetType sets Type field to given value.



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


