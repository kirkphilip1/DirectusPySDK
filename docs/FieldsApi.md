# swagger_client.FieldsApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_field**](FieldsApi.md#create_field) | **POST** /fields/{collection} | Create Field in Collection
[**delete_field**](FieldsApi.md#delete_field) | **DELETE** /fields/{collection}/{id} | Delete a Field
[**get_collection_field**](FieldsApi.md#get_collection_field) | **GET** /fields/{collection}/{id} | Retrieve a Field
[**get_collection_fields**](FieldsApi.md#get_collection_fields) | **GET** /fields/{collection} | List Fields in Collection
[**get_fields**](FieldsApi.md#get_fields) | **GET** /fields | List All Fields
[**update_field**](FieldsApi.md#update_field) | **PATCH** /fields/{collection}/{id} | Update a Field

# **create_field**
> InlineResponse20020 create_field(collection, body=body)

Create Field in Collection

Create a new field in a given collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FieldsApi()
collection = 'collection_example' # str | Unique identifier of the collection the item resides in.
body = swagger_client.FieldsCollectionBody() # FieldsCollectionBody |  (optional)

try:
    # Create Field in Collection
    api_response = api_instance.create_field(collection, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->create_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection the item resides in. | 
 **body** | [**FieldsCollectionBody**](FieldsCollectionBody.md)|  | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_field**
> delete_field(collection, id)

Delete a Field

Delete an existing field.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FieldsApi()
collection = 'collection_example' # str | Unique identifier of the collection the item resides in.
id = 'id_example' # str | Unique identifier of the field.

try:
    # Delete a Field
    api_instance.delete_field(collection, id)
except ApiException as e:
    print("Exception when calling FieldsApi->delete_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection the item resides in. | 
 **id** | **str**| Unique identifier of the field. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_field**
> InlineResponse20020 get_collection_field(collection, id)

Retrieve a Field

Retrieves the details of a single field in a given collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FieldsApi()
collection = 'collection_example' # str | Unique identifier of the collection the item resides in.
id = 'id_example' # str | Unique identifier of the field.

try:
    # Retrieve a Field
    api_response = api_instance.get_collection_field(collection, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->get_collection_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection the item resides in. | 
 **id** | **str**| Unique identifier of the field. | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection_fields**
> InlineResponse20019 get_collection_fields(collection, sort=sort)

List Fields in Collection

Returns a list of the fields available in the given collection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FieldsApi()
collection = 'collection_example' # str | Unique identifier of the collection the item resides in.
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)

try:
    # List Fields in Collection
    api_response = api_instance.get_collection_fields(collection, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->get_collection_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection the item resides in. | 
 **sort** | [**list[str]**](str.md)| How to sort the returned items. &#x60;sort&#x60; is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (&#x60; - &#x60;) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a &#x60; ? &#x60; to sort randomly.  | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fields**
> InlineResponse20019 get_fields(limit=limit, sort=sort)

List All Fields

Returns a list of the fields available in the project.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FieldsApi()
limit = 56 # int | A limit on the number of objects that are returned. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)

try:
    # List All Fields
    api_response = api_instance.get_fields(limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->get_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| A limit on the number of objects that are returned. | [optional] 
 **sort** | [**list[str]**](str.md)| How to sort the returned items. &#x60;sort&#x60; is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (&#x60; - &#x60;) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a &#x60; ? &#x60; to sort randomly.  | [optional] 

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_field**
> InlineResponse20020 update_field(collection, id, body=body)

Update a Field

Update an existing field.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FieldsApi()
collection = 'collection_example' # str | Unique identifier of the collection the item resides in.
id = 'id_example' # str | Unique identifier of the field.
body = swagger_client.CollectionIdBody() # CollectionIdBody |  (optional)

try:
    # Update a Field
    api_response = api_instance.update_field(collection, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FieldsApi->update_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection** | **str**| Unique identifier of the collection the item resides in. | 
 **id** | **str**| Unique identifier of the field. | 
 **body** | [**CollectionIdBody**](CollectionIdBody.md)|  | [optional] 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

