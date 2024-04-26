# swagger_client.VersionsApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compare_content_version**](VersionsApi.md#compare_content_version) | **GET** /versions/{id}/compare | Compare a Content Version
[**create_content_version**](VersionsApi.md#create_content_version) | **POST** /versions | Create Multiple Content Versions
[**delete_content_version**](VersionsApi.md#delete_content_version) | **DELETE** /versions/{id} | Delete a Content Version
[**delete_content_versions**](VersionsApi.md#delete_content_versions) | **DELETE** /versions | Delete Multiple Content Versions
[**get_content_version**](VersionsApi.md#get_content_version) | **GET** /versions/{id} | Retrieve a Content Version
[**get_content_versions**](VersionsApi.md#get_content_versions) | **GET** /versions | List Content Versions
[**promote_content_version**](VersionsApi.md#promote_content_version) | **POST** /versions/{id}/promote | Promote a Content Version
[**save_content_version**](VersionsApi.md#save_content_version) | **POST** /versions/{id}/save | Save to a Content Version
[**update_content_version**](VersionsApi.md#update_content_version) | **PATCH** /versions/{id} | Update a Content Version
[**update_content_versions**](VersionsApi.md#update_content_versions) | **PATCH** /versions | Update Multiple Content Versions

# **compare_content_version**
> InlineResponse2005 compare_content_version(id)

Compare a Content Version

Compare an existing Content Version with the main version of the item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionsApi()
id = 'id_example' # str | Unique identifier for the object.

try:
    # Compare a Content Version
    api_response = api_instance.compare_content_version(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->compare_content_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the object. | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_content_version**
> InlineResponse20044 create_content_version(body=body, fields=fields, meta=meta)

Create Multiple Content Versions

Create multiple new Content Versions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionsApi()
body = swagger_client.VersionsBody() # VersionsBody |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Create Multiple Content Versions
    api_response = api_instance.create_content_version(body=body, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->create_content_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VersionsBody**](VersionsBody.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_content_version**
> delete_content_version(id)

Delete a Content Version

Delete an existing Content Version.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionsApi()
id = 'id_example' # str | Unique identifier for the object.

try:
    # Delete a Content Version
    api_instance.delete_content_version(id)
except ApiException as e:
    print("Exception when calling VersionsApi->delete_content_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_content_versions**
> delete_content_versions()

Delete Multiple Content Versions

Delete multiple existing Content Versions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionsApi()

try:
    # Delete Multiple Content Versions
    api_instance.delete_content_versions()
except ApiException as e:
    print("Exception when calling VersionsApi->delete_content_versions: %s\n" % e)
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

# **get_content_version**
> InlineResponse20044 get_content_version(id, fields=fields, meta=meta)

Retrieve a Content Version

Retrieve a single Content Version by unique identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionsApi()
id = 'id_example' # str | Unique identifier for the object.
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Retrieve a Content Version
    api_response = api_instance.get_content_version(id, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->get_content_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the object. | 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_content_versions**
> InlineResponse20043 get_content_versions(fields=fields, limit=limit, offset=offset, meta=meta, sort=sort, filter=filter, search=search)

List Content Versions

Get all Content Versions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionsApi()
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)

try:
    # List Content Versions
    api_response = api_instance.get_content_versions(fields=fields, limit=limit, offset=offset, meta=meta, sort=sort, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->get_content_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **limit** | **int**| A limit on the number of objects that are returned. | [optional] 
 **offset** | **int**| How many items to skip when fetching data. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 
 **sort** | [**list[str]**](str.md)| How to sort the returned items. &#x60;sort&#x60; is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (&#x60; - &#x60;) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a &#x60; ? &#x60; to sort randomly.  | [optional] 
 **filter** | [**object**](.md)| Select items in collection by given conditions. | [optional] 
 **search** | **str**| Filter by items that contain the given search query in one of their fields. | [optional] 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **promote_content_version**
> object promote_content_version(id, body=body)

Promote a Content Version

Pass the current hash of the main version of the item (obtained from the `compare` endpoint) along with an optional array of field names of which the values are to be promoted (by default, all fields are selected).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionsApi()
id = 'id_example' # str | Unique identifier for the object.
body = swagger_client.IdPromoteBody() # IdPromoteBody |  (optional)

try:
    # Promote a Content Version
    api_response = api_instance.promote_content_version(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->promote_content_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the object. | 
 **body** | [**IdPromoteBody**](IdPromoteBody.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_content_version**
> object save_content_version(id, body=body)

Save to a Content Version

Save item changes to an existing Content Version.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionsApi()
id = 'id_example' # str | Unique identifier for the object.
body = NULL # object |  (optional)

try:
    # Save to a Content Version
    api_response = api_instance.save_content_version(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->save_content_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the object. | 
 **body** | [**object**](object.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_content_version**
> InlineResponse20044 update_content_version(id, body=body, fields=fields, meta=meta)

Update a Content Version

Update an existing Content Version.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionsApi()
id = 'id_example' # str | Unique identifier for the object.
body = swagger_client.VersionsIdBody() # VersionsIdBody |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Update a Content Version
    api_response = api_instance.update_content_version(id, body=body, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->update_content_version: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the object. | 
 **body** | [**VersionsIdBody**](VersionsIdBody.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_content_versions**
> InlineResponse20043 update_content_versions(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)

Update Multiple Content Versions

Update multiple Content Versions at the same time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionsApi()
body = swagger_client.VersionsBody1() # VersionsBody1 |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)

try:
    # Update Multiple Content Versions
    api_response = api_instance.update_content_versions(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionsApi->update_content_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VersionsBody1**](VersionsBody1.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **limit** | **int**| A limit on the number of objects that are returned. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 
 **offset** | **int**| How many items to skip when fetching data. | [optional] 
 **sort** | [**list[str]**](str.md)| How to sort the returned items. &#x60;sort&#x60; is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (&#x60; - &#x60;) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a &#x60; ? &#x60; to sort randomly.  | [optional] 
 **filter** | [**object**](.md)| Select items in collection by given conditions. | [optional] 
 **search** | **str**| Filter by items that contain the given search query in one of their fields. | [optional] 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

