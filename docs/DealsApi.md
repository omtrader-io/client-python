# openapi_client.DealsApi

All URIs are relative to *http://api.omtrader.io/swagger/v1/trader*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trader_deal**](DealsApi.md#get_trader_deal) | **GET** /api/v1/trader/deals/{id} | 
[**get_trader_deals**](DealsApi.md#get_trader_deals) | **GET** /api/v1/trader/deals | 


# **get_trader_deal**
> ModelDeal get_trader_deal(id)

Get Trader Deal

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.model_deal import ModelDeal
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.omtrader.io/swagger/v1/trader
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.omtrader.io/swagger/v1/trader"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DealsApi(api_client)
    id = 56 # int | Deal ID

    try:
        api_response = api_instance.get_trader_deal(id)
        print("The response of DealsApi->get_trader_deal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealsApi->get_trader_deal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Deal ID | 

### Return type

[**ModelDeal**](ModelDeal.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trader_deals**
> List[ModelDeal] get_trader_deals(page=page, limit=limit, var_from=var_from, to=to, sort_by=sort_by, dir=dir)

Get Trader Deals

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.model_deal import ModelDeal
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.omtrader.io/swagger/v1/trader
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.omtrader.io/swagger/v1/trader"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: BearerAuth
configuration.api_key['BearerAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['BearerAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DealsApi(api_client)
    page = 56 # int | page number (optional)
    limit = 56 # int | limit number (optional)
    var_from = 'var_from_example' # str | from date (optional)
    to = 'to_example' # str | to date (optional)
    sort_by = 'sort_by_example' # str | sort by (optional)
    dir = 'dir_example' # str | direction (optional)

    try:
        api_response = api_instance.get_trader_deals(page=page, limit=limit, var_from=var_from, to=to, sort_by=sort_by, dir=dir)
        print("The response of DealsApi->get_trader_deals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DealsApi->get_trader_deals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| page number | [optional] 
 **limit** | **int**| limit number | [optional] 
 **var_from** | **str**| from date | [optional] 
 **to** | **str**| to date | [optional] 
 **sort_by** | **str**| sort by | [optional] 
 **dir** | **str**| direction | [optional] 

### Return type

[**List[ModelDeal]**](ModelDeal.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

