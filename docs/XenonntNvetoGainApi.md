# xepmts_staging.XenonntNvetoGainApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_xenonnt_nveto_gains**](XenonntNvetoGainApi.md#get_xenonnt_nveto_gains) | **GET** /gains/xenonnt/nveto | Retrieves one or more XenonntNvetoGains


# **get_xenonnt_nveto_gains**
> InlineResponse20037 get_xenonnt_nveto_gains(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more XenonntNvetoGains

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
    api_instance = xepmts_staging.XenonntNvetoGainApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more XenonntNvetoGains
        api_response = api_instance.get_xenonnt_nveto_gains(where=where, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling XenonntNvetoGainApi->get_xenonnt_nveto_gains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of XenonntNvetoGains |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

