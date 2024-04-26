# swagger_client.FoldersApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_folder**](FoldersApi.md#create_folder) | **POST** /folders | Create a Folder
[**delete_folder**](FoldersApi.md#delete_folder) | **DELETE** /folders/{id} | Delete a Folder
[**delete_folders**](FoldersApi.md#delete_folders) | **DELETE** /folders | Delete Multiple Folders
[**get_folder**](FoldersApi.md#get_folder) | **GET** /folders/{id} | Retrieve a Folder
[**get_folders**](FoldersApi.md#get_folders) | **GET** /folders | List Folders
[**update_folder**](FoldersApi.md#update_folder) | **PATCH** /folders/{id} | Update a Folder
[**update_folders**](FoldersApi.md#update_folders) | **PATCH** /folders | Update Multiple Folders

# **create_folder**
> InlineResponse20026 create_folder(body=body, fields=fields, meta=meta)

Create a Folder

Create a new folder.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FoldersApi()
body = swagger_client.FoldersBody() # FoldersBody |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Create a Folder
    api_response = api_instance.create_folder(body=body, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FoldersApi->create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FoldersBody**](FoldersBody.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> delete_folder(id)

Delete a Folder

Delete an existing folder

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FoldersApi()
id = 'id_example' # str | Unique identifier for the object.

try:
    # Delete a Folder
    api_instance.delete_folder(id)
except ApiException as e:
    print("Exception when calling FoldersApi->delete_folder: %s\n" % e)
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

# **delete_folders**
> delete_folders()

Delete Multiple Folders

Delete multiple existing folders.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FoldersApi()

try:
    # Delete Multiple Folders
    api_instance.delete_folders()
except ApiException as e:
    print("Exception when calling FoldersApi->delete_folders: %s\n" % e)
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

# **get_folder**
> InlineResponse20026 get_folder(id, fields=fields, meta=meta)

Retrieve a Folder

Retrieve a single folder by unique identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FoldersApi()
id = 'id_example' # str | Unique identifier for the object.
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Retrieve a Folder
    api_response = api_instance.get_folder(id, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FoldersApi->get_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the object. | 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folders**
> InlineResponse20025 get_folders(fields=fields, limit=limit, offset=offset, sort=sort, filter=filter, search=search, meta=meta)

List Folders

List the folders.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FoldersApi()
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # List Folders
    api_response = api_instance.get_folders(fields=fields, limit=limit, offset=offset, sort=sort, filter=filter, search=search, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FoldersApi->get_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **limit** | **int**| A limit on the number of objects that are returned. | [optional] 
 **offset** | **int**| How many items to skip when fetching data. | [optional] 
 **sort** | [**list[str]**](str.md)| How to sort the returned items. &#x60;sort&#x60; is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (&#x60; - &#x60;) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a &#x60; ? &#x60; to sort randomly.  | [optional] 
 **filter** | [**object**](.md)| Select items in collection by given conditions. | [optional] 
 **search** | **str**| Filter by items that contain the given search query in one of their fields. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folder**
> InlineResponse20026 update_folder(id, body=body, fields=fields, meta=meta)

Update a Folder

Update an existing folder

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FoldersApi()
id = 'id_example' # str | Unique identifier for the object.
body = swagger_client.FoldersIdBody() # FoldersIdBody |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Update a Folder
    api_response = api_instance.update_folder(id, body=body, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FoldersApi->update_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique identifier for the object. | 
 **body** | [**FoldersIdBody**](FoldersIdBody.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folders**
> InlineResponse20025 update_folders(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)

Update Multiple Folders

Update multiple folders at the same time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FoldersApi()
body = swagger_client.FoldersBody1() # FoldersBody1 |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)

try:
    # Update Multiple Folders
    api_response = api_instance.update_folders(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FoldersApi->update_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FoldersBody1**](FoldersBody1.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **limit** | **int**| A limit on the number of objects that are returned. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 
 **offset** | **int**| How many items to skip when fetching data. | [optional] 
 **sort** | [**list[str]**](str.md)| How to sort the returned items. &#x60;sort&#x60; is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (&#x60; - &#x60;) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a &#x60; ? &#x60; to sort randomly.  | [optional] 
 **filter** | [**object**](.md)| Select items in collection by given conditions. | [optional] 
 **search** | **str**| Filter by items that contain the given search query in one of their fields. | [optional] 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

