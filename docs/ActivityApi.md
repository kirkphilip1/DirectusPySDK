# swagger_client.ActivityApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_comment**](ActivityApi.md#create_comment) | **POST** /activity/comment | Create a Comment
[**delete_comment**](ActivityApi.md#delete_comment) | **DELETE** /activity/comment/{id} | Delete a Comment
[**get_activities**](ActivityApi.md#get_activities) | **GET** /activity | List Activity Actions
[**get_activity**](ActivityApi.md#get_activity) | **GET** /activity/{id} | Retrieve an Activity Action
[**update_comment**](ActivityApi.md#update_comment) | **PATCH** /activity/comment/{id} | Update a Comment

# **create_comment**
> InlineResponse20014 create_comment(body=body, meta=meta)

Create a Comment

Creates a new comment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityApi()
body = swagger_client.ActivityCommentBody() # ActivityCommentBody |  (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Create a Comment
    api_response = api_instance.create_comment(body=body, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->create_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ActivityCommentBody**](ActivityCommentBody.md)|  | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_comment**
> delete_comment(id)

Delete a Comment

Delete an existing comment. Deleted comments can not be retrieved.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityApi()
id = 56 # int | Index

try:
    # Delete a Comment
    api_instance.delete_comment(id)
except ApiException as e:
    print("Exception when calling ActivityApi->delete_comment: %s\n" % e)
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

# **get_activities**
> InlineResponse20013 get_activities(fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)

List Activity Actions

Returns a list of activity actions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityApi()
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
limit = 56 # int | A limit on the number of objects that are returned. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)
offset = 56 # int | How many items to skip when fetching data. (optional)
sort = ['sort_example'] # list[str] | How to sort the returned items. `sort` is a CSV of fields used to sort the fetched items. Sorting defaults to ascending (ASC) order but a minus sign (` - `) can be used to reverse this to descending (DESC) order. Fields are prioritized by their order in the CSV. You can also use a ` ? ` to sort randomly.  (optional)
filter = NULL # object | Select items in collection by given conditions. (optional)
search = 'search_example' # str | Filter by items that contain the given search query in one of their fields. (optional)

try:
    # List Activity Actions
    api_response = api_instance.get_activities(fields=fields, limit=limit, meta=meta, offset=offset, sort=sort, filter=filter, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_activities: %s\n" % e)
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

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_activity**
> InlineResponse20014 get_activity(id, fields=fields, meta=meta)

Retrieve an Activity Action

Retrieves the details of an existing activity action. Provide the primary key of the activity action and Directus will return the corresponding information.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityApi()
id = 56 # int | Index
fields = ['fields_example'] # list[str] | Control what fields are being returned in the object. (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Retrieve an Activity Action
    api_response = api_instance.get_activity(id, fields=fields, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->get_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Index | 
 **fields** | [**list[str]**](str.md)| Control what fields are being returned in the object. | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_comment**
> InlineResponse20014 update_comment(id, body=body, meta=meta)

Update a Comment

Update the content of an existing comment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivityApi()
id = 56 # int | Index
body = swagger_client.CommentIdBody() # CommentIdBody |  (optional)
meta = 'meta_example' # str | What metadata to return in the response. (optional)

try:
    # Update a Comment
    api_response = api_instance.update_comment(id, body=body, meta=meta)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActivityApi->update_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Index | 
 **body** | [**CommentIdBody**](CommentIdBody.md)|  | [optional] 
 **meta** | **str**| What metadata to return in the response. | [optional] 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

