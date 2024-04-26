# swagger_client.ItemsScrapeHashesApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_items_scrape_hashes**](ItemsScrapeHashesApi.md#create_items_scrape_hashes) | **POST** /items/scrape_hashes | Create an Item
[**delete_items_scrape_hashes**](ItemsScrapeHashesApi.md#delete_items_scrape_hashes) | **DELETE** /items/scrape_hashes | Delete Multiple Items
[**delete_single_items_scrape_hashes**](ItemsScrapeHashesApi.md#delete_single_items_scrape_hashes) | **DELETE** /items/scrape_hashes/{id} | Delete an Item
[**read_items_scrape_hashes**](ItemsScrapeHashesApi.md#read_items_scrape_hashes) | **GET** /items/scrape_hashes | List Items
[**read_single_items_scrape_hashes**](ItemsScrapeHashesApi.md#read_single_items_scrape_hashes) | **GET** /items/scrape_hashes/{id} | Retrieve an Item
[**update_items_scrape_hashes**](ItemsScrapeHashesApi.md#update_items_scrape_hashes) | **PATCH** /items/scrape_hashes | Update Multiple Items
[**update_single_items_scrape_hashes**](ItemsScrapeHashesApi.md#update_single_items_scrape_hashes) | **PATCH** /items/scrape_hashes/{id} | Update an Item

# **create_items_scrape_hashes**
> InlineResponse20060 create_items_scrape_hashes(body=body, meta=meta)

Create an Item

Create a new scrape_hashes item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsScrapeHashesApi()
body = swagger_client.ItemsScrapeHashesBody() # ItemsScrapeHashesBody |  (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Create an Item
    api_response = api_instance.create_items_scrape_hashes(body=body, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsScrapeHashesApi->create_items_scrape_hashes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemsScrapeHashesBody**](ItemsScrapeHashesBody.md)|  | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_items_scrape_hashes**
> delete_items_scrape_hashes()

Delete Multiple Items

Delete multiple existing scrape_hashes items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsScrapeHashesApi()

try:
    # Delete Multiple Items
    api_instance.delete_items_scrape_hashes()
except ApiException as e:
    print("Exception when calling ItemsScrapeHashesApi->delete_items_scrape_hashes: %s\n" % e)
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

# **delete_single_items_scrape_hashes**
> delete_single_items_scrape_hashes(id)

Delete an Item

Delete an existing scrape_hashes item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsScrapeHashesApi()
id = swagger_client.Id13() # Id13 | Index of the item.

try:
    # Delete an Item
    api_instance.delete_single_items_scrape_hashes(id)
except ApiException as e:
    print("Exception when calling ItemsScrapeHashesApi->delete_single_items_scrape_hashes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id13**](.md)| Index of the item. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_items_scrape_hashes**
> InlineResponse20059 read_items_scrape_hashes(fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)

List Items

List the scrape_hashes items.

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
api_instance = swagger_client.ItemsScrapeHashesApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)

try:
    # List Items
    api_response = api_instance.read_items_scrape_hashes(fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsScrapeHashesApi->read_items_scrape_hashes: %s\n" % e)
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

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[Auth](../README.md#Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_single_items_scrape_hashes**
> InlineResponse20062 read_single_items_scrape_hashes(id, fields=fields, meta=meta, version=version)

Retrieve an Item

Retrieve a single scrape_hashes item by unique identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsScrapeHashesApi()
id = swagger_client.Id12() # Id12 | Index of the item.
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
version = 'version_example' # str | Retrieve an item's state from a specific Content Version. The value corresponds to the \"key\" of the Content Version.  (optional)

try:
    # Retrieve an Item
    api_response = api_instance.read_single_items_scrape_hashes(id, fields=fields, meta=meta, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsScrapeHashesApi->read_single_items_scrape_hashes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id12**](.md)| Index of the item. | 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 
 **version** | **str**| Retrieve an item&#x27;s state from a specific Content Version. The value corresponds to the \&quot;key\&quot; of the Content Version.  | [optional] 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_items_scrape_hashes**
> InlineResponse20061 update_items_scrape_hashes(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)

Update Multiple Items

Update multiple scrape_hashes items at the same time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsScrapeHashesApi()
body = swagger_client.ItemsScrapeHashesBody1() # ItemsScrapeHashesBody1 |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)

try:
    # Update Multiple Items
    api_response = api_instance.update_items_scrape_hashes(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsScrapeHashesApi->update_items_scrape_hashes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemsScrapeHashesBody1**](ItemsScrapeHashesBody1.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **limit** | **int**| A limit on the number of objects that are returned. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 
 **offset** | **int**| How many items to skip when fetching data. | [optional] 
 **sort** | [**list[str]**](str.md)| How to sort the returned items. &#x60;sort&#x60; is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (&#x60; - &#x60;) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a &#x60; ? &#x60; to sort randomly.  | [optional] 
 **filter** | [**object**](.md)| Select items in collection by given conditions. | [optional] 
 **search** | **str**| Filter by items that contain the given search query in one of their fields. | [optional] 

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_single_items_scrape_hashes**
> InlineResponse20062 update_single_items_scrape_hashes(id, body=body, fields=fields, meta=meta)

Update an Item

Update an existing scrape_hashes item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsScrapeHashesApi()
id = swagger_client.Id14() # Id14 | Index of the item.
body = swagger_client.ItemsScrapeHashes() # ItemsScrapeHashes |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Update an Item
    api_response = api_instance.update_single_items_scrape_hashes(id, body=body, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsScrapeHashesApi->update_single_items_scrape_hashes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id14**](.md)| Index of the item. | 
 **body** | [**ItemsScrapeHashes**](ItemsScrapeHashes.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

