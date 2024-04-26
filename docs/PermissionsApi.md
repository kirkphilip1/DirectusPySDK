# swagger_client.PermissionsApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_permission**](PermissionsApi.md#create_permission) | **POST** /permissions | Create a Permission
[**delete_permission**](PermissionsApi.md#delete_permission) | **DELETE** /permissions/{id} | Delete a Permission
[**delete_permissions**](PermissionsApi.md#delete_permissions) | **DELETE** /permissions | Delete Multiple Permissions
[**get_my_permissions**](PermissionsApi.md#get_my_permissions) | **GET** /permissions/me | List My Permissions
[**get_permission**](PermissionsApi.md#get_permission) | **GET** /permissions/{id} | Retrieve a Permission
[**get_permissions**](PermissionsApi.md#get_permissions) | **GET** /permissions | List Permissions
[**update_permission**](PermissionsApi.md#update_permission) | **PATCH** /permissions/{id} | Update a Permission
[**update_permissions**](PermissionsApi.md#update_permissions) | **PATCH** /permissions | Update Multiple Permissions

# **create_permission**
> InlineResponse20030 create_permission(body=body, meta=meta)

Create a Permission

Create a new permission.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
body = swagger_client.PermissionsBody() # PermissionsBody |  (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Create a Permission
    api_response = api_instance.create_permission(body=body, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->create_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermissionsBody**](PermissionsBody.md)|  | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_permission**
> delete_permission(id)

Delete a Permission

Delete an existing permission

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
id = 56 # int | Index

try:
    # Delete a Permission
    api_instance.delete_permission(id)
except ApiException as e:
    print("Exception when calling PermissionsApi->delete_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Index | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_permissions**
> delete_permissions()

Delete Multiple Permissions

Delete multiple existing permissions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()

try:
    # Delete Multiple Permissions
    api_instance.delete_permissions()
except ApiException as e:
    print("Exception when calling PermissionsApi->delete_permissions: %s\n" % e)
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

# **get_my_permissions**
> InlineResponse20031 get_my_permissions()

List My Permissions

List the permissions that apply to the current user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()

try:
    # List My Permissions
    api_response = api_instance.get_my_permissions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_my_permissions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permission**
> InlineResponse20030 get_permission(id, fields=fields, meta=meta)

Retrieve a Permission

Retrieve a single permissions object by unique identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
id = 56 # int | Index
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Retrieve a Permission
    api_response = api_instance.get_permission(id, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Index | 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_permissions**
> InlineResponse20029 get_permissions(fields=fields, limit=limit, offset=offset, meta=meta, sort=sort, filter=filter, search=search, page=page)

List Permissions

List all permissions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)
page = 56 # int | Cursor for use in pagination. Often used in combination with limit. (optional)

try:
    # List Permissions
    api_response = api_instance.get_permissions(fields=fields, limit=limit, offset=offset, meta=meta, sort=sort, filter=filter, search=search, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->get_permissions: %s\n" % e)
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
 **page** | **int**| Cursor for use in pagination. Often used in combination with limit. | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permission**
> InlineResponse20030 update_permission(id, body=body, meta=meta)

Update a Permission

Update an existing permission

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
id = 56 # int | Index
body = swagger_client.PermissionsIdBody() # PermissionsIdBody |  (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Update a Permission
    api_response = api_instance.update_permission(id, body=body, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->update_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Index | 
 **body** | [**PermissionsIdBody**](PermissionsIdBody.md)|  | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20030**](InlineResponse20030.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_permissions**
> InlineResponse20029 update_permissions(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)

Update Multiple Permissions

Update multiple permissions at the same time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PermissionsApi()
body = swagger_client.PermissionsBody1() # PermissionsBody1 |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)

try:
    # Update Multiple Permissions
    api_response = api_instance.update_permissions(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PermissionsApi->update_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PermissionsBody1**](PermissionsBody1.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **limit** | **int**| A limit on the number of objects that are returned. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 
 **offset** | **int**| How many items to skip when fetching data. | [optional] 
 **sort** | [**list[str]**](str.md)| How to sort the returned items. &#x60;sort&#x60; is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (&#x60; - &#x60;) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a &#x60; ? &#x60; to sort randomly.  | [optional] 
 **filter** | [**object**](.md)| Select items in collection by given conditions. | [optional] 
 **search** | **str**| Filter by items that contain the given search query in one of their fields. | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

