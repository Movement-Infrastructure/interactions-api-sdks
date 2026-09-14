# ddx-interactions-api
Interactions API documentation

Python client for the DDx Interactions API, generated from its OpenAPI
specification.

- API version: v1
- Package version: 0.3.0
- Generator version: 7.10.0

For more information, please visit [https://demexchange.com/](https://demexchange.com/).

For support for this package or the DDx Interactions API please contact us
at <api@demexchange.com>

## Requirements

Python 3.8+

## Installation

```sh
pip install ddx-interactions-api
```

Then import the package:

```python
import ddx_interactions_api
```

## Changelog

API changes are recorded in the
[changelog](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/CHANGELOG.md),
regenerated from a diff of the OpenAPI specification on each sync. Entries
marked **breaking** require a change on the consumer side.

## Reporting issues

This package is generated; edits to it are overwritten on the next spec sync.
Report problems against the API specification rather than the generated code.

## Getting Started

Validating an integration end to end? The [UAT guide](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/docs/PythonUat.md)
walks through install, authentication, submitting an interaction, and confirming
it reached the Exchange.

```python

import ddx_interactions_api
from ddx_interactions_api.rest import ApiException
from pprint import pprint

# Authentication is HTTP basic, with your API key in the password field and an
# empty username. The key has the form "<keyId>.<secret>".
#
# The host defaults to https://api.movementinfrastructure.org. Pass host= to target another server.
# See configuration.py for all supported parameters.
import os

configuration = ddx_interactions_api.Configuration(
    username = "",
    password = os.environ["DDX_API_KEY"],
)


# Enter a context with an instance of the API client
with ddx_interactions_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ddx_interactions_api.AuthenticationDetailsApi(api_client)
    version = '1' # str |  (default to '1')

    try:
        # Get authentication context
        api_response = api_instance.vversion_auth_me_get(version)
        print("The response of AuthenticationDetailsApi->vversion_auth_me_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationDetailsApi->vversion_auth_me_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.movementinfrastructure.org*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationDetailsApi* | [**vversion_auth_me_get**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/AuthenticationDetailsApi.md#vversion_auth_me_get) | **GET** /v{version}/auth/me | Get authentication context
*InteractionsApi* | [**vversion_interactions_exchange_status_get**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InteractionsApi.md#vversion_interactions_exchange_status_get) | **GET** /v{version}/interactions/exchange-status | Get Exchange pipeline statuses by correlation or interaction ID
*InteractionsApi* | [**vversion_interactions_exchange_status_range_get**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InteractionsApi.md#vversion_interactions_exchange_status_range_get) | **GET** /v{version}/interactions/exchange-status/range | Get Exchange pipeline statuses by date range
*InteractionsApi* | [**vversion_interactions_interaction_id_transactions_get**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InteractionsApi.md#vversion_interactions_interaction_id_transactions_get) | **GET** /v{version}/interactions/{interactionId}/transactions | Get external API transactions by interactionId
*InteractionsApi* | [**vversion_interactions_post**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InteractionsApi.md#vversion_interactions_post) | **POST** /v{version}/interactions | Post interactions data
*InteractionsApi* | [**vversion_interactions_transactions_get**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InteractionsApi.md#vversion_interactions_transactions_get) | **GET** /v{version}/interactions/transactions | Get external API transaction logs by date range


## Documentation For Models

 - [AcceptedInteractionDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/AcceptedInteractionDto.md)
 - [AcceptedInteractionsDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/AcceptedInteractionsDto.md)
 - [ActivistCode](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/ActivistCode.md)
 - [ActivistCodeOutcomeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/ActivistCodeOutcomeDetails.md)
 - [Address](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/Address.md)
 - [AddressChannelDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/AddressChannelDetails.md)
 - [CanvasserDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/CanvasserDetails.md)
 - [CommitteeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/CommitteeDetails.md)
 - [CommunicationConsent](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/CommunicationConsent.md)
 - [CommunicationConsentOutcomeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/CommunicationConsentOutcomeDetails.md)
 - [CommunicationConsentStatus](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/CommunicationConsentStatus.md)
 - [ContactInfo](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/ContactInfo.md)
 - [ContactMethod](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/ContactMethod.md)
 - [DynamicChannelDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/DynamicChannelDetails.md)
 - [DynamicOutcomeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/DynamicOutcomeDetails.md)
 - [EventDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/EventDetails.md)
 - [EventRole](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/EventRole.md)
 - [EventSignup](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/EventSignup.md)
 - [EventSignupOutcomeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/EventSignupOutcomeDetails.md)
 - [EventSignupStatus](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/EventSignupStatus.md)
 - [EventSignupStatusValue](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/EventSignupStatusValue.md)
 - [ExchangeInteractionStatus](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/ExchangeInteractionStatus.md)
 - [ExchangeInteractionStatusDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/ExchangeInteractionStatusDto.md)
 - [ExchangeInteractionStatusDtoCursorPaginatedResponseDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/ExchangeInteractionStatusDtoCursorPaginatedResponseDto.md)
 - [ExternalApiKeyStatus](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/ExternalApiKeyStatus.md)
 - [ExternalApiKeyType](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/ExternalApiKeyType.md)
 - [ExternalTransactionStatus](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/ExternalTransactionStatus.md)
 - [InitiativeDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InitiativeDto.md)
 - [InteractionDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InteractionDto.md)
 - [InteractionDtoChannel](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InteractionDtoChannel.md)
 - [InteractionDtoOutcomesDetailedInner](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InteractionDtoOutcomesDetailedInner.md)
 - [InteractionErrorDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InteractionErrorDto.md)
 - [InteractionVanFieldsDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InteractionVanFieldsDto.md)
 - [InteractionsBatchResultDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InteractionsBatchResultDto.md)
 - [InteractionsDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InteractionsDto.md)
 - [InteractionsExternalApiTransactionDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InteractionsExternalApiTransactionDto.md)
 - [InteractionsExternalApiTransactionDtoGetResponseDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InteractionsExternalApiTransactionDtoGetResponseDto.md)
 - [InteractionsExternalApiTransactionLogDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/InteractionsExternalApiTransactionLogDto.md)
 - [MercuryDestinationVanApiKeyDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/MercuryDestinationVanApiKeyDto.md)
 - [MinervaMetadataDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/MinervaMetadataDto.md)
 - [Outcome](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/Outcome.md)
 - [OutcomeDetailOperation](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/OutcomeDetailOperation.md)
 - [PersonIdentifier](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/PersonIdentifier.md)
 - [ProblemDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/ProblemDetails.md)
 - [RejectedInteractionDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/RejectedInteractionDto.md)
 - [RejectedInteractionsDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/RejectedInteractionsDto.md)
 - [SimpleDestinationDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/SimpleDestinationDto.md)
 - [SimpleMovementAppDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/SimpleMovementAppDto.md)
 - [SimpleWorkspaceDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/SimpleWorkspaceDto.md)
 - [SurveyResponse](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/SurveyResponse.md)
 - [SurveyResponseOutcomeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/SurveyResponseOutcomeDetails.md)
 - [VanApiKeyDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/VanApiKeyDto.md)
 - [VanDatabaseMode](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/VanDatabaseMode.md)
 - [WhoAmIApiKeyDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/WhoAmIApiKeyDto.md)
 - [WorkspaceTypeDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/python/v1/docs/WorkspaceTypeDto.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Basic"></a>
### Basic

- **Type**: HTTP basic authentication


## Author

api@demexchange.com


