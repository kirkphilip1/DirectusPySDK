# swagger_client.SettingsApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_settings**](SettingsApi.md#get_settings) | **GET** /settings | Retrieve Settings
[**update_setting**](SettingsApi.md#update_setting) | **PATCH** /settings | Update Settings

# **get_settings**
> InlineResponse20040 get_settings(limit=limit, offset=offset, meta=meta, page=page)

Retrieve Settings

List the settings.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SettingsApi()
limit = 56 # int | A limit on the number of objects that are returned. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
page = 56 # int | Cursor for use in pagination. Often used in combination with limit. (optional)

try:
    # Retrieve Settings
    api_response = api_instance.get_settings(limit=limit, offset=offset, meta=meta, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->get_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| A limit on the number of objects that are returned. | [optional] 
 **offset** | **int**| How many items to skip when fetching data. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 
 **page** | **int**| Cursor for use in pagination. Often used in combination with limit. | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_setting**
> InlineResponse20040 update_setting(body=body)

Update Settings

Update the settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SettingsApi()
body = NULL # object |  (optional)

try:
    # Update Settings
    api_response = api_instance.update_setting(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->update_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

