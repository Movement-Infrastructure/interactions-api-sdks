# DynamicChannelDetails
## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
| **id** | **String** | Optional; unique identifier for any known id for the channel &#x60;type&#x60; | [optional] [default to null] |
| **type** | **String** | Type of the channel specified in &#39;value&#39;. Required when Channel is provided.                Recognized types:  - \&quot;phone_number\&quot;: Indicates &#x60;value&#x60; is a phone number; &#x60;value&#x60; must be in E.164 format (e.g., +14155552671).  - \&quot;email\&quot;: Indicates &#x60;value&#x60; is an email address.  - [any other identifier]: Any type not listed above. &#x60;value&#x60; can be a string, an int or an arbitrary object. | [optional] [default to null] |
| **value** | [**oas_any_type_not_mapped**](.md) |  The actual channel used during the outreach attempt. This field can be provided as a string or int though only the object form is shown here.   Examples: +14155552671, name@org.org, @handle.   Required when Channel is provided. | [optional] [default to null] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

