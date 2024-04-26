# swagger_client.RelationsApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_relation**](RelationsApi.md#create_relation) | **POST** /relations | Create a Relation
[**delete_relation**](RelationsApi.md#delete_relation) | **DELETE** /relations/{id} | Delete a Relation
[**get_relation**](RelationsApi.md#get_relation) | **GET** /relations/{id} | Retrieve a Relation
[**get_relations**](RelationsApi.md#get_relations) | **GET** /relations | List Relations
[**update_relation**](RelationsApi.md#update_relation) | **PATCH** /relations/{id} | Update a Relation

# **create_relation**
> InlineResponse20035 create_relation(body=body, fields=fields, meta=meta)

Create a Relation

Create a new relation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationsApi()
body = swagger_client.RelationsBody() # RelationsBody |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Create a Relation
    api_response = api_instance.create_relation(body=body, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->create_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RelationsBody**](RelationsBody.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_relation**
> delete_relation(id)

Delete a Relation

Delete an existing relation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationsApi()
id = 56 # int | Index

try:
    # Delete a Relation
    api_instance.delete_relation(id)
except ApiException as e:
    print("Exception when calling RelationsApi->delete_relation: %s\n" % e)
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

# **get_relation**
> InlineResponse20035 get_relation(id, fields=fields, meta=meta)

Retrieve a Relation

Retrieve a single relation by unique identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationsApi()
id = 56 # int | Index
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Retrieve a Relation
    api_response = api_instance.get_relation(id, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->get_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Index | 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relations**
> InlineResponse20034 get_relations(fields=fields, limit=limit, offset=offset, meta=meta, sort=sort, filter=filter, search=search, page=page)

List Relations

List the relations.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationsApi()
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)
page = 56 # int | Cursor for use in pagination. Often used in combination with limit. (optional)

try:
    # List Relations
    api_response = api_instance.get_relations(fields=fields, limit=limit, offset=offset, meta=meta, sort=sort, filter=filter, search=search, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->get_relations: %s\n" % e)
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

[**InlineResponse20034**](InlineResponse20034.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_relation**
> InlineResponse20035 update_relation(id, body=body, fields=fields, meta=meta)

Update a Relation

Update an existing relation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RelationsApi()
id = 56 # int | Index
body = swagger_client.RelationsIdBody() # RelationsIdBody |  (optional)
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Update a Relation
    api_response = api_instance.update_relation(id, body=body, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RelationsApi->update_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Index | 
 **body** | [**RelationsIdBody**](RelationsIdBody.md)|  | [optional] 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

