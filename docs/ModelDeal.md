# ModelDeal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | [**ModelTradeAccount**](ModelTradeAccount.md) |  | [optional] 
**account_id** | **int** |  | [optional] 
**action** | **int** |  | [optional] 
**channel** | [**ModelChannelType**](ModelChannelType.md) |  | [optional] 
**closed_volume** | **float** | lot which closed partially so we need to get closing_order_ids from the table | [optional] 
**comment** | **str** |  | [optional] 
**commission** | **float** |  | [optional] 
**contract_size** | **float** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **int** |  | [optional] 
**dealer_id** | **int** |  | [optional] 
**digits** | **int** |  | [optional] 
**digits_currency** | **int** |  | [optional] 
**direction** | [**ModelDirectionType**](ModelDirectionType.md) |  | [optional] 
**entry** | **int** |  | [optional] 
**external_id** | **str** | id of position on LP | [optional] 
**external_volume** | **float** | volume of position on LP | [optional] 
**external_volume_closed** | **float** | volume of position on LP | [optional] 
**fee** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**market_ask** | **float** |  | [optional] 
**market_bid** | **float** |  | [optional] 
**market_last** | **float** |  | [optional] 
**order_id** | **int** | which order this deal belong to | [optional] 
**position_id** | **int** | which position deal belong to | [optional] 
**price** | **float** | price of deal | [optional] 
**price_position** | **float** | price of position on LP | [optional] 
**price_sl** | **float** | price of stop loss | [optional] 
**price_tp** | **float** | price of take profit | [optional] 
**profit** | **float** |  | [optional] 
**profit_raw** | **float** |  | [optional] 
**reason** | [**ModelReasonType**](ModelReasonType.md) |  | [optional] 
**side** | [**ModelSideType**](ModelSideType.md) |  | [optional] 
**storage** | **float** |  | [optional] 
**swap** | **float** | swap for this deal from symbol swap | [optional] 
**symbol** | [**ModelSymbol**](ModelSymbol.md) |  | [optional] 
**symbol_id** | **int** |  | [optional] 
**tick_size** | **float** |  | [optional] 
**tick_value** | **float** | tick value of symbol | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **int** |  | [optional] 
**volume** | **float** | total lot | [optional] 

## Example

```python
from openapi_client.models.model_deal import ModelDeal

# TODO update the JSON string below
json = "{}"
# create an instance of ModelDeal from a JSON string
model_deal_instance = ModelDeal.from_json(json)
# print the JSON string representation of the object
print(ModelDeal.to_json())

# convert the object into a dict
model_deal_dict = model_deal_instance.to_dict()
# create an instance of ModelDeal from a dict
model_deal_from_dict = ModelDeal.from_dict(model_deal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


