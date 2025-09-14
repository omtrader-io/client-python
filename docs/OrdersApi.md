# openapi_client.OrdersApi

All URIs are relative to *http://api.omtrader.io/swagger/v1/trader*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approval_trader_order**](OrdersApi.md#approval_trader_order) | **POST** /api/v1/trader/orders/{id}/approval | 
[**cancel_trader_order**](OrdersApi.md#cancel_trader_order) | **DELETE** /api/v1/trader/orders/{id} | 
[**create_trader_order**](OrdersApi.md#create_trader_order) | **POST** /api/v1/trader/orders | 
[**get_trader_order**](OrdersApi.md#get_trader_order) | **GET** /api/v1/trader/orders/{id} | 
[**get_trader_orders**](OrdersApi.md#get_trader_orders) | **GET** /api/v1/trader/orders | 
[**get_trader_orders_history**](OrdersApi.md#get_trader_orders_history) | **GET** /api/v1/trader/orders/history | 
[**update_trader_order**](OrdersApi.md#update_trader_order) | **PUT** /api/v1/trader/orders/{id} | 


# **approval_trader_order**
> str approval_trader_order(id, body)

Approval Trader Order

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.messaging_trader_order_approval import MessagingTraderOrderApproval
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
    api_instance = openapi_client.OrdersApi(api_client)
    id = 56 # int | Order ID
    body = openapi_client.MessagingTraderOrderApproval() # MessagingTraderOrderApproval | Order

    try:
        api_response = api_instance.approval_trader_order(id, body)
        print("The response of OrdersApi->approval_trader_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->approval_trader_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **body** | [**MessagingTraderOrderApproval**](MessagingTraderOrderApproval.md)| Order | 

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

# **cancel_trader_order**
> str cancel_trader_order(id, body)

Cancel Trader Order

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.messaging_cancel_order import MessagingCancelOrder
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
    api_instance = openapi_client.OrdersApi(api_client)
    id = 56 # int | Order ID
    body = openapi_client.MessagingCancelOrder() # MessagingCancelOrder | Order

    try:
        api_response = api_instance.cancel_trader_order(id, body)
        print("The response of OrdersApi->cancel_trader_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->cancel_trader_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **body** | [**MessagingCancelOrder**](MessagingCancelOrder.md)| Order | 

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

# **create_trader_order**
> str create_trader_order(body)

Create Trader Order

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.messaging_crt_order import MessagingCrtOrder
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
    api_instance = openapi_client.OrdersApi(api_client)
    body = openapi_client.MessagingCrtOrder() # MessagingCrtOrder | Order

    try:
        api_response = api_instance.create_trader_order(body)
        print("The response of OrdersApi->create_trader_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->create_trader_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessagingCrtOrder**](MessagingCrtOrder.md)| Order | 

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
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_trader_order**
> ModelOrder get_trader_order(id)

Get Tader Order

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.model_order import ModelOrder
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
    api_instance = openapi_client.OrdersApi(api_client)
    id = 56 # int | Order ID

    try:
        api_response = api_instance.get_trader_order(id)
        print("The response of OrdersApi->get_trader_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_trader_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 

### Return type

[**ModelOrder**](ModelOrder.md)

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

# **get_trader_orders**
> List[ModelOrder] get_trader_orders()

Get Orders

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.model_order import ModelOrder
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
    api_instance = openapi_client.OrdersApi(api_client)

    try:
        api_response = api_instance.get_trader_orders()
        print("The response of OrdersApi->get_trader_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_trader_orders: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ModelOrder]**](ModelOrder.md)

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

# **get_trader_orders_history**
> List[ModelOrder] get_trader_orders_history()

Get Orders History

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.model_order import ModelOrder
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
    api_instance = openapi_client.OrdersApi(api_client)

    try:
        api_response = api_instance.get_trader_orders_history()
        print("The response of OrdersApi->get_trader_orders_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_trader_orders_history: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ModelOrder]**](ModelOrder.md)

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

# **update_trader_order**
> str update_trader_order(id, body)

Update Trader Order

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.messaging_upt_order import MessagingUptOrder
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
    api_instance = openapi_client.OrdersApi(api_client)
    id = 56 # int | Order ID
    body = openapi_client.MessagingUptOrder() # MessagingUptOrder | Order

    try:
        api_response = api_instance.update_trader_order(id, body)
        print("The response of OrdersApi->update_trader_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->update_trader_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | 
 **body** | [**MessagingUptOrder**](MessagingUptOrder.md)| Order | 

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

