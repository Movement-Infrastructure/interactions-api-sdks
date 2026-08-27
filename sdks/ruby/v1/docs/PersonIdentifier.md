# DdxInteractionsApi::PersonIdentifier

## Properties

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | **String** | A primary identifier for tracking individual voters. This can be an integer (e.g. for DNC person_ids),  a string (for UUIDs, phone numbers), or other identifier formats depending on the source system.  Used to link voter records across different data sources and track in-state voter history over time. |  |
| **type** | **String** | Type of identifier or source system that generated the id.  Examples include \&quot;VAN\&quot;, \&quot;phone\&quot;, \&quot;slimCRM\&quot;, \&quot;DNC\&quot;, \&quot;SOS\&quot;, etc.   This field indicates the origin or authority of the person identifier. |  |

## Example

```ruby
require 'ddx_interactions_api'

instance = DdxInteractionsApi::PersonIdentifier.new(
  id: null,
  type: null
)
```

