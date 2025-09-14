# openapi_client.PositionsApi

All URIs are relative to *http://api.omtrader.io/swagger/v1/trader*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_trader_position**](PositionsApi.md#close_trader_position) | **POST** /api/v1/trader/positions/{id} | 
[**get_trader_position**](PositionsApi.md#get_trader_position) | **GET** /api/v1/trader/positions/{id} | 
[**get_trader_positions**](PositionsApi.md#get_trader_positions) | **GET** /api/v1/trader/positions | 
[**get_trader_positions_history**](PositionsApi.md#get_trader_positions_history) | **GET** /api/v1/trader/positions/history | 
[**update_trader_position**](PositionsApi.md#update_trader_position) | **PUT** /api/v1/trader/positions/{id} | 


# **close_trader_position**
> str close_trader_position(id, body)

Close Trader Position

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.messaging_close_position import MessagingClosePosition
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
    api_instance = openapi_client.PositionsApi(api_client)
    id = 56 # int | Position ID
    body = openapi_client.MessagingClosePosition() # MessagingClosePosition | Position

    try:
        api_response = api_instance.close_trader_position(id, body)
        print("The response of PositionsApi->close_trader_position:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PositionsApi->close_trader_position: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Position ID | 
 **body** | [**MessagingClosePosition**](MessagingClosePosition.md)| Position | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trader_position**
> ModelPosition get_trader_position(id)

Get Trader Position

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.model_position import ModelPosition
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
    api_instance = openapi_client.PositionsApi(api_client)
    id = 56 # int | Position ID

    try:
        api_response = api_instance.get_trader_position(id)
        print("The response of PositionsApi->get_trader_position:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PositionsApi->get_trader_position: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Position ID | 

### Return type

[**ModelPosition**](ModelPosition.md)

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

# **get_trader_positions**
> List[ModelPosition] get_trader_positions()

Get Trader Positions

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.model_position import ModelPosition
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
    api_instance = openapi_client.PositionsApi(api_client)

    try:
        api_response = api_instance.get_trader_positions()
        print("The response of PositionsApi->get_trader_positions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PositionsApi->get_trader_positions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ModelPosition]**](ModelPosition.md)

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

# **get_trader_positions_history**
> List[ModelPosition] get_trader_positions_history()

Get Trader Positions History

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.model_position import ModelPosition
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
    api_instance = openapi_client.PositionsApi(api_client)

    try:
        api_response = api_instance.get_trader_positions_history()
        print("The response of PositionsApi->get_trader_positions_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PositionsApi->get_trader_positions_history: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ModelPosition]**](ModelPosition.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_trader_position**
> str update_trader_position(id, body)

Update Trader Position

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.messaging_upt_position import MessagingUptPosition
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
    api_instance = openapi_client.PositionsApi(api_client)
    id = 56 # int | Position ID
    body = openapi_client.MessagingUptPosition() # MessagingUptPosition | Position

    try:
        api_response = api_instance.update_trader_position(id, body)
        print("The response of PositionsApi->update_trader_position:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PositionsApi->update_trader_position: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Position ID | 
 **body** | [**MessagingUptPosition**](MessagingUptPosition.md)| Position | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

