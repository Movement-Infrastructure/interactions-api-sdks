# Documentation for Interactions API

<a name="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://api.movementinfrastructure.org*

| Class | Method | HTTP request | Description |
|------------ | ------------- | ------------- | -------------|
| *AuthenticationDetailsApi* | [**vversionAuthMeGet**](Apis/AuthenticationDetailsApi.md#vversionauthmeget) | **GET** /v{version}/auth/me | Get authentication context |
| *InteractionsApi* | [**vversionInteractionsExchangeStatusGet**](Apis/InteractionsApi.md#vversioninteractionsexchangestatusget) | **GET** /v{version}/interactions/exchange-status | Get Exchange pipeline statuses by correlation or interaction ID |
*InteractionsApi* | [**vversionInteractionsExchangeStatusRangeGet**](Apis/InteractionsApi.md#vversioninteractionsexchangestatusrangeget) | **GET** /v{version}/interactions/exchange-status/range | Get Exchange pipeline statuses by date range |
*InteractionsApi* | [**vversionInteractionsInteractionIdTransactionsGet**](Apis/InteractionsApi.md#vversioninteractionsinteractionidtransactionsget) | **GET** /v{version}/interactions/{interactionId}/transactions | Get external API transactions by interactionId |
*InteractionsApi* | [**vversionInteractionsPost**](Apis/InteractionsApi.md#vversioninteractionspost) | **POST** /v{version}/interactions | Post interactions data |
*InteractionsApi* | [**vversionInteractionsTransactionsGet**](Apis/InteractionsApi.md#vversioninteractionstransactionsget) | **GET** /v{version}/interactions/transactions | Get external API transaction logs by date range |


<a name="documentation-for-models"></a>
## Documentation for Models

 - [AcceptedInteractionDto](./Models/AcceptedInteractionDto.md)
 - [AcceptedInteractionsDto](./Models/AcceptedInteractionsDto.md)
 - [ActivistCode](./Models/ActivistCode.md)
 - [ActivistCodeOutcomeDetails](./Models/ActivistCodeOutcomeDetails.md)
 - [Address](./Models/Address.md)
 - [AddressChannelDetails](./Models/AddressChannelDetails.md)
 - [CanvasserDetails](./Models/CanvasserDetails.md)
 - [CommitteeDetails](./Models/CommitteeDetails.md)
 - [CommunicationConsent](./Models/CommunicationConsent.md)
 - [CommunicationConsentOutcomeDetails](./Models/CommunicationConsentOutcomeDetails.md)
 - [CommunicationConsentStatus](./Models/CommunicationConsentStatus.md)
 - [ContactInfo](./Models/ContactInfo.md)
 - [ContactMethod](./Models/ContactMethod.md)
 - [DynamicChannelDetails](./Models/DynamicChannelDetails.md)
 - [DynamicOutcomeDetails](./Models/DynamicOutcomeDetails.md)
 - [EventDetails](./Models/EventDetails.md)
 - [EventRole](./Models/EventRole.md)
 - [EventSignup](./Models/EventSignup.md)
 - [EventSignupOutcomeDetails](./Models/EventSignupOutcomeDetails.md)
 - [EventSignupStatus](./Models/EventSignupStatus.md)
 - [EventSignupStatusValue](./Models/EventSignupStatusValue.md)
 - [ExchangeInteractionStatus](./Models/ExchangeInteractionStatus.md)
 - [ExchangeInteractionStatusDto](./Models/ExchangeInteractionStatusDto.md)
 - [ExchangeInteractionStatusDtoCursorPaginatedResponseDto](./Models/ExchangeInteractionStatusDtoCursorPaginatedResponseDto.md)
 - [ExternalApiKeyStatus](./Models/ExternalApiKeyStatus.md)
 - [ExternalApiKeyType](./Models/ExternalApiKeyType.md)
 - [ExternalTransactionStatus](./Models/ExternalTransactionStatus.md)
 - [InitiativeDto](./Models/InitiativeDto.md)
 - [InteractionDto](./Models/InteractionDto.md)
 - [InteractionDto_channel](./Models/InteractionDto_channel.md)
 - [InteractionDto_outcomesDetailed_inner](./Models/InteractionDto_outcomesDetailed_inner.md)
 - [InteractionErrorDto](./Models/InteractionErrorDto.md)
 - [InteractionVanFieldsDto](./Models/InteractionVanFieldsDto.md)
 - [InteractionsBatchResultDto](./Models/InteractionsBatchResultDto.md)
 - [InteractionsDto](./Models/InteractionsDto.md)
 - [InteractionsExternalApiTransactionDto](./Models/InteractionsExternalApiTransactionDto.md)
 - [InteractionsExternalApiTransactionDtoGetResponseDto](./Models/InteractionsExternalApiTransactionDtoGetResponseDto.md)
 - [InteractionsExternalApiTransactionLogDto](./Models/InteractionsExternalApiTransactionLogDto.md)
 - [MercuryDestinationVanApiKeyDto](./Models/MercuryDestinationVanApiKeyDto.md)
 - [MinervaMetadataDto](./Models/MinervaMetadataDto.md)
 - [Outcome](./Models/Outcome.md)
 - [OutcomeDetailOperation](./Models/OutcomeDetailOperation.md)
 - [PersonIdentifier](./Models/PersonIdentifier.md)
 - [ProblemDetails](./Models/ProblemDetails.md)
 - [RejectedInteractionDto](./Models/RejectedInteractionDto.md)
 - [RejectedInteractionsDto](./Models/RejectedInteractionsDto.md)
 - [SimpleDestinationDto](./Models/SimpleDestinationDto.md)
 - [SimpleMovementAppDto](./Models/SimpleMovementAppDto.md)
 - [SimpleWorkspaceDto](./Models/SimpleWorkspaceDto.md)
 - [SurveyResponse](./Models/SurveyResponse.md)
 - [SurveyResponseOutcomeDetails](./Models/SurveyResponseOutcomeDetails.md)
 - [VanApiKeyDto](./Models/VanApiKeyDto.md)
 - [VanDatabaseMode](./Models/VanDatabaseMode.md)
 - [WhoAmIApiKeyDto](./Models/WhoAmIApiKeyDto.md)
 - [WorkspaceTypeDto](./Models/WorkspaceTypeDto.md)


<a name="documentation-for-authorization"></a>
## Documentation for Authorization

<a name="Basic"></a>
### Basic

- **Type**: HTTP basic authentication

