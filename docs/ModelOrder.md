# ModelOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**ModelTradeAccount**](ModelTradeAccount.md) |  | [optional] 
**account_id** | **int** |  | [optional] 
**comment** | **str** |  | [optional] 
**contract_size** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **int** |  | [optional] 
**dealer_id** | **int** |  | [optional] 
**digits** | **int** | configured digits to use for this positions | [optional] 
**digits_currency** | **int** | currency digits | [optional] 
**exit_level** | [**ModelExitLevel**](ModelExitLevel.md) | when to exit overide S/L | [optional] 
**exit_loos** | **float** | exit loos value for the position | [optional] 
**exit_profit** | **float** | exit profit value for the position | [optional] 
**expiration_policy** | [**ModelExpirationPolicy**](ModelExpirationPolicy.md) |  | [optional] 
**external_id** | **str** | id of position on LP | [optional] 
**id** | **int** |  | [optional] 
**position** | [**ModelPosition**](ModelPosition.md) |  | [optional] 
**position_by** | [**ModelPosition**](ModelPosition.md) |  | [optional] 
**position_by_id** | **int** |  | [optional] 
**position_id** | **int** |  | [optional] 
**price_current** | **float** |  | [optional] 
**price_order** | **float** |  | [optional] 
**price_sl** | **float** |  | [optional] 
**price_tp** | **float** |  | [optional] 
**price_trigger** | **float** |  | [optional] 
**rate_margin** | **float** |  | [optional] 
**reason** | [**ModelReasonType**](ModelReasonType.md) |  | [optional] 
**side** | [**ModelSideType**](ModelSideType.md) |  | [optional] 
**status** | [**ModelOrderStatus**](ModelOrderStatus.md) |  | [optional] 
**symbol** | [**ModelSymbol**](ModelSymbol.md) |  | [optional] 
**symbol_id** | **int** | symbol id | [optional] 
**time_done** | **str** |  | [optional] 
**time_expiration** | **str** |  | [optional] 
**time_setup** | **str** |  | [optional] 
**type** | [**ModelOrderType**](ModelOrderType.md) |  | [optional] 
**type_fill** | [**ModelFillPolicy**](ModelFillPolicy.md) |  | [optional] 
**type_time** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **int** |  | [optional] 
**volume_current** | **float** |  | [optional] 
**volume_current_ext** | **float** |  | [optional] 
**volume_initial** | **float** |  | [optional] 
**volume_initial_ext** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.model_order import ModelOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ModelOrder from a JSON string
model_order_instance = ModelOrder.from_json(json)
# print the JSON string representation of the object
print(ModelOrder.to_json())

# convert the object into a dict
model_order_dict = model_order_instance.to_dict()
# create an instance of ModelOrder from a dict
model_order_from_dict = ModelOrder.from_dict(model_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


