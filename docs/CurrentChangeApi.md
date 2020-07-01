# xepmts_staging.CurrentChangeApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_current_change_item**](CurrentChangeApi.md#delete_current_change_item) | **DELETE** /current_changes/{currentchangeId} | Deletes a CurrentChange document
[**get_current_change_item**](CurrentChangeApi.md#get_current_change_item) | **GET** /current_changes/{currentchangeId} | Retrieves a CurrentChange document
[**get_current_changes**](CurrentChangeApi.md#get_current_changes) | **GET** /current_changes | Retrieves one or more CurrentChanges
[**post_current_changes**](CurrentChangeApi.md#post_current_changes) | **POST** /current_changes | Stores one or more CurrentChanges.
[**put_current_change_item**](CurrentChangeApi.md#put_current_change_item) | **PUT** /current_changes/{currentchangeId} | Replaces a CurrentChange document


# **delete_current_change_item**
> delete_current_change_item(currentchange_id, if_match=if_match)

Deletes a CurrentChange document

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts_staging
from xepmts_staging.rest import ApiException
from pprint import pprint
configuration = xepmts_staging.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.xepmts.yossisprojects.com/v1
configuration.host = "https://api.xepmts.yossisprojects.com/v1"

# Enter a context with an instance of the API client
with xepmts_staging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts_staging.CurrentChangeApi(api_client)
    currentchange_id = 'currentchange_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a CurrentChange document
        api_instance.delete_current_change_item(currentchange_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling CurrentChangeApi->delete_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currentchange_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | CurrentChange document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_change_item**
> CurrentChange get_current_change_item(currentchange_id)

Retrieves a CurrentChange document

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts_staging
from xepmts_staging.rest import ApiException
from pprint import pprint
configuration = xepmts_staging.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.xepmts.yossisprojects.com/v1
configuration.host = "https://api.xepmts.yossisprojects.com/v1"

# Enter a context with an instance of the API client
with xepmts_staging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts_staging.CurrentChangeApi(api_client)
    currentchange_id = 'currentchange_id_example' # str | 

    try:
        # Retrieves a CurrentChange document
        api_response = api_instance.get_current_change_item(currentchange_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CurrentChangeApi->get_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currentchange_id** | **str**|  | 

### Return type

[**CurrentChange**](CurrentChange.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CurrentChange document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_changes**
> InlineResponse2004 get_current_changes(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more CurrentChanges

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts_staging
from xepmts_staging.rest import ApiException
from pprint import pprint
configuration = xepmts_staging.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.xepmts.yossisprojects.com/v1
configuration.host = "https://api.xepmts.yossisprojects.com/v1"

# Enter a context with an instance of the API client
with xepmts_staging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts_staging.CurrentChangeApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more CurrentChanges
        api_response = api_instance.get_current_changes(where=where, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CurrentChangeApi->get_current_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of CurrentChanges |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_current_changes**
> post_current_changes(current_change)

Stores one or more CurrentChanges.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts_staging
from xepmts_staging.rest import ApiException
from pprint import pprint
configuration = xepmts_staging.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.xepmts.yossisprojects.com/v1
configuration.host = "https://api.xepmts.yossisprojects.com/v1"

# Enter a context with an instance of the API client
with xepmts_staging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts_staging.CurrentChangeApi(api_client)
    current_change = xepmts_staging.CurrentChange() # CurrentChange | A CurrentChange or list of CurrentChange documents

    try:
        # Stores one or more CurrentChanges.
        api_instance.post_current_changes(current_change)
    except ApiException as e:
        print("Exception when calling CurrentChangeApi->post_current_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **current_change** | [**CurrentChange**](CurrentChange.md)| A CurrentChange or list of CurrentChange documents | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | operation has been successful |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_current_change_item**
> put_current_change_item(currentchange_id, current_change, if_match=if_match)

Replaces a CurrentChange document

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts_staging
from xepmts_staging.rest import ApiException
from pprint import pprint
configuration = xepmts_staging.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api.xepmts.yossisprojects.com/v1
configuration.host = "https://api.xepmts.yossisprojects.com/v1"

# Enter a context with an instance of the API client
with xepmts_staging.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts_staging.CurrentChangeApi(api_client)
    currentchange_id = 'currentchange_id_example' # str | 
current_change = xepmts_staging.CurrentChange() # CurrentChange | A CurrentChange or list of CurrentChange documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a CurrentChange document
        api_instance.put_current_change_item(currentchange_id, current_change, if_match=if_match)
    except ApiException as e:
        print("Exception when calling CurrentChangeApi->put_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currentchange_id** | **str**|  | 
 **current_change** | [**CurrentChange**](CurrentChange.md)| A CurrentChange or list of CurrentChange documents | 
 **if_match** | **str**| Current value of the _etag field | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CurrentChange document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

