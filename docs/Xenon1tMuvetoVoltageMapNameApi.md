# xepmts_staging.Xenon1tMuvetoVoltageMapNameApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_xenon1t_muveto_voltage_map_names**](Xenon1tMuvetoVoltageMapNameApi.md#get_xenon1t_muveto_voltage_map_names) | **GET** /voltage_maps/names/xenon1t/muveto | Retrieves one or more Xenon1tMuvetoVoltageMapNames


# **get_xenon1t_muveto_voltage_map_names**
> InlineResponse20069 get_xenon1t_muveto_voltage_map_names(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more Xenon1tMuvetoVoltageMapNames

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
    api_instance = xepmts_staging.Xenon1tMuvetoVoltageMapNameApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more Xenon1tMuvetoVoltageMapNames
        api_response = api_instance.get_xenon1t_muveto_voltage_map_names(where=where, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling Xenon1tMuvetoVoltageMapNameApi->get_xenon1t_muveto_voltage_map_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse20069**](InlineResponse20069.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of Xenon1tMuvetoVoltageMapNames |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

