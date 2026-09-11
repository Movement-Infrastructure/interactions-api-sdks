# ddx_interactions_api
Interactions API documentation

Ruby client for the DDx Interactions API, generated from its OpenAPI
specification.

- API version: v1
- Gem version: 0.1.0
- Generator version: 7.10.0

For more information, please visit [https://demexchange.com/](https://demexchange.com/).

## Requirements

Ruby >= 3.0

## Installation

```shell
gem install ddx_interactions_api
```

Every published version is currently a prerelease (`X.Y.Z.pre.N`), and both
`gem install` and Bundler skip prereleases unless asked. Add `--pre` to take
the most recent one:

```shell
gem install ddx_interactions_api --pre
```

In a Gemfile, pin the exact version. A pessimistic constraint (`~>`) will not
select a prerelease:

    gem 'ddx_interactions_api', '0.1.0.pre.<build>'

[RubyGems](https://rubygems.org/gems/ddx_interactions_api/versions) lists what is
published.

## Changelog

API changes are recorded in the
[changelog](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/CHANGELOG.md),
regenerated from a diff of the OpenAPI specification on each sync. Entries
marked **breaking** require a change on the consumer side.

## Reporting issues

This gem is generated; edits to it are overwritten on the next spec sync.
Report problems against the API specification rather than the generated code.

## Getting Started

```ruby
require 'ddx_interactions_api'

config = DdxInteractionsApi::Configuration.new
# HTTP basic auth, with the API key in the password field and an empty
# username. `config.host` defaults to the production API.
config.username = ''
config.password = ENV.fetch('DDX_API_KEY')

client = DdxInteractionsApi::ApiClient.new(config)

begin
  me = DdxInteractionsApi::AuthenticationDetailsApi.new(client).vversion_auth_me_get('1')
  p me
rescue DdxInteractionsApi::ApiError => e
  # The exception message is only the status line; the body says why.
  warn "Interactions API returned #{e.code}: #{e.response_body}"
end
```

## Documentation for API Endpoints

All URIs are relative to *https://api.movementinfrastructure.org*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DdxInteractionsApi::AuthenticationDetailsApi* | [**vversion_auth_me_get**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/AuthenticationDetailsApi.md#vversion_auth_me_get) | **GET** /v{version}/auth/me | Get authentication context
*DdxInteractionsApi::InteractionsApi* | [**vversion_interactions_exchange_status_get**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InteractionsApi.md#vversion_interactions_exchange_status_get) | **GET** /v{version}/interactions/exchange-status | Get Exchange pipeline statuses by correlation or interaction ID
*DdxInteractionsApi::InteractionsApi* | [**vversion_interactions_exchange_status_range_get**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InteractionsApi.md#vversion_interactions_exchange_status_range_get) | **GET** /v{version}/interactions/exchange-status/range | Get Exchange pipeline statuses by date range
*DdxInteractionsApi::InteractionsApi* | [**vversion_interactions_interaction_id_transactions_get**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InteractionsApi.md#vversion_interactions_interaction_id_transactions_get) | **GET** /v{version}/interactions/{interactionId}/transactions | Get external API transactions by interactionId
*DdxInteractionsApi::InteractionsApi* | [**vversion_interactions_post**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InteractionsApi.md#vversion_interactions_post) | **POST** /v{version}/interactions | Post interactions data
*DdxInteractionsApi::InteractionsApi* | [**vversion_interactions_transactions_get**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InteractionsApi.md#vversion_interactions_transactions_get) | **GET** /v{version}/interactions/transactions | Get external API transaction logs by date range


## Documentation for Models

 - [DdxInteractionsApi::AcceptedInteractionDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/AcceptedInteractionDto.md)
 - [DdxInteractionsApi::AcceptedInteractionsDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/AcceptedInteractionsDto.md)
 - [DdxInteractionsApi::ActivistCode](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/ActivistCode.md)
 - [DdxInteractionsApi::ActivistCodeOutcomeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/ActivistCodeOutcomeDetails.md)
 - [DdxInteractionsApi::Address](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/Address.md)
 - [DdxInteractionsApi::AddressChannelDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/AddressChannelDetails.md)
 - [DdxInteractionsApi::CanvasserDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/CanvasserDetails.md)
 - [DdxInteractionsApi::CommitteeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/CommitteeDetails.md)
 - [DdxInteractionsApi::CommunicationConsent](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/CommunicationConsent.md)
 - [DdxInteractionsApi::CommunicationConsentOutcomeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/CommunicationConsentOutcomeDetails.md)
 - [DdxInteractionsApi::CommunicationConsentStatus](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/CommunicationConsentStatus.md)
 - [DdxInteractionsApi::ContactInfo](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/ContactInfo.md)
 - [DdxInteractionsApi::ContactMethod](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/ContactMethod.md)
 - [DdxInteractionsApi::DynamicChannelDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/DynamicChannelDetails.md)
 - [DdxInteractionsApi::DynamicOutcomeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/DynamicOutcomeDetails.md)
 - [DdxInteractionsApi::EventDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/EventDetails.md)
 - [DdxInteractionsApi::EventRole](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/EventRole.md)
 - [DdxInteractionsApi::EventSignup](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/EventSignup.md)
 - [DdxInteractionsApi::EventSignupOutcomeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/EventSignupOutcomeDetails.md)
 - [DdxInteractionsApi::EventSignupStatus](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/EventSignupStatus.md)
 - [DdxInteractionsApi::EventSignupStatusValue](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/EventSignupStatusValue.md)
 - [DdxInteractionsApi::ExchangeInteractionStatus](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/ExchangeInteractionStatus.md)
 - [DdxInteractionsApi::ExchangeInteractionStatusDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/ExchangeInteractionStatusDto.md)
 - [DdxInteractionsApi::ExchangeInteractionStatusDtoCursorPaginatedResponseDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/ExchangeInteractionStatusDtoCursorPaginatedResponseDto.md)
 - [DdxInteractionsApi::ExternalApiKeyStatus](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/ExternalApiKeyStatus.md)
 - [DdxInteractionsApi::ExternalApiKeyType](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/ExternalApiKeyType.md)
 - [DdxInteractionsApi::ExternalTransactionStatus](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/ExternalTransactionStatus.md)
 - [DdxInteractionsApi::InitiativeDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InitiativeDto.md)
 - [DdxInteractionsApi::InteractionDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InteractionDto.md)
 - [DdxInteractionsApi::InteractionDtoChannel](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InteractionDtoChannel.md)
 - [DdxInteractionsApi::InteractionDtoOutcomesDetailedInner](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InteractionDtoOutcomesDetailedInner.md)
 - [DdxInteractionsApi::InteractionErrorDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InteractionErrorDto.md)
 - [DdxInteractionsApi::InteractionVanFieldsDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InteractionVanFieldsDto.md)
 - [DdxInteractionsApi::InteractionsBatchResultDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InteractionsBatchResultDto.md)
 - [DdxInteractionsApi::InteractionsDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InteractionsDto.md)
 - [DdxInteractionsApi::InteractionsExternalApiTransactionDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InteractionsExternalApiTransactionDto.md)
 - [DdxInteractionsApi::InteractionsExternalApiTransactionDtoGetResponseDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InteractionsExternalApiTransactionDtoGetResponseDto.md)
 - [DdxInteractionsApi::InteractionsExternalApiTransactionLogDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/InteractionsExternalApiTransactionLogDto.md)
 - [DdxInteractionsApi::MercuryDestinationVanApiKeyDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/MercuryDestinationVanApiKeyDto.md)
 - [DdxInteractionsApi::MinervaMetadataDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/MinervaMetadataDto.md)
 - [DdxInteractionsApi::Outcome](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/Outcome.md)
 - [DdxInteractionsApi::OutcomeDetailOperation](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/OutcomeDetailOperation.md)
 - [DdxInteractionsApi::PersonIdentifier](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/PersonIdentifier.md)
 - [DdxInteractionsApi::RejectedInteractionDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/RejectedInteractionDto.md)
 - [DdxInteractionsApi::RejectedInteractionsDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/RejectedInteractionsDto.md)
 - [DdxInteractionsApi::SimpleDestinationDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/SimpleDestinationDto.md)
 - [DdxInteractionsApi::SimpleMovementAppDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/SimpleMovementAppDto.md)
 - [DdxInteractionsApi::SimpleWorkspaceDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/SimpleWorkspaceDto.md)
 - [DdxInteractionsApi::SurveyResponse](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/SurveyResponse.md)
 - [DdxInteractionsApi::SurveyResponseOutcomeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/SurveyResponseOutcomeDetails.md)
 - [DdxInteractionsApi::VanApiKeyDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/VanApiKeyDto.md)
 - [DdxInteractionsApi::VanDatabaseMode](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/VanDatabaseMode.md)
 - [DdxInteractionsApi::WhoAmIApiKeyDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/WhoAmIApiKeyDto.md)
 - [DdxInteractionsApi::WorkspaceTypeDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/ruby/v1/docs/WorkspaceTypeDto.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### Basic

- **Type**: HTTP basic authentication

