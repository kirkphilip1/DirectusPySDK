# swagger_client.AuthenticationApi

All URIs are relative to *api.kirknetllc.com:8055*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthenticationApi.md#login) | **POST** /auth/login | Retrieve a Temporary Access Token
[**logout**](AuthenticationApi.md#logout) | **POST** /auth/logout | Log Out
[**oauth**](AuthenticationApi.md#oauth) | **GET** /auth/oauth | List OAuth Providers
[**oauth_provider**](AuthenticationApi.md#oauth_provider) | **GET** /auth/oauth/{provider} | Authenticated using an OAuth provider
[**password_request**](AuthenticationApi.md#password_request) | **POST** /auth/password/request | Request a Password Reset
[**password_reset**](AuthenticationApi.md#password_reset) | **POST** /auth/password/reset | Reset a Password
[**refresh**](AuthenticationApi.md#refresh) | **POST** /auth/refresh | Refresh Token

# **login**
> InlineResponse200 login(body=body)

Retrieve a Temporary Access Token

Retrieve a Temporary Access Token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.AuthLoginBody() # AuthLoginBody |  (optional)

try:
    # Retrieve a Temporary Access Token
    api_response = api_instance.login(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthLoginBody**](AuthLoginBody.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout(body=body)

Log Out

Log Out

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.AuthLogoutBody() # AuthLogoutBody |  (optional)

try:
    # Log Out
    api_instance.logout(body=body)
except ApiException as e:
    print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthLogoutBody**](AuthLogoutBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth**
> InlineResponse2002 oauth()

List OAuth Providers

List configured OAuth providers.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()

try:
    # List OAuth Providers
    api_response = api_instance.oauth()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->oauth: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_provider**
> InlineResponse2003 oauth_provider(provider, redirect=redirect)

Authenticated using an OAuth provider

Start OAuth flow using the specified provider

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
provider = 'provider_example' # str | Key of the activated OAuth provider.
redirect = 'redirect_example' # str | Where to redirect on successful login.<br/>If set the authentication details are set inside cookies otherwise a JSON is returned. (optional)

try:
    # Authenticated using an OAuth provider
    api_response = api_instance.oauth_provider(provider, redirect=redirect)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->oauth_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| Key of the activated OAuth provider. | 
 **redirect** | **str**| Where to redirect on successful login.&lt;br/&gt;If set the authentication details are set inside cookies otherwise a JSON is returned. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_request**
> password_request(body=body)

Request a Password Reset

Request a reset password email to be send.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.PasswordRequestBody() # PasswordRequestBody |  (optional)

try:
    # Request a Password Reset
    api_instance.password_request(body=body)
except ApiException as e:
    print("Exception when calling AuthenticationApi->password_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordRequestBody**](PasswordRequestBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **password_reset**
> password_reset(body=body)

Reset a Password

The request a password reset endpoint sends an email with a link to the admin app which in turn uses this endpoint to allow the user to reset their password.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.PasswordResetBody() # PasswordResetBody |  (optional)

try:
    # Reset a Password
    api_instance.password_reset(body=body)
except ApiException as e:
    print("Exception when calling AuthenticationApi->password_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PasswordResetBody**](PasswordResetBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh**
> InlineResponse2001 refresh(body=body)

Refresh Token

Refresh a Temporary Access Token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.AuthRefreshBody() # AuthRefreshBody |  (optional)

try:
    # Refresh Token
    api_response = api_instance.refresh(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthRefreshBody**](AuthRefreshBody.md)|  | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

