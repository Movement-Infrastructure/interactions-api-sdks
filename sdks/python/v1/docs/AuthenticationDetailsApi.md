# mi_interactions_api.AuthenticationDetailsApi

All URIs are relative to *https://api.movementinfrastructure.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vversion_auth_me_get**](AuthenticationDetailsApi.md#vversion_auth_me_get) | **GET** /v{version}/auth/me | Get authentication context


# **vversion_auth_me_get**
> WhoAmIApiKeyDto vversion_auth_me_get(version)

Get authentication context

Returns details about the authenticated API key including vendor, organization, committee, and state information.

### Example

* Basic Authentication (Basic):

```python
import mi_interactions_api
from mi_interactions_api.models.who_am_i_api_key_dto import WhoAmIApiKeyDto
from mi_interactions_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.movementinfrastructure.org
# See configuration.py for a list of all supported configuration parameters.
configuration = mi_interactions_api.Configuration(
    host = "https://api.movementinfrastructure.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = mi_interactions_api.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with mi_interactions_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mi_interactions_api.AuthenticationDetailsApi(api_client)
    version = '1' # str |  (default to '1')

    try:
        # Get authentication context
        api_response = api_instance.vversion_auth_me_get(version)
        print("The response of AuthenticationDetailsApi->vversion_auth_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationDetailsApi->vversion_auth_me_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;1&#39;]

### Return type

[**WhoAmIApiKeyDto**](WhoAmIApiKeyDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved API key information |  -  |
**401** | Unauthorized - invalid or missing API key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

