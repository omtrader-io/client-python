# openapi_client.AccountsApi

All URIs are relative to *http://api.omtrader.io/swagger/v1/trader*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trader_account**](AccountsApi.md#get_trader_account) | **GET** /api/v1/trader/account | 
[**open_trader_account**](AccountsApi.md#open_trader_account) | **POST** /api/v1/trader/account | 


# **get_trader_account**
> ModelTradeAccount get_trader_account()

Get Trader Account

### Example

* Api Key Authentication (BearerAuth):

```python
import openapi_client
from openapi_client.models.model_trade_account import ModelTradeAccount
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
    api_instance = openapi_client.AccountsApi(api_client)

    try:
        api_response = api_instance.get_trader_account()
        print("The response of AccountsApi->get_trader_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_trader_account: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ModelTradeAccount**](ModelTradeAccount.md)

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

# **open_trader_account**
> ModelTradeAccount open_trader_account(body)

Open Trader Account

### Example


```python
import openapi_client
from openapi_client.models.messaging_open_account import MessagingOpenAccount
from openapi_client.models.model_trade_account import ModelTradeAccount
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.omtrader.io/swagger/v1/trader
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.omtrader.io/swagger/v1/trader"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AccountsApi(api_client)
    body = openapi_client.MessagingOpenAccount() # MessagingOpenAccount | Account

    try:
        api_response = api_instance.open_trader_account(body)
        print("The response of AccountsApi->open_trader_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->open_trader_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessagingOpenAccount**](MessagingOpenAccount.md)| Account | 

### Return type

[**ModelTradeAccount**](ModelTradeAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

