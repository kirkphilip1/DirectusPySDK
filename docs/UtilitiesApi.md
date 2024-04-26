# swagger_client.UtilitiesApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_import**](UtilitiesApi.md#call_import) | **POST** /utils/import/{collection} | Import Items
[**clear_cache**](UtilitiesApi.md#clear_cache) | **POST** /utils/cache/clear | Clear Cache
[**export**](UtilitiesApi.md#export) | **POST** /utils/export/{collection} | Export Items
[**hash_generate**](UtilitiesApi.md#hash_generate) | **POST** /utils/hash/generate | Hash a string
[**hash_verify**](UtilitiesApi.md#hash_verify) | **POST** /utils/hash/verify | Hash a string
[**random**](UtilitiesApi.md#random) | **GET** /utils/random/string | Get a Random String
[**sort**](UtilitiesApi.md#sort) | **POST** /utils/sort/{collection} | Sort Items

# **call_import**
> call_import(collection, file=file)

Import Items

Import multiple records from a JSON or CSV file into a collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilitiesApi()
collection = 'collection_example' # str | Collection identifier
file = 'file_example' # str |  (optional)

try:
    # Import Items
    api_instance.call_import(collection, file=file)
except ApiException as e:
    print("Exception when calling UtilitiesApi->call_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Collection identifier | 
 **file** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_cache**
> clear_cache()

Clear Cache

Resets both the data and schema cache of Directus.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilitiesApi()

try:
    # Clear Cache
    api_instance.clear_cache()
except ApiException as e:
    print("Exception when calling UtilitiesApi->clear_cache: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export**
> export(collection, body=body)

Export Items

Export a larger data set to a file in the File Library

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilitiesApi()
collection = 'collection_example' # str | Collection identifier
body = swagger_client.ExportCollectionBody() # ExportCollectionBody |  (optional)

try:
    # Export Items
    api_instance.export(collection, body=body)
except ApiException as e:
    print("Exception when calling UtilitiesApi->export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Collection identifier | 
 **body** | [**ExportCollectionBody**](ExportCollectionBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hash_generate**
> InlineResponse2006 hash_generate(body=body)

Hash a string

Generate a hash for a given string.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilitiesApi()
body = swagger_client.HashGenerateBody() # HashGenerateBody |  (optional)

try:
    # Hash a string
    api_response = api_instance.hash_generate(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->hash_generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HashGenerateBody**](HashGenerateBody.md)|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hash_verify**
> InlineResponse2007 hash_verify(body=body)

Hash a string

Generate a hash for a given string.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilitiesApi()
body = swagger_client.HashVerifyBody() # HashVerifyBody |  (optional)

try:
    # Hash a string
    api_response = api_instance.hash_verify(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->hash_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HashVerifyBody**](HashVerifyBody.md)|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **random**
> InlineResponse2008 random(length=length)

Get a Random String

Returns a random string of given length.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilitiesApi()
length = 56 # int | Length of the random string. (optional)

try:
    # Get a Random String
    api_response = api_instance.random(length=length)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->random: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **length** | **int**| Length of the random string. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sort**
> sort(collection, body=body)

Sort Items

Re-sort items in collection based on start and to value of item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UtilitiesApi()
collection = 'collection_example' # str | Collection identifier
body = swagger_client.SortCollectionBody() # SortCollectionBody |  (optional)

try:
    # Sort Items
    api_instance.sort(collection, body=body)
except ApiException as e:
    print("Exception when calling UtilitiesApi->sort: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Collection identifier | 
 **body** | [**SortCollectionBody**](SortCollectionBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

