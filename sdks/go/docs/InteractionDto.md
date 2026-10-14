# InteractionDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**InteractionId** | Pointer to **string** | Optional ID used to identify a specific interaction.  This ID should only be provided in the initial request when re-sending data, and must use DDx-provided  interactionId value. If an existing ID is not provided to mark the interaction as a retry, Interactions API  will populate this ID field and include it in the response for future use if the interaction needs to be re-sent. | [optional] 
**Person** | Pointer to [**[]PersonIdentifier**](PersonIdentifier.md) | Optional array of person identifiers representing all IDs from any vendor system for the person interacted with. Each identifier can  contain an ID and type of ID indicating source system. If contact information for a person involved in the interaction is not provided, at least one ID is required.   A maximum of 100 IDs are allowed per interaction.  An ID of type &#39;VAN&#39; must be present if VAN is included as a destination, even if contact information is provided. Each person identifier type can appear at most once  in the array (i.e. no duplicate types are allowed). | [optional] 
**ContactInfo** | Pointer to [**ContactInfo**](ContactInfo.md) |  | [optional] 
**Channel** | Pointer to [**NullableInteractionDtoChannel**](InteractionDtoChannel.md) |  | [optional] 
**StateCode** | **string** | 2-character US state postal abbreviation (e.g., AL, WY).  Use \&quot;NA\&quot; when the state is unknown.  Must be a valid uppercase state code. | 
**AttemptDateTime** | **time.Time** | The date and time when the outreach attempt occurred, as reported by the vendor  and normalized to Coordinated Universal Time (UTC). | 
**Method** | [**ContactMethod**](ContactMethod.md) |  | 
**Committee** | [**[]CommitteeDetails**](CommitteeDetails.md) | Array of entities (campaign, state party, etc.) that conducted or logged the outreach attempt.  Committee objects consist of a type and an identifier, and at least one committee must be provided. | 
**Canvasser** | Pointer to [**[]CanvasserDetails**](CanvasserDetails.md) | Array of canvasser details for the individual who conducted the outreach attempt, as reported by the vendor.  Optional object containing identifier and identifier type. | [optional] 
**VendorSource** | **string** | Canonical name of the vendor or tool used to facilitate the outreach attempt.  This field reflects the platform through which the contact was made, not necessarily where the data was ingested from. | 
**Outcome** | [**Outcome**](Outcome.md) |  | 
**OutcomesDetailed** | Pointer to [**[]InteractionDtoOutcomesDetailedInner**](InteractionDtoOutcomesDetailedInner.md) | Optional array of objects that provide additional context around the results of an interaction, such as activist codes or survey responses.  If the type is recognized as an Activist Code Outcome (type &#x3D; \&quot;activist_code\&quot;),  Communication Consent Outcome (type &#x3D; \&quot;communication_consent\&quot;), Survey Response Outcome  (type &#x3D; \&quot;survey_response\&quot;), or Event Signup (type &#x3D; \&quot;event_signup\&quot;) it will be deserialized to that type.  If the type is unrecognized, it will be deserialized to an unvalidated, loosely typed object for flexibility. | [optional] 
**ThreadId** | Pointer to **NullableString** | Unique identifier for interactions that took place during the same conversation or set of conversations.  Used to group related interactions together. Maximum length of 100 characters. | [optional] 
**JsonMetadata** | Pointer to **NullableString** | Additional metadata in JSON format related to the interaction.  Must be valid JSON when provided. Can contain arbitrary structured data relevant to the interaction. | [optional] 
**VanFields** | Pointer to [**InteractionVanFieldsDto**](InteractionVanFieldsDto.md) |  | [optional] 
**Initiative** | Pointer to [**[]InitiativeDto**](InitiativeDto.md) | Optional array of initiatives associated with the interaction, such as campaign IDs.  Each initiative can contain a type and an identifier. | [optional] 

## Methods

### NewInteractionDto

`func NewInteractionDto(stateCode string, attemptDateTime time.Time, method ContactMethod, committee []CommitteeDetails, vendorSource string, outcome Outcome, ) *InteractionDto`

NewInteractionDto instantiates a new InteractionDto object
This constructor will assign default values to properties that have it defined,
and makes sure properties required by API are set, but the set of arguments
will change when the set of required properties is changed

### NewInteractionDtoWithDefaults

`func NewInteractionDtoWithDefaults() *InteractionDto`

NewInteractionDtoWithDefaults instantiates a new InteractionDto object
This constructor will only assign default values to properties that have it defined,
but it doesn't guarantee that properties required by API are set

### GetInteractionId

`func (o *InteractionDto) GetInteractionId() string`

GetInteractionId returns the InteractionId field if non-nil, zero value otherwise.

### GetInteractionIdOk

`func (o *InteractionDto) GetInteractionIdOk() (*string, bool)`

GetInteractionIdOk returns a tuple with the InteractionId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInteractionId

`func (o *InteractionDto) SetInteractionId(v string)`

SetInteractionId sets InteractionId field to given value.

### HasInteractionId

`func (o *InteractionDto) HasInteractionId() bool`

HasInteractionId returns a boolean if a field has been set.

### GetPerson

`func (o *InteractionDto) GetPerson() []PersonIdentifier`

GetPerson returns the Person field if non-nil, zero value otherwise.

### GetPersonOk

`func (o *InteractionDto) GetPersonOk() (*[]PersonIdentifier, bool)`

GetPersonOk returns a tuple with the Person field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetPerson

`func (o *InteractionDto) SetPerson(v []PersonIdentifier)`

SetPerson sets Person field to given value.

### HasPerson

`func (o *InteractionDto) HasPerson() bool`

HasPerson returns a boolean if a field has been set.

### SetPersonNil

`func (o *InteractionDto) SetPersonNil(b bool)`

 SetPersonNil sets the value for Person to be an explicit nil

### UnsetPerson
`func (o *InteractionDto) UnsetPerson()`

UnsetPerson ensures that no value is present for Person, not even an explicit nil
### GetContactInfo

`func (o *InteractionDto) GetContactInfo() ContactInfo`

GetContactInfo returns the ContactInfo field if non-nil, zero value otherwise.

### GetContactInfoOk

`func (o *InteractionDto) GetContactInfoOk() (*ContactInfo, bool)`

GetContactInfoOk returns a tuple with the ContactInfo field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetContactInfo

`func (o *InteractionDto) SetContactInfo(v ContactInfo)`

SetContactInfo sets ContactInfo field to given value.

### HasContactInfo

`func (o *InteractionDto) HasContactInfo() bool`

HasContactInfo returns a boolean if a field has been set.

### GetChannel

`func (o *InteractionDto) GetChannel() InteractionDtoChannel`

GetChannel returns the Channel field if non-nil, zero value otherwise.

### GetChannelOk

`func (o *InteractionDto) GetChannelOk() (*InteractionDtoChannel, bool)`

GetChannelOk returns a tuple with the Channel field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetChannel

`func (o *InteractionDto) SetChannel(v InteractionDtoChannel)`

SetChannel sets Channel field to given value.

### HasChannel

`func (o *InteractionDto) HasChannel() bool`

HasChannel returns a boolean if a field has been set.

### SetChannelNil

`func (o *InteractionDto) SetChannelNil(b bool)`

 SetChannelNil sets the value for Channel to be an explicit nil

### UnsetChannel
`func (o *InteractionDto) UnsetChannel()`

UnsetChannel ensures that no value is present for Channel, not even an explicit nil
### GetStateCode

`func (o *InteractionDto) GetStateCode() string`

GetStateCode returns the StateCode field if non-nil, zero value otherwise.

### GetStateCodeOk

`func (o *InteractionDto) GetStateCodeOk() (*string, bool)`

GetStateCodeOk returns a tuple with the StateCode field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetStateCode

`func (o *InteractionDto) SetStateCode(v string)`

SetStateCode sets StateCode field to given value.


### GetAttemptDateTime

`func (o *InteractionDto) GetAttemptDateTime() time.Time`

GetAttemptDateTime returns the AttemptDateTime field if non-nil, zero value otherwise.

### GetAttemptDateTimeOk

`func (o *InteractionDto) GetAttemptDateTimeOk() (*time.Time, bool)`

GetAttemptDateTimeOk returns a tuple with the AttemptDateTime field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetAttemptDateTime

`func (o *InteractionDto) SetAttemptDateTime(v time.Time)`

SetAttemptDateTime sets AttemptDateTime field to given value.


### GetMethod

`func (o *InteractionDto) GetMethod() ContactMethod`

GetMethod returns the Method field if non-nil, zero value otherwise.

### GetMethodOk

`func (o *InteractionDto) GetMethodOk() (*ContactMethod, bool)`

GetMethodOk returns a tuple with the Method field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetMethod

`func (o *InteractionDto) SetMethod(v ContactMethod)`

SetMethod sets Method field to given value.


### GetCommittee

`func (o *InteractionDto) GetCommittee() []CommitteeDetails`

GetCommittee returns the Committee field if non-nil, zero value otherwise.

### GetCommitteeOk

`func (o *InteractionDto) GetCommitteeOk() (*[]CommitteeDetails, bool)`

GetCommitteeOk returns a tuple with the Committee field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCommittee

`func (o *InteractionDto) SetCommittee(v []CommitteeDetails)`

SetCommittee sets Committee field to given value.


### GetCanvasser

`func (o *InteractionDto) GetCanvasser() []CanvasserDetails`

GetCanvasser returns the Canvasser field if non-nil, zero value otherwise.

### GetCanvasserOk

`func (o *InteractionDto) GetCanvasserOk() (*[]CanvasserDetails, bool)`

GetCanvasserOk returns a tuple with the Canvasser field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetCanvasser

`func (o *InteractionDto) SetCanvasser(v []CanvasserDetails)`

SetCanvasser sets Canvasser field to given value.

### HasCanvasser

`func (o *InteractionDto) HasCanvasser() bool`

HasCanvasser returns a boolean if a field has been set.

### SetCanvasserNil

`func (o *InteractionDto) SetCanvasserNil(b bool)`

 SetCanvasserNil sets the value for Canvasser to be an explicit nil

### UnsetCanvasser
`func (o *InteractionDto) UnsetCanvasser()`

UnsetCanvasser ensures that no value is present for Canvasser, not even an explicit nil
### GetVendorSource

`func (o *InteractionDto) GetVendorSource() string`

GetVendorSource returns the VendorSource field if non-nil, zero value otherwise.

### GetVendorSourceOk

`func (o *InteractionDto) GetVendorSourceOk() (*string, bool)`

GetVendorSourceOk returns a tuple with the VendorSource field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVendorSource

`func (o *InteractionDto) SetVendorSource(v string)`

SetVendorSource sets VendorSource field to given value.


### GetOutcome

`func (o *InteractionDto) GetOutcome() Outcome`

GetOutcome returns the Outcome field if non-nil, zero value otherwise.

### GetOutcomeOk

`func (o *InteractionDto) GetOutcomeOk() (*Outcome, bool)`

GetOutcomeOk returns a tuple with the Outcome field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutcome

`func (o *InteractionDto) SetOutcome(v Outcome)`

SetOutcome sets Outcome field to given value.


### GetOutcomesDetailed

`func (o *InteractionDto) GetOutcomesDetailed() []InteractionDtoOutcomesDetailedInner`

GetOutcomesDetailed returns the OutcomesDetailed field if non-nil, zero value otherwise.

### GetOutcomesDetailedOk

`func (o *InteractionDto) GetOutcomesDetailedOk() (*[]InteractionDtoOutcomesDetailedInner, bool)`

GetOutcomesDetailedOk returns a tuple with the OutcomesDetailed field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetOutcomesDetailed

`func (o *InteractionDto) SetOutcomesDetailed(v []InteractionDtoOutcomesDetailedInner)`

SetOutcomesDetailed sets OutcomesDetailed field to given value.

### HasOutcomesDetailed

`func (o *InteractionDto) HasOutcomesDetailed() bool`

HasOutcomesDetailed returns a boolean if a field has been set.

### SetOutcomesDetailedNil

`func (o *InteractionDto) SetOutcomesDetailedNil(b bool)`

 SetOutcomesDetailedNil sets the value for OutcomesDetailed to be an explicit nil

### UnsetOutcomesDetailed
`func (o *InteractionDto) UnsetOutcomesDetailed()`

UnsetOutcomesDetailed ensures that no value is present for OutcomesDetailed, not even an explicit nil
### GetThreadId

`func (o *InteractionDto) GetThreadId() string`

GetThreadId returns the ThreadId field if non-nil, zero value otherwise.

### GetThreadIdOk

`func (o *InteractionDto) GetThreadIdOk() (*string, bool)`

GetThreadIdOk returns a tuple with the ThreadId field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetThreadId

`func (o *InteractionDto) SetThreadId(v string)`

SetThreadId sets ThreadId field to given value.

### HasThreadId

`func (o *InteractionDto) HasThreadId() bool`

HasThreadId returns a boolean if a field has been set.

### SetThreadIdNil

`func (o *InteractionDto) SetThreadIdNil(b bool)`

 SetThreadIdNil sets the value for ThreadId to be an explicit nil

### UnsetThreadId
`func (o *InteractionDto) UnsetThreadId()`

UnsetThreadId ensures that no value is present for ThreadId, not even an explicit nil
### GetJsonMetadata

`func (o *InteractionDto) GetJsonMetadata() string`

GetJsonMetadata returns the JsonMetadata field if non-nil, zero value otherwise.

### GetJsonMetadataOk

`func (o *InteractionDto) GetJsonMetadataOk() (*string, bool)`

GetJsonMetadataOk returns a tuple with the JsonMetadata field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetJsonMetadata

`func (o *InteractionDto) SetJsonMetadata(v string)`

SetJsonMetadata sets JsonMetadata field to given value.

### HasJsonMetadata

`func (o *InteractionDto) HasJsonMetadata() bool`

HasJsonMetadata returns a boolean if a field has been set.

### SetJsonMetadataNil

`func (o *InteractionDto) SetJsonMetadataNil(b bool)`

 SetJsonMetadataNil sets the value for JsonMetadata to be an explicit nil

### UnsetJsonMetadata
`func (o *InteractionDto) UnsetJsonMetadata()`

UnsetJsonMetadata ensures that no value is present for JsonMetadata, not even an explicit nil
### GetVanFields

`func (o *InteractionDto) GetVanFields() InteractionVanFieldsDto`

GetVanFields returns the VanFields field if non-nil, zero value otherwise.

### GetVanFieldsOk

`func (o *InteractionDto) GetVanFieldsOk() (*InteractionVanFieldsDto, bool)`

GetVanFieldsOk returns a tuple with the VanFields field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetVanFields

`func (o *InteractionDto) SetVanFields(v InteractionVanFieldsDto)`

SetVanFields sets VanFields field to given value.

### HasVanFields

`func (o *InteractionDto) HasVanFields() bool`

HasVanFields returns a boolean if a field has been set.

### GetInitiative

`func (o *InteractionDto) GetInitiative() []InitiativeDto`

GetInitiative returns the Initiative field if non-nil, zero value otherwise.

### GetInitiativeOk

`func (o *InteractionDto) GetInitiativeOk() (*[]InitiativeDto, bool)`

GetInitiativeOk returns a tuple with the Initiative field if it's non-nil, zero value otherwise
and a boolean to check if the value has been set.

### SetInitiative

`func (o *InteractionDto) SetInitiative(v []InitiativeDto)`

SetInitiative sets Initiative field to given value.

### HasInitiative

`func (o *InteractionDto) HasInitiative() bool`

HasInitiative returns a boolean if a field has been set.

### SetInitiativeNil

`func (o *InteractionDto) SetInitiativeNil(b bool)`

 SetInitiativeNil sets the value for Initiative to be an explicit nil

### UnsetInitiative
`func (o *InteractionDto) UnsetInitiative()`

UnsetInitiative ensures that no value is present for Initiative, not even an explicit nil

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


