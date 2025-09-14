# MessagingHistoryTick


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close** | **float** |  | [optional] 
**high** | **float** |  | [optional] 
**low** | **float** |  | [optional] 
**open** | **float** |  | [optional] 
**time** | **int** |  | [optional] 
**volume** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.messaging_history_tick import MessagingHistoryTick

# TODO update the JSON string below
json = "{}"
# create an instance of MessagingHistoryTick from a JSON string
messaging_history_tick_instance = MessagingHistoryTick.from_json(json)
# print the JSON string representation of the object
print(MessagingHistoryTick.to_json())

# convert the object into a dict
messaging_history_tick_dict = messaging_history_tick_instance.to_dict()
# create an instance of MessagingHistoryTick from a dict
messaging_history_tick_from_dict = MessagingHistoryTick.from_dict(messaging_history_tick_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


