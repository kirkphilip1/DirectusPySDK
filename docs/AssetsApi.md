# swagger_client.AssetsApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset**](AssetsApi.md#get_asset) | **GET** /assets/{id} | Get an Asset

# **get_asset**
> str get_asset(id, key=key, transforms=transforms, download=download)

Get an Asset

Image typed files can be dynamically resized and transformed to fit any need.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
id = 'id_example' # str | The id of the file.
key = 'key_example' # str | The key of the asset size configured in settings. (optional)
transforms = 'transforms_example' # str | A JSON array of image transformations (optional)
download = true # bool | Download the asset to your computer (optional)

try:
    # Get an Asset
    api_response = api_instance.get_asset(id, key=key, transforms=transforms, download=download)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the file. | 
 **key** | **str**| The key of the asset size configured in settings. | [optional] 
 **transforms** | **str**| A JSON array of image transformations | [optional] 
 **download** | **bool**| Download the asset to your computer | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

