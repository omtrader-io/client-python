# MessagingCancelOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**id** | **int** |  | 
**user_id** | **int** |  | 

## Example

```python
from openapi_client.models.messaging_cancel_order import MessagingCancelOrder

# TODO update the JSON string below
json = "{}"
# create an instance of MessagingCancelOrder from a JSON string
messaging_cancel_order_instance = MessagingCancelOrder.from_json(json)
# print the JSON string representation of the object
print(MessagingCancelOrder.to_json())

# convert the object into a dict
messaging_cancel_order_dict = messaging_cancel_order_instance.to_dict()
# create an instance of MessagingCancelOrder from a dict
messaging_cancel_order_from_dict = MessagingCancelOrder.from_dict(messaging_cancel_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


