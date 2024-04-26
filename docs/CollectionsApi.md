# swagger_client.CollectionsApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_collection**](CollectionsApi.md#create_collection) | **POST** /collections | Create a Collection
[**delete_collection**](CollectionsApi.md#delete_collection) | **DELETE** /collections/{id} | Delete a Collection
[**get_collection**](CollectionsApi.md#get_collection) | **GET** /collections/{id} | Retrieve a Collection
[**get_collections**](CollectionsApi.md#get_collections) | **GET** /collections | List Collections
[**update_collection**](CollectionsApi.md#update_collection) | **PATCH** /collections/{id} | Update a Collection

# **create_collection**
> InlineResponse20016 create_collection(body=body, meta=meta)

Create a Collection

Create a new collection in Directus.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
body = swagger_client.CollectionsBody() # CollectionsBody |  (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Create a Collection
    api_response = api_instance.create_collection(body=body, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->create_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionsBody**](CollectionsBody.md)|  | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection**
> delete_collection(id)

Delete a Collection

Delete an existing collection. Warning: This will delete the whole collection, including the items within. Proceed with caution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
id = 'id_example' # str | Unique identifier of the collection.

try:
    # Delete a Collection
    api_instance.delete_collection(id)
except ApiException as e:
    print("Exception when calling CollectionsApi->delete_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the collection. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection**
> InlineResponse20016 get_collection(id, meta=meta)

Retrieve a Collection

Retrieves the details of a single collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
id = 'id_example' # str | Unique identifier of the collection.
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Retrieve a Collection
    api_response = api_instance.get_collection(id, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->get_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the collection. | 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collections**
> InlineResponse20015 get_collections(offset=offset, meta=meta)

List Collections

Returns a list of the collections available in the project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
offset = 56 # int | How many items to skip when fetching data. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # List Collections
    api_response = api_instance.get_collections(offset=offset, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->get_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| How many items to skip when fetching data. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collection**
> InlineResponse20016 update_collection(id, body=body, meta=meta)

Update a Collection

Update an existing collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CollectionsApi()
id = 'id_example' # str | Unique identifier of the collection.
body = swagger_client.CollectionsIdBody() # CollectionsIdBody |  (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Update a Collection
    api_response = api_instance.update_collection(id, body=body, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionsApi->update_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier of the collection. | 
 **body** | [**CollectionsIdBody**](CollectionsIdBody.md)|  | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

