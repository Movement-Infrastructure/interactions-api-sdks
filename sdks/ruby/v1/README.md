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
*DdxInteractionsApi::AuthenticationDetailsApi* | [**vversion_auth_me_get**](docs/AuthenticationDetailsApi.md#vversion_auth_me_get) | **GET** /v{version}/auth/me | Get authentication context
*DdxInteractionsApi::InteractionsApi* | [**vversion_interactions_exchange_status_get**](docs/InteractionsApi.md#vversion_interactions_exchange_status_get) | **GET** /v{version}/interactions/exchange-status | Get Exchange pipeline statuses by correlation or interaction ID
*DdxInteractionsApi::InteractionsApi* | [**vversion_interactions_exchange_status_range_get**](docs/InteractionsApi.md#vversion_interactions_exchange_status_range_get) | **GET** /v{version}/interactions/exchange-status/range | Get Exchange pipeline statuses by date range
*DdxInteractionsApi::InteractionsApi* | [**vversion_interactions_interaction_id_transactions_get**](docs/InteractionsApi.md#vversion_interactions_interaction_id_transactions_get) | **GET** /v{version}/interactions/{interactionId}/transactions | Get external API transactions by interactionId
*DdxInteractionsApi::InteractionsApi* | [**vversion_interactions_post**](docs/InteractionsApi.md#vversion_interactions_post) | **POST** /v{version}/interactions | Post interactions data
*DdxInteractionsApi::InteractionsApi* | [**vversion_interactions_transactions_get**](docs/InteractionsApi.md#vversion_interactions_transactions_get) | **GET** /v{version}/interactions/transactions | Get external API transaction logs by date range


## Documentation for Models

 - [DdxInteractionsApi::AcceptedInteractionDto](docs/AcceptedInteractionDto.md)
 - [DdxInteractionsApi::AcceptedInteractionsDto](docs/AcceptedInteractionsDto.md)
 - [DdxInteractionsApi::ActivistCode](docs/ActivistCode.md)
 - [DdxInteractionsApi::ActivistCodeOutcomeDetails](docs/ActivistCodeOutcomeDetails.md)
 - [DdxInteractionsApi::Address](docs/Address.md)
 - [DdxInteractionsApi::AddressChannelDetails](docs/AddressChannelDetails.md)
 - [DdxInteractionsApi::CanvasserDetails](docs/CanvasserDetails.md)
 - [DdxInteractionsApi::CommitteeDetails](docs/CommitteeDetails.md)
 - [DdxInteractionsApi::CommunicationConsent](docs/CommunicationConsent.md)
 - [DdxInteractionsApi::CommunicationConsentOutcomeDetails](docs/CommunicationConsentOutcomeDetails.md)
 - [DdxInteractionsApi::CommunicationConsentStatus](docs/CommunicationConsentStatus.md)
 - [DdxInteractionsApi::ContactInfo](docs/ContactInfo.md)
 - [DdxInteractionsApi::ContactMethod](docs/ContactMethod.md)
 - [DdxInteractionsApi::DynamicChannelDetails](docs/DynamicChannelDetails.md)
 - [DdxInteractionsApi::DynamicOutcomeDetails](docs/DynamicOutcomeDetails.md)
 - [DdxInteractionsApi::EventDetails](docs/EventDetails.md)
 - [DdxInteractionsApi::EventRole](docs/EventRole.md)
 - [DdxInteractionsApi::EventSignup](docs/EventSignup.md)
 - [DdxInteractionsApi::EventSignupOutcomeDetails](docs/EventSignupOutcomeDetails.md)
 - [DdxInteractionsApi::EventSignupStatus](docs/EventSignupStatus.md)
 - [DdxInteractionsApi::EventSignupStatusValue](docs/EventSignupStatusValue.md)
 - [DdxInteractionsApi::ExchangeInteractionStatus](docs/ExchangeInteractionStatus.md)
 - [DdxInteractionsApi::ExchangeInteractionStatusDto](docs/ExchangeInteractionStatusDto.md)
 - [DdxInteractionsApi::ExchangeInteractionStatusDtoCursorPaginatedResponseDto](docs/ExchangeInteractionStatusDtoCursorPaginatedResponseDto.md)
 - [DdxInteractionsApi::ExternalApiKeyStatus](docs/ExternalApiKeyStatus.md)
 - [DdxInteractionsApi::ExternalApiKeyType](docs/ExternalApiKeyType.md)
 - [DdxInteractionsApi::ExternalTransactionStatus](docs/ExternalTransactionStatus.md)
 - [DdxInteractionsApi::InitiativeDto](docs/InitiativeDto.md)
 - [DdxInteractionsApi::InteractionDto](docs/InteractionDto.md)
 - [DdxInteractionsApi::InteractionDtoChannel](docs/InteractionDtoChannel.md)
 - [DdxInteractionsApi::InteractionDtoOutcomesDetailedInner](docs/InteractionDtoOutcomesDetailedInner.md)
 - [DdxInteractionsApi::InteractionErrorDto](docs/InteractionErrorDto.md)
 - [DdxInteractionsApi::InteractionVanFieldsDto](docs/InteractionVanFieldsDto.md)
 - [DdxInteractionsApi::InteractionsBatchResultDto](docs/InteractionsBatchResultDto.md)
 - [DdxInteractionsApi::InteractionsDto](docs/InteractionsDto.md)
 - [DdxInteractionsApi::InteractionsExternalApiTransactionDto](docs/InteractionsExternalApiTransactionDto.md)
 - [DdxInteractionsApi::InteractionsExternalApiTransactionDtoGetResponseDto](docs/InteractionsExternalApiTransactionDtoGetResponseDto.md)
 - [DdxInteractionsApi::InteractionsExternalApiTransactionLogDto](docs/InteractionsExternalApiTransactionLogDto.md)
 - [DdxInteractionsApi::MercuryDestinationVanApiKeyDto](docs/MercuryDestinationVanApiKeyDto.md)
 - [DdxInteractionsApi::MinervaMetadataDto](docs/MinervaMetadataDto.md)
 - [DdxInteractionsApi::Outcome](docs/Outcome.md)
 - [DdxInteractionsApi::OutcomeDetailOperation](docs/OutcomeDetailOperation.md)
 - [DdxInteractionsApi::PersonIdentifier](docs/PersonIdentifier.md)
 - [DdxInteractionsApi::RejectedInteractionDto](docs/RejectedInteractionDto.md)
 - [DdxInteractionsApi::RejectedInteractionsDto](docs/RejectedInteractionsDto.md)
 - [DdxInteractionsApi::SimpleDestinationDto](docs/SimpleDestinationDto.md)
 - [DdxInteractionsApi::SimpleMovementAppDto](docs/SimpleMovementAppDto.md)
 - [DdxInteractionsApi::SimpleWorkspaceDto](docs/SimpleWorkspaceDto.md)
 - [DdxInteractionsApi::SurveyResponse](docs/SurveyResponse.md)
 - [DdxInteractionsApi::SurveyResponseOutcomeDetails](docs/SurveyResponseOutcomeDetails.md)
 - [DdxInteractionsApi::VanApiKeyDto](docs/VanApiKeyDto.md)
 - [DdxInteractionsApi::VanDatabaseMode](docs/VanDatabaseMode.md)
 - [DdxInteractionsApi::WhoAmIApiKeyDto](docs/WhoAmIApiKeyDto.md)
 - [DdxInteractionsApi::WorkspaceTypeDto](docs/WorkspaceTypeDto.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### Basic

- **Type**: HTTP basic authentication

