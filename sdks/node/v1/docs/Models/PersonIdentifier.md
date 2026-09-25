# PersonIdentifier
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **String** | A primary identifier for tracking individual voters. This can be an integer (e.g. for DNC person_ids),  a string (for UUIDs, phone numbers), or other identifier formats depending on the source system.  Used to link voter records across different data sources and track in-state voter history over time. | [default to null] |
| **type** | **String** | Type of identifier or source system that generated the id.  Examples include \&quot;VAN\&quot;, \&quot;phone\&quot;, \&quot;slimCRM\&quot;, \&quot;DNC\&quot;, \&quot;SOS\&quot;, etc.   This field indicates the origin or authority of the person identifier. | [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

