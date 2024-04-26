# swagger_client.PresetsApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_preset**](PresetsApi.md#create_preset) | **POST** /presets | Create a Preset
[**delete_preset**](PresetsApi.md#delete_preset) | **DELETE** /presets/{id} | Delete a Preset
[**delete_presets**](PresetsApi.md#delete_presets) | **DELETE** /presets | Delete Multiple Presets
[**get_preset**](PresetsApi.md#get_preset) | **GET** /presets/{id} | Retrieve a Preset
[**get_presets**](PresetsApi.md#get_presets) | **GET** /presets | List Presets
[**update_preset**](PresetsApi.md#update_preset) | **PATCH** /presets/{id} | Update a Preset
[**update_presets**](PresetsApi.md#update_presets) | **PATCH** /presets | Update Multiple Presets

# **create_preset**
> InlineResponse20033 create_preset(body=body, fields=fields, meta=meta)

Create a Preset

Create a new preset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresetsApi()
body = swagger_client.PresetsBody() # PresetsBody |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Create a Preset
    api_response = api_instance.create_preset(body=body, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresetsApi->create_preset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PresetsBody**](PresetsBody.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_preset**
> delete_preset(id)

Delete a Preset

Delete an existing preset.

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
api_instance = swagger_client.PresetsApi(swagger_client.ApiClient(configuration))
id = 56 # int | Index

try:
    # Delete a Preset
    api_instance.delete_preset(id)
except ApiException as e:
    print("Exception when calling PresetsApi->delete_preset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Index | 

### Return type

void (empty response body)

### Authorization

[Auth](../README.md#Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_presets**
> delete_presets()

Delete Multiple Presets

Delete multiple existing presets.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresetsApi()

try:
    # Delete Multiple Presets
    api_instance.delete_presets()
except ApiException as e:
    print("Exception when calling PresetsApi->delete_presets: %s\n" % e)
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

# **get_preset**
> InlineResponse20033 get_preset(id, fields=fields, meta=meta)

Retrieve a Preset

Retrieve a single preset by unique identifier.

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
api_instance = swagger_client.PresetsApi(swagger_client.ApiClient(configuration))
id = 56 # int | Index
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Retrieve a Preset
    api_response = api_instance.get_preset(id, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresetsApi->get_preset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Index | 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[Auth](../README.md#Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_presets**
> InlineResponse20032 get_presets(fields=fields, limit=limit, offset=offset, page=page, sort=sort, filter=filter, search=search, meta=meta)

List Presets

List the presets.

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
api_instance = swagger_client.PresetsApi(swagger_client.ApiClient(configuration))
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
page = 56 # int | Cursor for use in pagination. Often used in combination with limit. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # List Presets
    api_response = api_instance.get_presets(fields=fields, limit=limit, offset=offset, page=page, sort=sort, filter=filter, search=search, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresetsApi->get_presets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **limit** | **int**| A limit on the number of objects that are returned. | [optional] 
 **offset** | **int**| How many items to skip when fetching data. | [optional] 
 **page** | **int**| Cursor for use in pagination. Often used in combination with limit. | [optional] 
 **sort** | [**list[str]**](str.md)| How to sort the returned items. &#x60;sort&#x60; is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (&#x60; - &#x60;) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a &#x60; ? &#x60; to sort randomly.  | [optional] 
 **filter** | [**object**](.md)| Select items in collection by given conditions. | [optional] 
 **search** | **str**| Filter by items that contain the given search query in one of their fields. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[Auth](../README.md#Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_preset**
> InlineResponse20033 update_preset(id, body=body, fields=fields, meta=meta)

Update a Preset

Update an existing preset.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresetsApi()
id = 56 # int | Index
body = swagger_client.PresetsIdBody() # PresetsIdBody |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Update a Preset
    api_response = api_instance.update_preset(id, body=body, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresetsApi->update_preset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Index | 
 **body** | [**PresetsIdBody**](PresetsIdBody.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_presets**
> InlineResponse20032 update_presets(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)

Update Multiple Presets

Update multiple presets at the same time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PresetsApi()
body = swagger_client.PresetsBody1() # PresetsBody1 |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)

try:
    # Update Multiple Presets
    api_response = api_instance.update_presets(body=body, fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PresetsApi->update_presets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PresetsBody1**](PresetsBody1.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **limit** | **int**| A limit on the number of objects that are returned. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 
 **offset** | **int**| How many items to skip when fetching data. | [optional] 
 **sort** | [**list[str]**](str.md)| How to sort the returned items. &#x60;sort&#x60; is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (&#x60; - &#x60;) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a &#x60; ? &#x60; to sort randomly.  | [optional] 
 **filter** | [**object**](.md)| Select items in collection by given conditions. | [optional] 
 **search** | **str**| Filter by items that contain the given search query in one of their fields. | [optional] 

### Return type

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

