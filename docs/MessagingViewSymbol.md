# MessagingViewSymbol


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_currency** | **str** |  | [optional] 
**broker_fee** | **float** |  | [optional] 
**buy_limit** | **float** |  | [optional] 
**buy_stop** | **float** |  | [optional] 
**buy_stop_limit** | **float** |  | [optional] 
**calculation** | [**ModelCalcType**](ModelCalcType.md) |  | [optional] 
**chart_mode** | **int** |  | [optional] 
**close** | **float** |  | [optional] 
**contract_size** | **float** |  | [optional] 
**desc** | **str** |  | [optional] 
**digits** | **int** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**execution** | [**ModelExecutionMode**](ModelExecutionMode.md) |  | [optional] 
**expiration** | **str** |  | [optional] 
**filling** | [**ModelFillPolicy**](ModelFillPolicy.md) |  | [optional] 
**gtc** | **int** |  | [optional] 
**high_ask** | **float** |  | [optional] 
**high_bid** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**isin** | **str** |  | [optional] 
**last_ask** | **float** |  | [optional] 
**last_bid** | **float** |  | [optional] 
**low_ask** | **float** |  | [optional] 
**low_bid** | **float** |  | [optional] 
**maintenance_buy_limit** | **float** |  | [optional] 
**maintenance_buy_stop** | **float** |  | [optional] 
**maintenance_buy_stop_limit** | **float** |  | [optional] 
**maintenance_margin_buy** | **float** |  | [optional] 
**maintenance_margin_sell** | **float** |  | [optional] 
**maintenance_sell_limit** | **float** |  | [optional] 
**maintenance_sell_stop** | **float** |  | [optional] 
**maintenance_sell_stop_limit** | **float** |  | [optional] 
**maker_fee** | **float** |  | [optional] 
**margin_buy** | **float** |  | [optional] 
**margin_flags** | **int** |  | [optional] 
**margin_initial** | **float** |  | [optional] 
**margin_maintenance** | **float** |  | [optional] 
**margin_sell** | **float** |  | [optional] 
**max_value** | **float** |  | [optional] 
**min_value** | **float** |  | [optional] 
**open** | **float** |  | [optional] 
**orders** | **str** |  | [optional] 
**quote_currency** | **str** |  | [optional] 
**quote_scale** | **float** |  | [optional] 
**quote_sessions** | **str** |  | [optional] 
**sell_limit** | **float** |  | [optional] 
**sell_stop** | **float** |  | [optional] 
**sell_stop_limit** | **float** |  | [optional] 
**spread** | **int** |  | [optional] 
**spread_balance** | **int** |  | [optional] 
**status** | [**ModelSymbolStatus**](ModelSymbolStatus.md) |  | [optional] 
**step** | **float** |  | [optional] 
**stop_level** | **int** |  | [optional] 
**swap_long** | **float** |  | [optional] 
**swap_short** | **float** |  | [optional] 
**swap_type** | [**ModelSwaptype**](ModelSwaptype.md) |  | [optional] 
**swaps_enabled** | **bool** |  | [optional] 
**symbol** | **str** |  | [optional] 
**symbol_class** | [**ModelSymbolClass**](ModelSymbolClass.md) |  | [optional] 
**symbol_scale** | **float** |  | [optional] 
**time_limit** | **str** |  | [optional] 
**trade_level** | [**ModelTradeLevel**](ModelTradeLevel.md) |  | [optional] 
**trade_sessions** | **str** |  | [optional] 
**ts** | **int** |  | [optional] 
**volume** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.messaging_view_symbol import MessagingViewSymbol

# TODO update the JSON string below
json = "{}"
# create an instance of MessagingViewSymbol from a JSON string
messaging_view_symbol_instance = MessagingViewSymbol.from_json(json)
# print the JSON string representation of the object
print(MessagingViewSymbol.to_json())

# convert the object into a dict
messaging_view_symbol_dict = messaging_view_symbol_instance.to_dict()
# create an instance of MessagingViewSymbol from a dict
messaging_view_symbol_from_dict = MessagingViewSymbol.from_dict(messaging_view_symbol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


