# InteractionDto

Represents a single interaction record containing voter outreach attempt data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interaction_id** | **str** | Optional ID used to identify a specific interaction.  This ID should only be provided in the initial request when re-sending data, and must use DDx-provided  interactionId value. If an existing ID is not provided to mark the interaction as a retry, Interactions API  will populate this ID field and include it in the response for future use if the interaction needs to be re-sent. | [optional] 
**person** | [**List[PersonIdentifier]**](PersonIdentifier.md) | Optional array of person identifiers representing all IDs from any vendor system for the person interacted with. Each identifier can  contain an ID and type of ID indicating source system. If contact information for a person involved in the interaction is not provided, at least one ID is required.   A maximum of 100 IDs are allowed per interaction.  An ID of type &#39;VAN&#39; must be present if VAN is included as a destination, even if contact information is provided. Each person identifier type can appear at most once  in the array (i.e. no duplicate types are allowed). | [optional] 
**contact_info** | [**ContactInfo**](ContactInfo.md) |  | [optional] 
**channel** | [**InteractionDtoChannel**](InteractionDtoChannel.md) |  | [optional] 
**state_code** | **str** | 2-character US state postal abbreviation (e.g., AL, WY).  Must be a valid uppercase state code. | 
**attempt_date_time** | **datetime** | The date and time when the outreach attempt occurred, as reported by the vendor  and normalized to Coordinated Universal Time (UTC). | 
**method** | [**ContactMethod**](ContactMethod.md) |  | 
**committee** | [**List[CommitteeDetails]**](CommitteeDetails.md) | Array of entities (campaign, state party, etc.) that conducted or logged the outreach attempt.  Committee objects consist of a type and an identifier, and at least one committee must be provided. | 
**canvasser** | [**List[CanvasserDetails]**](CanvasserDetails.md) | Array of canvasser details for the individual who conducted the outreach attempt, as reported by the vendor.  Optional object containing identifier and identifier type. | [optional] 
**vendor_source** | **str** | Canonical name of the vendor or tool used to facilitate the outreach attempt.  This field reflects the platform through which the contact was made, not necessarily where the data was ingested from. | 
**outcome** | [**Outcome**](Outcome.md) |  | 
**outcomes_detailed** | [**List[InteractionDtoOutcomesDetailedInner]**](InteractionDtoOutcomesDetailedInner.md) | Optional array of objects that provide additional context around the results of an interaction, such as activist codes or survey responses.  If the type is recognized as an Activist Code Outcome (type &#x3D; \&quot;activist_code\&quot;),  Communication Consent Outcome (type &#x3D; \&quot;communication_consent\&quot;), or Survey Response Outcome  (type &#x3D; \&quot;survey_response\&quot;) it will be deserialized to that type.  If the type is unrecognized, it will be deserialized to an unvalidated, loosely typed object for flexibility. | [optional] 
**thread_id** | **str** | Unique identifier for interactions that took place during the same conversation or set of conversations.  Used to group related interactions together. Maximum length of 100 characters. | [optional] 
**json_metadata** | **str** | Additional metadata in JSON format related to the interaction.  Must be valid JSON when provided. Can contain arbitrary structured data relevant to the interaction. | [optional] 
**van_fields** | [**InteractionVanFieldsDto**](InteractionVanFieldsDto.md) |  | [optional] 
**initiative** | [**List[InitiativeDto]**](InitiativeDto.md) | Optional array of initiatives associated with the interaction, such as campaign IDs.  Each initiative can contain a type and an identifier. | [optional] 

## Example

```python
from mig_interactions_api.models.interaction_dto import InteractionDto

# TODO update the JSON string below
json = "{}"
# create an instance of InteractionDto from a JSON string
interaction_dto_instance = InteractionDto.from_json(json)
# print the JSON string representation of the object
print(InteractionDto.to_json())

# convert the object into a dict
interaction_dto_dict = interaction_dto_instance.to_dict()
# create an instance of InteractionDto from a dict
interaction_dto_from_dict = InteractionDto.from_dict(interaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


