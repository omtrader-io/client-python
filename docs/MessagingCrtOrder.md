# MessagingCrtOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**comment** | **str** |  | [optional] 
**expiration_police** | [**ModelExpirationPolicy**](ModelExpirationPolicy.md) |  | [optional] 
**order_price** | **float** |  | 
**price_sl** | **float** |  | [optional] 
**price_tp** | **float** |  | [optional] 
**side** | [**ModelSideType**](ModelSideType.md) |  | [optional] 
**symbol_id** | **int** |  | 
**time_expiration** | **str** |  | [optional] 
**type** | [**ModelOrderType**](ModelOrderType.md) |  | [optional] 
**user_id** | **int** |  | 
**volume** | **float** |  | 

## Example

```python
from openapi_client.models.messaging_crt_order import MessagingCrtOrder

# TODO update the JSON string below
json = "{}"
# create an instance of MessagingCrtOrder from a JSON string
messaging_crt_order_instance = MessagingCrtOrder.from_json(json)
# print the JSON string representation of the object
print(MessagingCrtOrder.to_json())

# convert the object into a dict
messaging_crt_order_dict = messaging_crt_order_instance.to_dict()
# create an instance of MessagingCrtOrder from a dict
messaging_crt_order_from_dict = MessagingCrtOrder.from_dict(messaging_crt_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


