# xepmts_staging.VoltageChangeApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_voltage_change_item**](VoltageChangeApi.md#delete_voltage_change_item) | **DELETE** /voltage_changes/{voltagechangeId} | Deletes a VoltageChange document
[**get_voltage_change_item**](VoltageChangeApi.md#get_voltage_change_item) | **GET** /voltage_changes/{voltagechangeId} | Retrieves a VoltageChange document
[**get_voltage_changes**](VoltageChangeApi.md#get_voltage_changes) | **GET** /voltage_changes | Retrieves one or more VoltageChanges
[**post_voltage_changes**](VoltageChangeApi.md#post_voltage_changes) | **POST** /voltage_changes | Stores one or more VoltageChanges.
[**put_voltage_change_item**](VoltageChangeApi.md#put_voltage_change_item) | **PUT** /voltage_changes/{voltagechangeId} | Replaces a VoltageChange document


# **delete_voltage_change_item**
> delete_voltage_change_item(voltagechange_id, if_match=if_match)

Deletes a VoltageChange document

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
    api_instance = xepmts_staging.VoltageChangeApi(api_client)
    voltagechange_id = 'voltagechange_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a VoltageChange document
        api_instance.delete_voltage_change_item(voltagechange_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling VoltageChangeApi->delete_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voltagechange_id** | **str**|  | 
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
**204** | VoltageChange document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voltage_change_item**
> VoltageChange get_voltage_change_item(voltagechange_id)

Retrieves a VoltageChange document

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
    api_instance = xepmts_staging.VoltageChangeApi(api_client)
    voltagechange_id = 'voltagechange_id_example' # str | 

    try:
        # Retrieves a VoltageChange document
        api_response = api_instance.get_voltage_change_item(voltagechange_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VoltageChangeApi->get_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voltagechange_id** | **str**|  | 

### Return type

[**VoltageChange**](VoltageChange.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | VoltageChange document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voltage_changes**
> InlineResponse2005 get_voltage_changes(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more VoltageChanges

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
    api_instance = xepmts_staging.VoltageChangeApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more VoltageChanges
        api_response = api_instance.get_voltage_changes(where=where, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VoltageChangeApi->get_voltage_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of VoltageChanges |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_voltage_changes**
> post_voltage_changes(voltage_change)

Stores one or more VoltageChanges.

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
    api_instance = xepmts_staging.VoltageChangeApi(api_client)
    voltage_change = xepmts_staging.VoltageChange() # VoltageChange | A VoltageChange or list of VoltageChange documents

    try:
        # Stores one or more VoltageChanges.
        api_instance.post_voltage_changes(voltage_change)
    except ApiException as e:
        print("Exception when calling VoltageChangeApi->post_voltage_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voltage_change** | [**VoltageChange**](VoltageChange.md)| A VoltageChange or list of VoltageChange documents | 

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

# **put_voltage_change_item**
> put_voltage_change_item(voltagechange_id, voltage_change, if_match=if_match)

Replaces a VoltageChange document

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
    api_instance = xepmts_staging.VoltageChangeApi(api_client)
    voltagechange_id = 'voltagechange_id_example' # str | 
voltage_change = xepmts_staging.VoltageChange() # VoltageChange | A VoltageChange or list of VoltageChange documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a VoltageChange document
        api_instance.put_voltage_change_item(voltagechange_id, voltage_change, if_match=if_match)
    except ApiException as e:
        print("Exception when calling VoltageChangeApi->put_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voltagechange_id** | **str**|  | 
 **voltage_change** | [**VoltageChange**](VoltageChange.md)| A VoltageChange or list of VoltageChange documents | 
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
**200** | VoltageChange document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

