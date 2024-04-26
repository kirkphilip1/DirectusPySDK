# swagger_client.ServerApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping**](ServerApi.md#ping) | **GET** /server/ping | Ping
[**server_info**](ServerApi.md#server_info) | **GET** /server/info | System Info

# **ping**
> str ping()

Ping

Ping, pong. Ping.. pong.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()

try:
    # Ping
    api_response = api_instance.ping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->ping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/text

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **server_info**
> InlineResponse2005 server_info(super_admin_token)

System Info

Perform a system status check and return the options.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServerApi()
super_admin_token = 56 # int | The first time you create a project, the provided token will be saved and required for subsequent project installs. It can also be found and configured in `/config/__api.json` on your server.

try:
    # System Info
    api_response = api_instance.server_info(super_admin_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServerApi->server_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **super_admin_token** | **int**| The first time you create a project, the provided token will be saved and required for subsequent project installs. It can also be found and configured in &#x60;/config/__api.json&#x60; on your server. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

