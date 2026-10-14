# ContactInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**Email** | Pointer to **[]string** | Email addresses of the person being interacted with. | [optional] 
**Phone** | Pointer to **[]string** | Phone numbers of the person being interacted with. Should be in E.164 format (e.g. +1234567890). | [optional] 
**Address** | Pointer to [**[]Address**](Address.md) | Physical addresses of the person being interacted with. | [optional] 
**FirstName** | Pointer to **NullableString** | Optional first name field for person being interacted with. | [optional] 
**MiddleName** | Pointer to **NullableString** | Optional middle name field for person being interacted with. | [optional] 
**LastName** | Pointer to **NullableString** | Optional last name field for person being interacted with. | [optional] 
**SocialHandle** | Pointer to **[]string** | Optional social media handles for person being interacted with. | [optional] 

## Methods

### NewContactInfo

`func NewContactInfo() *ContactInfo`

NewContactInfo instantiates a new ContactInfo object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewContactInfoWithDefaults

`func NewContactInfoWithDefaults() *ContactInfo`

NewContactInfoWithDefaults instantiates a new ContactInfo object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetEmail

`func (o *ContactInfo) GetEmail() []string`

GetEmail returns the Email field if non-nil, zero value otherwise.

### GetEmailOk

`func (o *ContactInfo) GetEmailOk() (*[]string, bool)`

GetEmailOk returns a tuple with the Email field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetEmail

`func (o *ContactInfo) SetEmail(v []string)`

SetEmail sets Email field to given value.

### HasEmail

`func (o *ContactInfo) HasEmail() bool`

HasEmail returns a boolean if a field has been set.

### SetEmailNil

`func (o *ContactInfo) SetEmailNil(b bool)`

 SetEmailNil sets the value for Email to be an explicit nil

### UnsetEmail
`func (o *ContactInfo) UnsetEmail()`

UnsetEmail ensures that no value is present for Email, not even an explicit nil
### GetPhone

`func (o *ContactInfo) GetPhone() []string`

GetPhone returns the Phone field if non-nil, zero value otherwise.

### GetPhoneOk

`func (o *ContactInfo) GetPhoneOk() (*[]string, bool)`

GetPhoneOk returns a tuple with the Phone field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPhone

`func (o *ContactInfo) SetPhone(v []string)`

SetPhone sets Phone field to given value.

### HasPhone

`func (o *ContactInfo) HasPhone() bool`

HasPhone returns a boolean if a field has been set.

### SetPhoneNil

`func (o *ContactInfo) SetPhoneNil(b bool)`

 SetPhoneNil sets the value for Phone to be an explicit nil

### UnsetPhone
`func (o *ContactInfo) UnsetPhone()`

UnsetPhone ensures that no value is present for Phone, not even an explicit nil
### GetAddress

`func (o *ContactInfo) GetAddress() []Address`

GetAddress returns the Address field if non-nil, zero value otherwise.

### GetAddressOk

`func (o *ContactInfo) GetAddressOk() (*[]Address, bool)`

GetAddressOk returns a tuple with the Address field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAddress

`func (o *ContactInfo) SetAddress(v []Address)`

SetAddress sets Address field to given value.

### HasAddress

`func (o *ContactInfo) HasAddress() bool`

HasAddress returns a boolean if a field has been set.

### SetAddressNil

`func (o *ContactInfo) SetAddressNil(b bool)`

 SetAddressNil sets the value for Address to be an explicit nil

### UnsetAddress
`func (o *ContactInfo) UnsetAddress()`

UnsetAddress ensures that no value is present for Address, not even an explicit nil
### GetFirstName

`func (o *ContactInfo) GetFirstName() string`

GetFirstName returns the FirstName field if non-nil, zero value otherwise.

### GetFirstNameOk

`func (o *ContactInfo) GetFirstNameOk() (*string, bool)`

GetFirstNameOk returns a tuple with the FirstName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetFirstName

`func (o *ContactInfo) SetFirstName(v string)`

SetFirstName sets FirstName field to given value.

### HasFirstName

`func (o *ContactInfo) HasFirstName() bool`

HasFirstName returns a boolean if a field has been set.

### SetFirstNameNil

`func (o *ContactInfo) SetFirstNameNil(b bool)`

 SetFirstNameNil sets the value for FirstName to be an explicit nil

### UnsetFirstName
`func (o *ContactInfo) UnsetFirstName()`

UnsetFirstName ensures that no value is present for FirstName, not even an explicit nil
### GetMiddleName

`func (o *ContactInfo) GetMiddleName() string`

GetMiddleName returns the MiddleName field if non-nil, zero value otherwise.

### GetMiddleNameOk

`func (o *ContactInfo) GetMiddleNameOk() (*string, bool)`

GetMiddleNameOk returns a tuple with the MiddleName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMiddleName

`func (o *ContactInfo) SetMiddleName(v string)`

SetMiddleName sets MiddleName field to given value.

### HasMiddleName

`func (o *ContactInfo) HasMiddleName() bool`

HasMiddleName returns a boolean if a field has been set.

### SetMiddleNameNil

`func (o *ContactInfo) SetMiddleNameNil(b bool)`

 SetMiddleNameNil sets the value for MiddleName to be an explicit nil

### UnsetMiddleName
`func (o *ContactInfo) UnsetMiddleName()`

UnsetMiddleName ensures that no value is present for MiddleName, not even an explicit nil
### GetLastName

`func (o *ContactInfo) GetLastName() string`

GetLastName returns the LastName field if non-nil, zero value otherwise.

### GetLastNameOk

`func (o *ContactInfo) GetLastNameOk() (*string, bool)`

GetLastNameOk returns a tuple with the LastName field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetLastName

`func (o *ContactInfo) SetLastName(v string)`

SetLastName sets LastName field to given value.

### HasLastName

`func (o *ContactInfo) HasLastName() bool`

HasLastName returns a boolean if a field has been set.

### SetLastNameNil

`func (o *ContactInfo) SetLastNameNil(b bool)`

 SetLastNameNil sets the value for LastName to be an explicit nil

### UnsetLastName
`func (o *ContactInfo) UnsetLastName()`

UnsetLastName ensures that no value is present for LastName, not even an explicit nil
### GetSocialHandle

`func (o *ContactInfo) GetSocialHandle() []string`

GetSocialHandle returns the SocialHandle field if non-nil, zero value otherwise.

### GetSocialHandleOk

`func (o *ContactInfo) GetSocialHandleOk() (*[]string, bool)`

GetSocialHandleOk returns a tuple with the SocialHandle field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetSocialHandle

`func (o *ContactInfo) SetSocialHandle(v []string)`

SetSocialHandle sets SocialHandle field to given value.

### HasSocialHandle

`func (o *ContactInfo) HasSocialHandle() bool`

HasSocialHandle returns a boolean if a field has been set.

### SetSocialHandleNil

`func (o *ContactInfo) SetSocialHandleNil(b bool)`

 SetSocialHandleNil sets the value for SocialHandle to be an explicit nil

### UnsetSocialHandle
`func (o *ContactInfo) UnsetSocialHandle()`

UnsetSocialHandle ensures that no value is present for SocialHandle, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


