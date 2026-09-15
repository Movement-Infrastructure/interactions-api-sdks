# DdxInteractionsApi::InteractionDtoChannel

## Class instance methods

### `openapi_one_of`

Returns the list of classes defined in oneOf.

#### Example

```ruby
require 'ddx_interactions_api'

DdxInteractionsApi::InteractionDtoChannel.openapi_one_of
# =>
# [
#   :'AddressChannelDetails',
#   :'DynamicChannelDetails'
# ]
```

### `openapi_discriminator_name`

Returns the discriminator's property name.

#### Example

```ruby
require 'ddx_interactions_api'

DdxInteractionsApi::InteractionDtoChannel.openapi_discriminator_name
# => :'type'
```

### `openapi_discriminator_name`

Returns the discriminator's mapping.

#### Example

```ruby
require 'ddx_interactions_api'

DdxInteractionsApi::InteractionDtoChannel.openapi_discriminator_mapping
# =>
# {
#   :'address' => :'AddressChannelDetails',
#   :'example_type' => :'DynamicChannelDetails'
# }
```

### build

Find the appropriate object from the `openapi_one_of` list and casts the data into it.

#### Example

```ruby
require 'ddx_interactions_api'

DdxInteractionsApi::InteractionDtoChannel.build(data)
# => #<AddressChannelDetails:0x00007fdd4aab02a0>

DdxInteractionsApi::InteractionDtoChannel.build(data_that_doesnt_match)
# => nil
```

#### Parameters

| Name | Type | Description |
| ---- | ---- | ----------- |
| **data** | **Mixed** | data to be matched against the list of oneOf items |

#### Return type

- `AddressChannelDetails`
- `DynamicChannelDetails`
- `nil` (if no type matches)

