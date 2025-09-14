# openapi_client.SymbolsApi

All URIs are relative to *http://api.omtrader.io/swagger/v1/trader*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trader_symbol**](SymbolsApi.md#get_trader_symbol) | **GET** /api/v1/trader/symbols/{id} | 
[**get_trader_symbol_ticks_history**](SymbolsApi.md#get_trader_symbol_ticks_history) | **GET** /api/v1/trader/symbols/ticks/history/{id} | 
[**get_trader_symbols**](SymbolsApi.md#get_trader_symbols) | **GET** /api/v1/trader/symbols | 


# **get_trader_symbol**
> MessagingViewSymbol get_trader_symbol(id)

Get Trader Symbol

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.messaging_view_symbol import MessagingViewSymbol
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
    api_instance = openapi_client.SymbolsApi(api_client)
    id = 56 # int | Symbol ID

    try:
        api_response = api_instance.get_trader_symbol(id)
        print("The response of SymbolsApi->get_trader_symbol:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SymbolsApi->get_trader_symbol: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Symbol ID | 

### Return type

[**MessagingViewSymbol**](MessagingViewSymbol.md)

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

# **get_trader_symbol_ticks_history**
> List[MessagingHistoryTick] get_trader_symbol_ticks_history(id, symbol_id, var_from, to, resolution, count_back, type=type)

Get Trader Market Ticks History

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.messaging_history_tick import MessagingHistoryTick
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
    api_instance = openapi_client.SymbolsApi(api_client)
    id = 56 # int | Symbol ID
    symbol_id = 56 # int | Symbol ID
    var_from = 56 # int | From Timestamp
    to = 56 # int | To Timestamp
    resolution = 'resolution_example' # str | Resolution (Xm, Xh, Xd, Xw, Xmo)
    count_back = 56 # int | Count Back
    type = 'type_example' # str | Type (bid or ask) (optional)

    try:
        api_response = api_instance.get_trader_symbol_ticks_history(id, symbol_id, var_from, to, resolution, count_back, type=type)
        print("The response of SymbolsApi->get_trader_symbol_ticks_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SymbolsApi->get_trader_symbol_ticks_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Symbol ID | 
 **symbol_id** | **int**| Symbol ID | 
 **var_from** | **int**| From Timestamp | 
 **to** | **int**| To Timestamp | 
 **resolution** | **str**| Resolution (Xm, Xh, Xd, Xw, Xmo) | 
 **count_back** | **int**| Count Back | 
 **type** | **str**| Type (bid or ask) | [optional] 

### Return type

[**List[MessagingHistoryTick]**](MessagingHistoryTick.md)

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

# **get_trader_symbols**
> List[MessagingViewSymbol] get_trader_symbols()

Get Trader Symbols

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.messaging_view_symbol import MessagingViewSymbol
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
    api_instance = openapi_client.SymbolsApi(api_client)

    try:
        api_response = api_instance.get_trader_symbols()
        print("The response of SymbolsApi->get_trader_symbols:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SymbolsApi->get_trader_symbols: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MessagingViewSymbol]**](MessagingViewSymbol.md)

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

