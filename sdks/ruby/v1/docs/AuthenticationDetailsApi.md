# DdxInteractionsApi::AuthenticationDetailsApi

All URIs are relative to *https://api.movementinfrastructure.org*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**vversion_auth_me_get**](AuthenticationDetailsApi.md#vversion_auth_me_get) | **GET** /v{version}/auth/me | Get authentication context |


## vversion_auth_me_get

> <WhoAmIApiKeyDto> vversion_auth_me_get(version)

Get authentication context

Returns details about the authenticated API key including vendor, organization, committee, and state information.

### Examples

```ruby
require 'time'
require 'ddx_interactions_api'
# setup authorization
DdxInteractionsApi.configure do |config|
  # Configure HTTP basic authorization: Basic
  config.username = 'YOUR USERNAME'
  config.password = 'YOUR PASSWORD'
end

api_instance = DdxInteractionsApi::AuthenticationDetailsApi.new
version = 'version_example' # String | 

begin
  # Get authentication context
  result = api_instance.vversion_auth_me_get(version)
  p result
rescue DdxInteractionsApi::ApiError => e
  puts "Error when calling AuthenticationDetailsApi->vversion_auth_me_get: #{e}"
end
```

#### Using the vversion_auth_me_get_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<WhoAmIApiKeyDto>, Integer, Hash)> vversion_auth_me_get_with_http_info(version)

```ruby
begin
  # Get authentication context
  data, status_code, headers = api_instance.vversion_auth_me_get_with_http_info(version)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <WhoAmIApiKeyDto>
rescue DdxInteractionsApi::ApiError => e
  puts "Error when calling AuthenticationDetailsApi->vversion_auth_me_get_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **version** | **String** |  | [default to &#39;1&#39;] |

### Return type

[**WhoAmIApiKeyDto**](WhoAmIApiKeyDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

