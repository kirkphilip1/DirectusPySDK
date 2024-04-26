# swagger_client.SchemaApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schema_apply**](SchemaApi.md#schema_apply) | **POST** /schema/apply | Apply Schema Difference
[**schema_diff**](SchemaApi.md#schema_diff) | **POST** /schema/diff | Retrieve Schema Difference
[**schema_snapshot**](SchemaApi.md#schema_snapshot) | **GET** /schema/snapshot | Retrieve Schema Snapshot

# **schema_apply**
> schema_apply(body)

Apply Schema Difference

Update the instance's schema by passing the diff previously retrieved via `/schema/diff` endpoint in the JSON request body or a JSON/YAML file. This endpoint is only available to admin users.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchemaApi()
body = swagger_client.SchemaApplyBody() # SchemaApplyBody | 

try:
    # Apply Schema Difference
    api_instance.schema_apply(body)
except ApiException as e:
    print("Exception when calling SchemaApi->schema_apply: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SchemaApplyBody**](SchemaApplyBody.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schema_diff**
> SchemaApplyBody schema_diff(body, force=force)

Retrieve Schema Difference

Compare the current instance's schema against the schema snapshot in JSON request body or a JSON/YAML file and retrieve the difference. This endpoint is only available to admin users.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchemaApi()
body = swagger_client.SchemaDiffBody() # SchemaDiffBody | 
force = true # bool | Bypass version and database vendor restrictions. (optional)

try:
    # Retrieve Schema Difference
    api_response = api_instance.schema_diff(body, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->schema_diff: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SchemaDiffBody**](SchemaDiffBody.md)|  | 
 **force** | **bool**| Bypass version and database vendor restrictions. | [optional] 

### Return type

[**SchemaApplyBody**](SchemaApplyBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schema_snapshot**
> InlineResponse2004 schema_snapshot(export=export)

Retrieve Schema Snapshot

Retrieve the current schema. This endpoint is only available to admin users.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SchemaApi()
export = 'export_example' # str | Saves the API response to a file. Accepts one of \"csv\", \"json\", \"xml\", \"yaml\". (optional)

try:
    # Retrieve Schema Snapshot
    api_response = api_instance.schema_snapshot(export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchemaApi->schema_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export** | **str**| Saves the API response to a file. Accepts one of \&quot;csv\&quot;, \&quot;json\&quot;, \&quot;xml\&quot;, \&quot;yaml\&quot;. | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/yaml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

