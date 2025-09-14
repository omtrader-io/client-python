# MessagingUptPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** |  | 
**comment** | **str** |  | [optional] 
**id** | **int** |  | 
**price_sl** | **float** |  | [optional] 
**price_tp** | **float** |  | [optional] 
**user_id** | **int** |  | 

## Example

```python
from openapi_client.models.messaging_upt_position import MessagingUptPosition

# TODO update the JSON string below
json = "{}"
# create an instance of MessagingUptPosition from a JSON string
messaging_upt_position_instance = MessagingUptPosition.from_json(json)
# print the JSON string representation of the object
print(MessagingUptPosition.to_json())

# convert the object into a dict
messaging_upt_position_dict = messaging_upt_position_instance.to_dict()
# create an instance of MessagingUptPosition from a dict
messaging_upt_position_from_dict = MessagingUptPosition.from_dict(messaging_upt_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


