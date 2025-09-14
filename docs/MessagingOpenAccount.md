# MessagingOpenAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**balance** | **int** |  | 
**email** | **str** |  | [optional] 
**family_name** | **str** |  | [optional] 
**first_name** | **str** |  | 
**investor_password** | **str** |  | 
**middle_name** | **str** |  | [optional] 
**user_password** | **str** |  | 
**username** | **str** |  | 

## Example

```python
from openapi_client.models.messaging_open_account import MessagingOpenAccount

# TODO update the JSON string below
json = "{}"
# create an instance of MessagingOpenAccount from a JSON string
messaging_open_account_instance = MessagingOpenAccount.from_json(json)
# print the JSON string representation of the object
print(MessagingOpenAccount.to_json())

# convert the object into a dict
messaging_open_account_dict = messaging_open_account_instance.to_dict()
# create an instance of MessagingOpenAccount from a dict
messaging_open_account_from_dict = MessagingOpenAccount.from_dict(messaging_open_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


