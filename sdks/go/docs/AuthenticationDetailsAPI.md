# \AuthenticationDetailsAPI

All URIs are relative to *https://api.movementinfrastructure.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**VversionAuthMeGet**](AuthenticationDetailsAPI.md#VversionAuthMeGet) | **Get** /v{version}/auth/me | Get authentication context



## VversionAuthMeGet

> WhoAmIApiKeyDto VversionAuthMeGet(ctx, version).Execute()

Get authentication context



### Example

```go
package main

import (
	"context"
	"fmt"
	"os"
	openapiclient "github.com/Movement-Infrastructure/interactions-api-sdks/sdks/go"
)

func main() {
	version := "version_example" // string |  (default to "1")

	configuration := openapiclient.NewConfiguration()
	apiClient := openapiclient.NewAPIClient(configuration)
	resp, r, err := apiClient.AuthenticationDetailsAPI.VversionAuthMeGet(context.Background(), version).Execute()
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error when calling `AuthenticationDetailsAPI.VversionAuthMeGet``: %v\n", err)
		fmt.Fprintf(os.Stderr, "Full HTTP response: %v\n", r)
	}
	// response from `VversionAuthMeGet`: WhoAmIApiKeyDto
	fmt.Fprintf(os.Stdout, "Response from `AuthenticationDetailsAPI.VversionAuthMeGet`: %v\n", resp)
}
```

### Path Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**ctx** | **context.Context** | context for authentication, logging, cancellation, deadlines, tracing, etc.
**version** | **string** |  | [default to &quot;1&quot;]

### Other Parameters

Other parameters are passed through a pointer to a apiVversionAuthMeGetRequest struct via the builder pattern


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------


### Return type

[**WhoAmIApiKeyDto**](WhoAmIApiKeyDto.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../README.md#documentation-for-models)
[[Back to README]](../README.md)

