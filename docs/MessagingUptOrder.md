# MessagingUptOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**comment** | **str** |  | [optional] 
**expiration_police** | [**ModelExpirationPolicy**](ModelExpirationPolicy.md) |  | [optional] 
**id** | **int** |  | 
**order_price** | **float** |  | 
**price_sl** | **float** |  | [optional] 
**price_tp** | **float** |  | [optional] 
**time_expiration** | **str** |  | [optional] 
**type** | [**ModelOrderType**](ModelOrderType.md) |  | [optional] 
**user_id** | **int** |  | 
**volume** | **float** |  | 

## Example

```python
from openapi_client.models.messaging_upt_order import MessagingUptOrder

# TODO update the JSON string below
json = "{}"
# create an instance of MessagingUptOrder from a JSON string
messaging_upt_order_instance = MessagingUptOrder.from_json(json)
# print the JSON string representation of the object
print(MessagingUptOrder.to_json())

# convert the object into a dict
messaging_upt_order_dict = messaging_upt_order_instance.to_dict()
# create an instance of MessagingUptOrder from a dict
messaging_upt_order_from_dict = MessagingUptOrder.from_dict(messaging_upt_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


