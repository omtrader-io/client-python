# MessagingTraderOrderApproval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**approved** | **bool** |  | [optional] 
**id** | **int** |  | 
**user_id** | **int** |  | 

## Example

```python
from openapi_client.models.messaging_trader_order_approval import MessagingTraderOrderApproval

# TODO update the JSON string below
json = "{}"
# create an instance of MessagingTraderOrderApproval from a JSON string
messaging_trader_order_approval_instance = MessagingTraderOrderApproval.from_json(json)
# print the JSON string representation of the object
print(MessagingTraderOrderApproval.to_json())

# convert the object into a dict
messaging_trader_order_approval_dict = messaging_trader_order_approval_instance.to_dict()
# create an instance of MessagingTraderOrderApproval from a dict
messaging_trader_order_approval_from_dict = MessagingTraderOrderApproval.from_dict(messaging_trader_order_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


