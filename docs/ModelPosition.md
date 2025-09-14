# ModelPosition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**ModelTradeAccount**](ModelTradeAccount.md) |  | [optional] 
**account_id** | **int** |  | [optional] 
**action** | **int** |  | [optional] 
**comment** | **str** | set by the trader | [optional] 
**commission** | **float** |  | [optional] 
**contract_size** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **int** |  | [optional] 
**dealer_id** | **int** |  | [optional] 
**deals** | [**ModelDeal**](ModelDeal.md) |  | [optional] 
**digits** | **int** | configured digits to use for this positions | [optional] 
**digits_currency** | **int** | currency digits | [optional] 
**exit_level** | [**ModelExitLevel**](ModelExitLevel.md) | when to exit overide S/L | [optional] 
**exit_loos** | **float** | exit loos value for the position | [optional] 
**exit_profit** | **float** | exit profit value for the position | [optional] 
**external_id** | **str** | id of position on LP | [optional] 
**id** | **int** |  | [optional] 
**price_current** | **float** |  | [optional] 
**price_open** | **float** |  | [optional] 
**price_sl** | **float** | stop loss | [optional] 
**price_tp** | **float** | take profit | [optional] 
**profit** | **float** |  | [optional] 
**rate_margin** | **float** |  | [optional] 
**rate_profit** | **float** |  | [optional] 
**reason** | [**ModelReasonType**](ModelReasonType.md) |  | [optional] 
**side** | [**ModelSideType**](ModelSideType.md) |  | [optional] 
**status** | [**ModelPositionStatus**](ModelPositionStatus.md) |  | [optional] 
**storage** | **float** |  | [optional] 
**swaps** | **float** | swap fees | [optional] 
**symbol** | [**ModelSymbol**](ModelSymbol.md) |  | [optional] 
**symbol_id** | **int** | symbol id | [optional] 
**total_profit** | **float** | total profit | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **int** |  | [optional] 
**volume_current** | **float** | no of lots | [optional] 
**volume_current_ext** | **float** |  | [optional] 
**volume_initial** | **float** | no of lots | [optional] 
**volume_initial_ext** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.model_position import ModelPosition

# TODO update the JSON string below
json = "{}"
# create an instance of ModelPosition from a JSON string
model_position_instance = ModelPosition.from_json(json)
# print the JSON string representation of the object
print(ModelPosition.to_json())

# convert the object into a dict
model_position_dict = model_position_instance.to_dict()
# create an instance of ModelPosition from a dict
model_position_from_dict = ModelPosition.from_dict(model_position_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


