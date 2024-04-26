# swagger_client.ItemsScrapeConfigApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_items_scrape_config**](ItemsScrapeConfigApi.md#create_items_scrape_config) | **POST** /items/scrape_config | Create an Item
[**delete_items_scrape_config**](ItemsScrapeConfigApi.md#delete_items_scrape_config) | **DELETE** /items/scrape_config | Delete Multiple Items
[**delete_single_items_scrape_config**](ItemsScrapeConfigApi.md#delete_single_items_scrape_config) | **DELETE** /items/scrape_config/{id} | Delete an Item
[**read_items_scrape_config**](ItemsScrapeConfigApi.md#read_items_scrape_config) | **GET** /items/scrape_config | List Items
[**read_single_items_scrape_config**](ItemsScrapeConfigApi.md#read_single_items_scrape_config) | **GET** /items/scrape_config/{id} | Retrieve an Item
[**update_items_scrape_config**](ItemsScrapeConfigApi.md#update_items_scrape_config) | **PATCH** /items/scrape_config | Update Multiple Items
[**update_single_items_scrape_config**](ItemsScrapeConfigApi.md#update_single_items_scrape_config) | **PATCH** /items/scrape_config/{id} | Update an Item

# **create_items_scrape_config**
> InlineResponse20056 create_items_scrape_config(body=body, meta=meta)

Create an Item

Create a new scrape_config item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsScrapeConfigApi()
body = swagger_client.ItemsScrapeConfigBody() # ItemsScrapeConfigBody |  (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Create an Item
    api_response = api_instance.create_items_scrape_config(body=body, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsScrapeConfigApi->create_items_scrape_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemsScrapeConfigBody**](ItemsScrapeConfigBody.md)|  | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_items_scrape_config**
> delete_items_scrape_config()

Delete Multiple Items

Delete multiple existing scrape_config items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsScrapeConfigApi()

try:
    # Delete Multiple Items
    api_instance.delete_items_scrape_config()
except ApiException as e:
    print("Exception when calling ItemsScrapeConfigApi->delete_items_scrape_config: %s\n" % e)
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

# **delete_single_items_scrape_config**
> delete_single_items_scrape_config(id)

Delete an Item

Delete an existing scrape_config item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsScrapeConfigApi()
id = swagger_client.Id10() # Id10 | Index of the item.

try:
    # Delete an Item
    api_instance.delete_single_items_scrape_config(id)
except ApiException as e:
    print("Exception when calling ItemsScrapeConfigApi->delete_single_items_scrape_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id10**](.md)| Index of the item. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_items_scrape_config**
> InlineResponse20055 read_items_scrape_config(fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)

List Items

List the scrape_config items.

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
api_instance = swagger_client.ItemsScrapeConfigApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)

try:
    # List Items
    api_response = api_instance.read_items_scrape_config(fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsScrapeConfigApi->read_items_scrape_config: %s\n" % e)
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

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

[Auth](../README.md#Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_single_items_scrape_config**
> InlineResponse20058 read_single_items_scrape_config(id, fields=fields, meta=meta, version=version)

Retrieve an Item

Retrieve a single scrape_config item by unique identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsScrapeConfigApi()
id = swagger_client.Id9() # Id9 | Index of the item.
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
version = 'version_example' # str | Retrieve an item's state from a specific Content Version. The value corresponds to the \"key\" of the Content Version.  (optional)

try:
    # Retrieve an Item
    api_response = api_instance.read_single_items_scrape_config(id, fields=fields, meta=meta, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsScrapeConfigApi->read_single_items_scrape_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id9**](.md)| Index of the item. | 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 
 **version** | **str**| Retrieve an item&#x27;s state from a specific Content Version. The value corresponds to the \&quot;key\&quot; of the Content Version.  | [optional] 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_items_scrape_config**
> InlineResponse20057 update_items_scrape_config(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)

Update Multiple Items

Update multiple scrape_config items at the same time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsScrapeConfigApi()
body = swagger_client.ItemsScrapeConfigBody1() # ItemsScrapeConfigBody1 |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)

try:
    # Update Multiple Items
    api_response = api_instance.update_items_scrape_config(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsScrapeConfigApi->update_items_scrape_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ItemsScrapeConfigBody1**](ItemsScrapeConfigBody1.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **limit** | **int**| A limit on the number of objects that are returned. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 
 **offset** | **int**| How many items to skip when fetching data. | [optional] 
 **sort** | [**list[str]**](str.md)| How to sort the returned items. &#x60;sort&#x60; is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (&#x60; - &#x60;) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a &#x60; ? &#x60; to sort randomly.  | [optional] 
 **filter** | [**object**](.md)| Select items in collection by given conditions. | [optional] 
 **search** | **str**| Filter by items that contain the given search query in one of their fields. | [optional] 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_single_items_scrape_config**
> InlineResponse20058 update_single_items_scrape_config(id, body=body, fields=fields, meta=meta)

Update an Item

Update an existing scrape_config item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ItemsScrapeConfigApi()
id = swagger_client.Id11() # Id11 | Index of the item.
body = swagger_client.ItemsScrapeConfig() # ItemsScrapeConfig |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Update an Item
    api_response = api_instance.update_single_items_scrape_config(id, body=body, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsScrapeConfigApi->update_single_items_scrape_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**Id11**](.md)| Index of the item. | 
 **body** | [**ItemsScrapeConfig**](ItemsScrapeConfig.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

