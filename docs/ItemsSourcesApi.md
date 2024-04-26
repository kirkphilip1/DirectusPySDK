# swagger_client.ItemsSourcesApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_items_sources**](ItemsSourcesApi.md#create_items_sources) | **POST** /items/sources | Create an Item
[**delete_items_sources**](ItemsSourcesApi.md#delete_items_sources) | **DELETE** /items/sources | Delete Multiple Items
[**delete_single_items_sources**](ItemsSourcesApi.md#delete_single_items_sources) | **DELETE** /items/sources/{id} | Delete an Item
[**read_items_sources**](ItemsSourcesApi.md#read_items_sources) | **GET** /items/sources | List Items
[**read_single_items_sources**](ItemsSourcesApi.md#read_single_items_sources) | **GET** /items/sources/{id} | Retrieve an Item
[**update_items_sources**](ItemsSourcesApi.md#update_items_sources) | **PATCH** /items/sources | Update Multiple Items
[**update_single_items_sources**](ItemsSourcesApi.md#update_single_items_sources) | **PATCH** /items/sources/{id} | Update an Item

# **create_items_sources**
> InlineResponse20068 create_items_sources(body=body, meta=meta)

Create an Item

Create a new sources item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsSourcesApi()
body = swagger_client.ItemsSourcesBody() # ItemsSourcesBody |  (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Create an Item
    api_response = api_instance.create_items_sources(body=body, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsSourcesApi->create_items_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemsSourcesBody**](ItemsSourcesBody.md)|  | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20068**](InlineResponse20068.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_items_sources**
> delete_items_sources()

Delete Multiple Items

Delete multiple existing sources items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsSourcesApi()

try:
    # Delete Multiple Items
    api_instance.delete_items_sources()
except ApiException as e:
    print("Exception when calling ItemsSourcesApi->delete_items_sources: %s\n" % e)
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

# **delete_single_items_sources**
> delete_single_items_sources(id)

Delete an Item

Delete an existing sources item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsSourcesApi()
id = swagger_client.Id19() # Id19 | Index of the item.

try:
    # Delete an Item
    api_instance.delete_single_items_sources(id)
except ApiException as e:
    print("Exception when calling ItemsSourcesApi->delete_single_items_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id19**](.md)| Index of the item. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_items_sources**
> InlineResponse20067 read_items_sources(fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)

List Items

List the sources items.

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
api_instance = swagger_client.ItemsSourcesApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)

try:
    # List Items
    api_response = api_instance.read_items_sources(fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsSourcesApi->read_items_sources: %s\n" % e)
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

[**InlineResponse20067**](InlineResponse20067.md)

### Authorization

[Auth](../README.md#Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_single_items_sources**
> InlineResponse20070 read_single_items_sources(id, fields=fields, meta=meta, version=version)

Retrieve an Item

Retrieve a single sources item by unique identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsSourcesApi()
id = swagger_client.Id18() # Id18 | Index of the item.
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
version = 'version_example' # str | Retrieve an item's state from a specific Content Version. The value corresponds to the \"key\" of the Content Version.  (optional)

try:
    # Retrieve an Item
    api_response = api_instance.read_single_items_sources(id, fields=fields, meta=meta, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsSourcesApi->read_single_items_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id18**](.md)| Index of the item. | 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 
 **version** | **str**| Retrieve an item&#x27;s state from a specific Content Version. The value corresponds to the \&quot;key\&quot; of the Content Version.  | [optional] 

### Return type

[**InlineResponse20070**](InlineResponse20070.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_items_sources**
> InlineResponse20069 update_items_sources(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)

Update Multiple Items

Update multiple sources items at the same time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsSourcesApi()
body = swagger_client.ItemsSourcesBody1() # ItemsSourcesBody1 |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)

try:
    # Update Multiple Items
    api_response = api_instance.update_items_sources(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsSourcesApi->update_items_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemsSourcesBody1**](ItemsSourcesBody1.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **limit** | **int**| A limit on the number of objects that are returned. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 
 **offset** | **int**| How many items to skip when fetching data. | [optional] 
 **sort** | [**list[str]**](str.md)| How to sort the returned items. &#x60;sort&#x60; is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (&#x60; - &#x60;) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a &#x60; ? &#x60; to sort randomly.  | [optional] 
 **filter** | [**object**](.md)| Select items in collection by given conditions. | [optional] 
 **search** | **str**| Filter by items that contain the given search query in one of their fields. | [optional] 

### Return type

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_single_items_sources**
> InlineResponse20070 update_single_items_sources(id, body=body, fields=fields, meta=meta)

Update an Item

Update an existing sources item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsSourcesApi()
id = swagger_client.Id20() # Id20 | Index of the item.
body = swagger_client.ItemsSources() # ItemsSources |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Update an Item
    api_response = api_instance.update_single_items_sources(id, body=body, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsSourcesApi->update_single_items_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id20**](.md)| Index of the item. | 
 **body** | [**ItemsSources**](ItemsSources.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20070**](InlineResponse20070.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

