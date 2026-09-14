# Ddx.InteractionsApi
Interactions API documentation

C# client for the DDx Interactions API, generated from its OpenAPI
specification.

- API version: v1
- Package version: 0.1.0
- Generator version: 7.10.0

For more information, please visit [https://demexchange.com/](https://demexchange.com/).

## Requirements

net8.0

## Installation

```shell
dotnet add package Ddx.InteractionsApi
```

Then import the namespaces:

```csharp
using Ddx.InteractionsApi.Api;
using Ddx.InteractionsApi.Client;
using Ddx.InteractionsApi.Model;
```

## Reporting issues

This package is generated; edits to it are overwritten on the next spec sync.
Report problems against the API specification rather than the generated code.

## Getting Started

```csharp
using System;
using Ddx.InteractionsApi.Api;
using Ddx.InteractionsApi.Client;

// HTTP basic auth, API key in the password field, empty username.
// Configuration.BasePath already defaults to the production API.
var config = new Configuration
{
    Username = "",
    Password = Environment.GetEnvironmentVariable("DDX_API_KEY"),
};

var api = new AuthenticationDetailsApi(config);

try
{
    var me = api.VversionAuthMeGet("1");
    Console.WriteLine(me.ToJson());
}
catch (ApiException e)
{
    // The exception message is only the status line; ErrorContent says why.
    Console.Error.WriteLine($"Interactions API returned {e.ErrorCode}: {e.ErrorContent}");
}
```

<a id="documentation-for-api-endpoints"></a>
## Documentation for API Endpoints

All URIs are relative to *https://api.movementinfrastructure.org*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationDetailsApi* | [**VversionAuthMeGet**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/AuthenticationDetailsApi.md#vversionauthmeget) | **GET** /v{version}/auth/me | Get authentication context
*InteractionsApi* | [**VversionInteractionsExchangeStatusGet**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InteractionsApi.md#vversioninteractionsexchangestatusget) | **GET** /v{version}/interactions/exchange-status | Get Exchange pipeline statuses by correlation or interaction ID
*InteractionsApi* | [**VversionInteractionsExchangeStatusRangeGet**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InteractionsApi.md#vversioninteractionsexchangestatusrangeget) | **GET** /v{version}/interactions/exchange-status/range | Get Exchange pipeline statuses by date range
*InteractionsApi* | [**VversionInteractionsInteractionIdTransactionsGet**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InteractionsApi.md#vversioninteractionsinteractionidtransactionsget) | **GET** /v{version}/interactions/{interactionId}/transactions | Get external API transactions by interactionId
*InteractionsApi* | [**VversionInteractionsPost**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InteractionsApi.md#vversioninteractionspost) | **POST** /v{version}/interactions | Post interactions data
*InteractionsApi* | [**VversionInteractionsTransactionsGet**](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InteractionsApi.md#vversioninteractionstransactionsget) | **GET** /v{version}/interactions/transactions | Get external API transaction logs by date range


<a id="documentation-for-models"></a>
## Documentation for Models

 - [Model.AcceptedInteractionDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/AcceptedInteractionDto.md)
 - [Model.AcceptedInteractionsDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/AcceptedInteractionsDto.md)
 - [Model.ActivistCode](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/ActivistCode.md)
 - [Model.ActivistCodeOutcomeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/ActivistCodeOutcomeDetails.md)
 - [Model.Address](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/Address.md)
 - [Model.AddressChannelDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/AddressChannelDetails.md)
 - [Model.CanvasserDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/CanvasserDetails.md)
 - [Model.CommitteeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/CommitteeDetails.md)
 - [Model.CommunicationConsent](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/CommunicationConsent.md)
 - [Model.CommunicationConsentOutcomeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/CommunicationConsentOutcomeDetails.md)
 - [Model.CommunicationConsentStatus](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/CommunicationConsentStatus.md)
 - [Model.ContactInfo](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/ContactInfo.md)
 - [Model.ContactMethod](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/ContactMethod.md)
 - [Model.DynamicChannelDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/DynamicChannelDetails.md)
 - [Model.DynamicOutcomeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/DynamicOutcomeDetails.md)
 - [Model.EventDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/EventDetails.md)
 - [Model.EventRole](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/EventRole.md)
 - [Model.EventSignup](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/EventSignup.md)
 - [Model.EventSignupOutcomeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/EventSignupOutcomeDetails.md)
 - [Model.EventSignupStatus](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/EventSignupStatus.md)
 - [Model.EventSignupStatusValue](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/EventSignupStatusValue.md)
 - [Model.ExchangeInteractionStatus](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/ExchangeInteractionStatus.md)
 - [Model.ExchangeInteractionStatusDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/ExchangeInteractionStatusDto.md)
 - [Model.ExchangeInteractionStatusDtoCursorPaginatedResponseDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/ExchangeInteractionStatusDtoCursorPaginatedResponseDto.md)
 - [Model.ExternalApiKeyStatus](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/ExternalApiKeyStatus.md)
 - [Model.ExternalApiKeyType](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/ExternalApiKeyType.md)
 - [Model.ExternalTransactionStatus](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/ExternalTransactionStatus.md)
 - [Model.InitiativeDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InitiativeDto.md)
 - [Model.InteractionDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InteractionDto.md)
 - [Model.InteractionDtoChannel](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InteractionDtoChannel.md)
 - [Model.InteractionDtoOutcomesDetailedInner](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InteractionDtoOutcomesDetailedInner.md)
 - [Model.InteractionErrorDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InteractionErrorDto.md)
 - [Model.InteractionVanFieldsDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InteractionVanFieldsDto.md)
 - [Model.InteractionsBatchResultDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InteractionsBatchResultDto.md)
 - [Model.InteractionsDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InteractionsDto.md)
 - [Model.InteractionsExternalApiTransactionDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InteractionsExternalApiTransactionDto.md)
 - [Model.InteractionsExternalApiTransactionDtoGetResponseDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InteractionsExternalApiTransactionDtoGetResponseDto.md)
 - [Model.InteractionsExternalApiTransactionLogDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/InteractionsExternalApiTransactionLogDto.md)
 - [Model.MercuryDestinationVanApiKeyDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/MercuryDestinationVanApiKeyDto.md)
 - [Model.MinervaMetadataDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/MinervaMetadataDto.md)
 - [Model.Outcome](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/Outcome.md)
 - [Model.OutcomeDetailOperation](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/OutcomeDetailOperation.md)
 - [Model.PersonIdentifier](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/PersonIdentifier.md)
 - [Model.RejectedInteractionDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/RejectedInteractionDto.md)
 - [Model.RejectedInteractionsDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/RejectedInteractionsDto.md)
 - [Model.SimpleDestinationDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/SimpleDestinationDto.md)
 - [Model.SimpleMovementAppDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/SimpleMovementAppDto.md)
 - [Model.SimpleWorkspaceDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/SimpleWorkspaceDto.md)
 - [Model.SurveyResponse](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/SurveyResponse.md)
 - [Model.SurveyResponseOutcomeDetails](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/SurveyResponseOutcomeDetails.md)
 - [Model.VanApiKeyDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/VanApiKeyDto.md)
 - [Model.VanDatabaseMode](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/VanDatabaseMode.md)
 - [Model.WhoAmIApiKeyDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/WhoAmIApiKeyDto.md)
 - [Model.WorkspaceTypeDto](https://github.com/Movement-Infrastructure/interactions-api-sdks/blob/main/sdks/csharp/v1/docs/WorkspaceTypeDto.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="Basic"></a>
### Basic

- **Type**: HTTP basic authentication
