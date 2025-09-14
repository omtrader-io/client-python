# ModelGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compensate_negative_balance** | **bool** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**currency_digits** | **int** |  | [optional] 
**default_leverage** | **int** | Rules or Permissions | [optional] 
**desc** | **str** | Common | 
**full_stop_out** | **bool** |  | [optional] 
**group_type** | [**ModelGroupType**](ModelGroupType.md) | 0-client group 1-admin group | [optional] 
**groups** | [**List[ModelGroup]**](ModelGroup.md) | Models | [optional] 
**id** | **int** |  | [optional] 
**limit_history** | **int** |  | [optional] 
**limit_orders** | **int** |  | [optional] 
**limit_positions** | **int** |  | [optional] 
**limit_positions_volume** | **int** |  | [optional] 
**limit_symbols** | **int** |  | [optional] 
**margin_call** | **float** |  | [optional] 
**margin_mode** | [**ModelMarginMode**](ModelMarginMode.md) | Margin | [optional] 
**margin_stop_out** | **float** |  | [optional] 
**parent_id** | **int** | parent group if not root otherwise zero | [optional] 
**root** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**trade_accounts** | [**List[ModelTradeAccount]**](ModelTradeAccount.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.model_group import ModelGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ModelGroup from a JSON string
model_group_instance = ModelGroup.from_json(json)
# print the JSON string representation of the object
print(ModelGroup.to_json())

# convert the object into a dict
model_group_dict = model_group_instance.to_dict()
# create an instance of ModelGroup from a dict
model_group_from_dict = ModelGroup.from_dict(model_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


