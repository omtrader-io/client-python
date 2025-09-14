# MessagingClosePosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**id** | **int** |  | 
**user_id** | **int** |  | 
**volume** | **float** |  | 

## Example

```python
from openapi_client.models.messaging_close_position import MessagingClosePosition

# TODO update the JSON string below
json = "{}"
# create an instance of MessagingClosePosition from a JSON string
messaging_close_position_instance = MessagingClosePosition.from_json(json)
# print the JSON string representation of the object
print(MessagingClosePosition.to_json())

# convert the object into a dict
messaging_close_position_dict = messaging_close_position_instance.to_dict()
# create an instance of MessagingClosePosition from a dict
messaging_close_position_from_dict = MessagingClosePosition.from_dict(messaging_close_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


