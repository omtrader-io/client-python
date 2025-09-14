# ModelTradeAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | **float** |  | [optional] 
**balance** | **float** |  | [optional] 
**blocked_commission** | **float** |  | [optional] 
**blocked_profit** | **float** |  | [optional] 
**client_id** | **int** |  | [optional] 
**credit** | **float** |  | [optional] 
**currency** | **str** | currency of the account | [optional] 
**currency_digits** | **int** |  | [optional] 
**day_profit** | **float** |  | [optional] 
**deals** | [**List[ModelDeal]**](ModelDeal.md) |  | [optional] 
**enable_risk_management** | **bool** | These fields overide positions S/L works global for account level P/L Control flow for day then week then month in case defined in current unit | [optional] 
**equity** | **float** |  | [optional] 
**floating** | **float** |  | [optional] 
**group_id** | **int** | this trade account if part of a group | [optional] 
**id** | **int** |  | [optional] 
**leverage** | **int** | 1:x where X &#x3D; 5000 down to 1 use group level if ZERP | [optional] 
**liabilities** | **float** |  | [optional] 
**liqudation_status** | [**ModelLiqudationStatus**](ModelLiqudationStatus.md) | liquidation status | [optional] 
**margin** | **float** |  | [optional] 
**margin_free** | **float** |  | [optional] 
**margin_initial** | **float** |  | [optional] 
**margin_level** | **float** |  | [optional] 
**margin_leverage** | **float** |  | [optional] 
**margin_maintenance** | **float** |  | [optional] 
**max_day_loss** | **float** |  | [optional] 
**max_day_profit** | **float** |  | [optional] 
**max_month_loss** | **float** |  | [optional] 
**max_month_profit** | **float** |  | [optional] 
**max_week_loss** | **float** |  | [optional] 
**max_week_profit** | **float** |  | [optional] 
**month_profit** | **float** |  | [optional] 
**orders** | [**List[ModelOrder]**](ModelOrder.md) |  | [optional] 
**positions** | [**List[ModelPosition]**](ModelPosition.md) |  | [optional] 
**profit** | **float** |  | [optional] 
**storage** | **float** |  | [optional] 
**trade_type** | [**ModelTradeType**](ModelTradeType.md) | account trading properties | [optional] 
**user** | [**ModelUser**](ModelUser.md) |  | [optional] 
**user_id** | **int** |  | [optional] 
**week_profit** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.model_trade_account import ModelTradeAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ModelTradeAccount from a JSON string
model_trade_account_instance = ModelTradeAccount.from_json(json)
# print the JSON string representation of the object
print(ModelTradeAccount.to_json())

# convert the object into a dict
model_trade_account_dict = model_trade_account_instance.to_dict()
# create an instance of ModelTradeAccount from a dict
model_trade_account_from_dict = ModelTradeAccount.from_dict(model_trade_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


