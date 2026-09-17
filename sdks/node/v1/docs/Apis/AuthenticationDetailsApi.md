# AuthenticationDetailsApi

All URIs are relative to *https://api.movementinfrastructure.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vversionAuthMeGet**](AuthenticationDetailsApi.md#vversionAuthMeGet) | **GET** /v{version}/auth/me | Get authentication context |


<a name="vversionAuthMeGet"></a>
# **vversionAuthMeGet**
> WhoAmIApiKeyDto vversionAuthMeGet(version)

Get authentication context

    Returns details about the authenticated API key including vendor, organization, committee, and state information.

### Parameters

|Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **version** | **String**|  | [default to 1] |

### Return type

[**WhoAmIApiKeyDto**](../Models/WhoAmIApiKeyDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

