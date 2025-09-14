# ModelSymbol


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_currency** | **str** | EUR | [optional] 
**buy_limit** | **float** |  | [optional] 
**buy_stop** | **float** |  | [optional] 
**buy_stop_limit** | **float** |  | [optional] 
**calculation** | [**ModelCalcType**](ModelCalcType.md) | Trades | [optional] 
**contract_size** | **float** | Contract size for this symbol max 100,000 | [optional] 
**conversion_currency** | **int** | pointing to another symbol | [optional] 
**conversion_type** | [**ModelConversionType**](ModelConversionType.md) | 0-Multiply 1-Divide | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **int** |  | [optional] 
**data_source** | [**ModelDataSource**](ModelDataSource.md) |  | [optional] 
**data_source_feeder** | **str** |  | [optional] 
**data_source_symbol** | **str** |  | [optional] 
**delay** | **int** | Delay | [optional] 
**desc** | **str** | description | [optional] 
**digits** | **int** | number of digits after the decimal point | [optional] 
**enabled** | **bool** | if the symbol is enabled or not by the broker | [optional] 
**execution** | [**ModelExecutionMode**](ModelExecutionMode.md) | Exectuion | [optional] 
**expiration** | **str** | 1-All 2- | [optional] 
**filling** | [**ModelFillPolicy**](ModelFillPolicy.md) | 0&#x3D;Fill or Kill 2 &#x3D; Immidate or Cancel ..others | [optional] 
**id** | **int** |  | [optional] 
**isin** | **str** | International Securities Identifying Number. | [optional] 
**larger_leg_enabled** | **bool** | larger leg enabled | [optional] 
**maintenance_buy_limit** | **float** |  | [optional] 
**maintenance_buy_stop** | **float** |  | [optional] 
**maintenance_buy_stop_limit** | **float** |  | [optional] 
**maintenance_margin_buy** | **float** | Maintence | [optional] 
**maintenance_margin_sell** | **float** | marging for future sell on this assest | [optional] 
**maintenance_sell_limit** | **float** |  | [optional] 
**maintenance_sell_stop** | **float** |  | [optional] 
**maintenance_sell_stop_limit** | **float** |  | [optional] 
**margin_buy** | **float** | Margin rates Initial | [optional] 
**margin_hedged** | **float** | margin hedged | [optional] 
**margin_initial** | **float** | Margins | [optional] 
**margin_maintenance** | **float** | margin maintence | [optional] 
**margin_sell** | **float** | marging for future sell on this assest | [optional] 
**max_loss_deviation** | **float** | max loss deviation | [optional] 
**max_profit_deviation** | **float** | max profit deviation | [optional] 
**max_time_deviation** | **float** | max time deviation | [optional] 
**max_value** | **float** | Max lot value &#x3D; 0.01 | [optional] 
**min_value** | **float** | Min lot value &#x3D; 0.01 | [optional] 
**orders** | **str** | 1-All 2- | [optional] 
**quote_currency** | **str** | USD  quote currency (OR futures contract currency) | [optional] 
**quote_sessions** | **str** | Sessions | [optional] 
**sell_limit** | **float** |  | [optional] 
**sell_stop** | **float** |  | [optional] 
**sell_stop_limit** | **float** |  | [optional] 
**spread** | **int** | 1- floating 2-value | [optional] 
**spread_balance** | **int** | spread balance | [optional] 
**status** | [**ModelSymbolStatus**](ModelSymbolStatus.md) | added by saif | [optional] 
**step** | **float** | lot step value &#x3D; 0.01 , increment of lots | [optional] 
**stop_level** | **int** |  | [optional] 
**swap_days** | **str** | swap days ex: \&quot;1,2,3,4,5,6,7\&quot; | [optional] 
**swap_days_year** | **int** | swap days per year ex: 360 | [optional] 
**swap_long** | **float** | swap for Buy positions. | [optional] 
**swap_short** | **float** | swap short charge of long swap | [optional] 
**swap_type** | [**ModelSwaptype**](ModelSwaptype.md) | swap type to calc | [optional] 
**swaps_enabled** | **bool** | swaps | [optional] 
**symbol** | **str** | Common | [optional] 
**symbol_class_id** | **int** |  | [optional] 
**symbol_map** | **str** | User defined symbol map | [optional] 
**tick_size** | **float** | tick size | [optional] 
**tick_value** | **float** | tick value | [optional] 
**time_limit** | **str** | time limit for the symbol startDate-endDate | [optional] 
**timeout** | **int** | timeout in seconds if it exceeded then the symbol status will be changed to disable | [optional] 
**trade_level** | [**ModelTradeLevel**](ModelTradeLevel.md) | 1&#x3D;Full Access 2&#x3D; Buy 3-Sell | [optional] 
**trade_sessions** | **str** | array [Day,Time]... | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.model_symbol import ModelSymbol

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSymbol from a JSON string
model_symbol_instance = ModelSymbol.from_json(json)
# print the JSON string representation of the object
print(ModelSymbol.to_json())

# convert the object into a dict
model_symbol_dict = model_symbol_instance.to_dict()
# create an instance of ModelSymbol from a dict
model_symbol_from_dict = ModelSymbol.from_dict(model_symbol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


