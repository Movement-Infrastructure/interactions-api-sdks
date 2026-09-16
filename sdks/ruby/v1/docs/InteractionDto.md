# DdxInteractionsApi::InteractionDto

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **interaction_id** | **String** | Optional ID used to identify a specific interaction.  This ID should only be provided in the initial request when re-sending data, and must use DDx-provided  interactionId value. If an existing ID is not provided to mark the interaction as a retry, Interactions API  will populate this ID field and include it in the response for future use if the interaction needs to be re-sent. | [optional] |
| **person** | [**Array&lt;PersonIdentifier&gt;**](PersonIdentifier.md) | Optional array of person identifiers representing all IDs from any vendor system for the person interacted with. Each identifier can  contain an ID and type of ID indicating source system. If contact information for a person involved in the interaction is not provided, at least one ID is required.   A maximum of 100 IDs are allowed per interaction.  An ID of type &#39;VAN&#39; must be present if VAN is included as a destination, even if contact information is provided. Each person identifier type can appear at most once  in the array (i.e. no duplicate types are allowed). | [optional] |
| **contact_info** | [**ContactInfo**](ContactInfo.md) |  | [optional] |
| **channel** | [**InteractionDtoChannel**](InteractionDtoChannel.md) |  | [optional] |
| **state_code** | **String** | 2-character US state postal abbreviation (e.g., AL, WY).  Use \&quot;NA\&quot; when the state is unknown.  Must be a valid uppercase state code. |  |
| **attempt_date_time** | **Time** | The date and time when the outreach attempt occurred, as reported by the vendor  and normalized to Coordinated Universal Time (UTC). |  |
| **method** | [**ContactMethod**](ContactMethod.md) |  |  |
| **committee** | [**Array&lt;CommitteeDetails&gt;**](CommitteeDetails.md) | Array of entities (campaign, state party, etc.) that conducted or logged the outreach attempt.  Committee objects consist of a type and an identifier, and at least one committee must be provided. |  |
| **canvasser** | [**Array&lt;CanvasserDetails&gt;**](CanvasserDetails.md) | Array of canvasser details for the individual who conducted the outreach attempt, as reported by the vendor.  Optional object containing identifier and identifier type. | [optional] |
| **vendor_source** | **String** | Canonical name of the vendor or tool used to facilitate the outreach attempt.  This field reflects the platform through which the contact was made, not necessarily where the data was ingested from. |  |
| **outcome** | [**Outcome**](Outcome.md) |  |  |
| **outcomes_detailed** | [**Array&lt;InteractionDtoOutcomesDetailedInner&gt;**](InteractionDtoOutcomesDetailedInner.md) | Optional array of objects that provide additional context around the results of an interaction, such as activist codes or survey responses.  If the type is recognized as an Activist Code Outcome (type &#x3D; \&quot;activist_code\&quot;),  Communication Consent Outcome (type &#x3D; \&quot;communication_consent\&quot;), Survey Response Outcome  (type &#x3D; \&quot;survey_response\&quot;), or Event Signup (type &#x3D; \&quot;event_signup\&quot;) it will be deserialized to that type.  If the type is unrecognized, it will be deserialized to an unvalidated, loosely typed object for flexibility. | [optional] |
| **thread_id** | **String** | Unique identifier for interactions that took place during the same conversation or set of conversations.  Used to group related interactions together. Maximum length of 100 characters. | [optional] |
| **json_metadata** | **String** | Additional metadata in JSON format related to the interaction.  Must be valid JSON when provided. Can contain arbitrary structured data relevant to the interaction. | [optional] |
| **van_fields** | [**InteractionVanFieldsDto**](InteractionVanFieldsDto.md) |  | [optional] |
| **initiative** | [**Array&lt;InitiativeDto&gt;**](InitiativeDto.md) | Optional array of initiatives associated with the interaction, such as campaign IDs.  Each initiative can contain a type and an identifier. | [optional] |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::InteractionDto.new(
  interaction_id: null,
  person: null,
  contact_info: null,
  channel: null,
  state_code: null,
  attempt_date_time: null,
  method: null,
  committee: null,
  canvasser: null,
  vendor_source: null,
  outcome: null,
  outcomes_detailed: null,
  thread_id: null,
  json_metadata: null,
  van_fields: null,
  initiative: null
)
```

