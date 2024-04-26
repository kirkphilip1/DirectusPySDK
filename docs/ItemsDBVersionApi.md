# swagger_client.ItemsDBVersionApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_items_db_version**](ItemsDBVersionApi.md#create_items_db_version) | **POST** /items/db_version | Create an Item
[**delete_items_db_version**](ItemsDBVersionApi.md#delete_items_db_version) | **DELETE** /items/db_version | Delete Multiple Items
[**delete_single_items_db_version**](ItemsDBVersionApi.md#delete_single_items_db_version) | **DELETE** /items/db_version/{id} | Delete an Item
[**read_items_db_version**](ItemsDBVersionApi.md#read_items_db_version) | **GET** /items/db_version | List Items
[**read_single_items_db_version**](ItemsDBVersionApi.md#read_single_items_db_version) | **GET** /items/db_version/{id} | Retrieve an Item
[**update_items_db_version**](ItemsDBVersionApi.md#update_items_db_version) | **PATCH** /items/db_version | Update Multiple Items
[**update_single_items_db_version**](ItemsDBVersionApi.md#update_single_items_db_version) | **PATCH** /items/db_version/{id} | Update an Item

# **create_items_db_version**
> InlineResponse20010 create_items_db_version(body=body, meta=meta)

Create an Item

Create a new db_version item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsDBVersionApi()
body = swagger_client.ItemsDbVersionBody() # ItemsDbVersionBody |  (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Create an Item
    api_response = api_instance.create_items_db_version(body=body, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsDBVersionApi->create_items_db_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemsDbVersionBody**](ItemsDbVersionBody.md)|  | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_items_db_version**
> delete_items_db_version()

Delete Multiple Items

Delete multiple existing db_version items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsDBVersionApi()

try:
    # Delete Multiple Items
    api_instance.delete_items_db_version()
except ApiException as e:
    print("Exception when calling ItemsDBVersionApi->delete_items_db_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_single_items_db_version**
> delete_single_items_db_version(id)

Delete an Item

Delete an existing db_version item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsDBVersionApi()
id = swagger_client.Id1() # Id1 | Index of the item.

try:
    # Delete an Item
    api_instance.delete_single_items_db_version(id)
except ApiException as e:
    print("Exception when calling ItemsDBVersionApi->delete_single_items_db_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id1**](.md)| Index of the item. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_items_db_version**
> InlineResponse2009 read_items_db_version(fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)

List Items

List the db_version items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Auth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ItemsDBVersionApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)

try:
    # List Items
    api_response = api_instance.read_items_db_version(fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsDBVersionApi->read_items_db_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **limit** | **int**| A limit on the number of objects that are returned. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 
 **offset** | **int**| How many items to skip when fetching data. | [optional] 
 **sort** | [**list[str]**](str.md)| How to sort the returned items. &#x60;sort&#x60; is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (&#x60; - &#x60;) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a &#x60; ? &#x60; to sort randomly.  | [optional] 
 **filter** | [**object**](.md)| Select items in collection by given conditions. | [optional] 
 **search** | **str**| Filter by items that contain the given search query in one of their fields. | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[Auth](../README.md#Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_single_items_db_version**
> InlineResponse20012 read_single_items_db_version(id, fields=fields, meta=meta, version=version)

Retrieve an Item

Retrieve a single db_version item by unique identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsDBVersionApi()
id = swagger_client.Id() # Id | Index of the item.
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
version = 'version_example' # str | Retrieve an item's state from a specific Content Version. The value corresponds to the \"key\" of the Content Version.  (optional)

try:
    # Retrieve an Item
    api_response = api_instance.read_single_items_db_version(id, fields=fields, meta=meta, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsDBVersionApi->read_single_items_db_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id**](.md)| Index of the item. | 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 
 **version** | **str**| Retrieve an item&#x27;s state from a specific Content Version. The value corresponds to the \&quot;key\&quot; of the Content Version.  | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_items_db_version**
> InlineResponse20011 update_items_db_version(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)

Update Multiple Items

Update multiple db_version items at the same time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsDBVersionApi()
body = swagger_client.ItemsDbVersionBody1() # ItemsDbVersionBody1 |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)

try:
    # Update Multiple Items
    api_response = api_instance.update_items_db_version(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsDBVersionApi->update_items_db_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemsDbVersionBody1**](ItemsDbVersionBody1.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **limit** | **int**| A limit on the number of objects that are returned. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 
 **offset** | **int**| How many items to skip when fetching data. | [optional] 
 **sort** | [**list[str]**](str.md)| How to sort the returned items. &#x60;sort&#x60; is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (&#x60; - &#x60;) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a &#x60; ? &#x60; to sort randomly.  | [optional] 
 **filter** | [**object**](.md)| Select items in collection by given conditions. | [optional] 
 **search** | **str**| Filter by items that contain the given search query in one of their fields. | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_single_items_db_version**
> InlineResponse20012 update_single_items_db_version(id, body=body, fields=fields, meta=meta)

Update an Item

Update an existing db_version item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsDBVersionApi()
id = swagger_client.Id2() # Id2 | Index of the item.
body = swagger_client.ItemsDBVersion() # ItemsDBVersion |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Update an Item
    api_response = api_instance.update_single_items_db_version(id, body=body, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsDBVersionApi->update_single_items_db_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id2**](.md)| Index of the item. | 
 **body** | [**ItemsDBVersion**](ItemsDBVersion.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

