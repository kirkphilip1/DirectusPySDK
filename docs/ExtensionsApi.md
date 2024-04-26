# swagger_client.ExtensionsApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_extensions**](ExtensionsApi.md#list_extensions) | **GET** /extensions | List Extensions
[**update_extensions**](ExtensionsApi.md#update_extensions) | **PATCH** /extensions/{name} | Update an Extension
[**update_extensions_0**](ExtensionsApi.md#update_extensions_0) | **PATCH** /extensions/{bundle}/{name} | Update an Extension

# **list_extensions**
> InlineResponse20017 list_extensions()

List Extensions

List the installed extensions and their configuration in the project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtensionsApi()

try:
    # List Extensions
    api_response = api_instance.list_extensions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsApi->list_extensions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_extensions**
> InlineResponse20018 update_extensions(name, body=body)

Update an Extension

Update an existing extension.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtensionsApi()
name = 'name_example' # str | 
body = swagger_client.ExtensionsNameBody() # ExtensionsNameBody |  (optional)

try:
    # Update an Extension
    api_response = api_instance.update_extensions(name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsApi->update_extensions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | [**ExtensionsNameBody**](ExtensionsNameBody.md)|  | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_extensions_0**
> InlineResponse20018 update_extensions_0(bundle, name, body=body)

Update an Extension

Update an existing extension.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtensionsApi()
bundle = 'bundle_example' # str | 
name = 'name_example' # str | 
body = swagger_client.BundleNameBody() # BundleNameBody |  (optional)

try:
    # Update an Extension
    api_response = api_instance.update_extensions_0(bundle, name, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsApi->update_extensions_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bundle** | **str**|  | 
 **name** | **str**|  | 
 **body** | [**BundleNameBody**](BundleNameBody.md)|  | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

