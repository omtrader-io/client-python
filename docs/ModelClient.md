# ModelClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**List[ModelTradeAccount]**](ModelTradeAccount.md) |  | [optional] 
**address** | **str** |  | [optional] 
**annual_deposit** | **float** |  | [optional] 
**annual_income** | **float** |  | [optional] 
**approval_date** | **str** |  | [optional] 
**approved_by** | **int** |  | [optional] 
**birth_date** | **str** |  | [optional] 
**cfd_experience** | [**ModelTradingExperience**](ModelTradingExperience.md) |  | [optional] 
**city** | **str** |  | [optional] 
**close_date** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**created_by** | **int** |  | [optional] 
**document_number** | **str** |  | [optional] 
**document_type** | [**ModelDocumentType**](ModelDocumentType.md) | Address Properties | [optional] 
**education_level** | [**ModelEducationLevel**](ModelEducationLevel.md) |  | [optional] 
**email** | **str** |  | [optional] 
**employment_industry** | [**ModelEmploymentIndustry**](ModelEmploymentIndustry.md) |  | [optional] 
**employment_status** | [**ModelEmploymentStatus**](ModelEmploymentStatus.md) |  | [optional] 
**expiry_date** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**family_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**forex_experience** | [**ModelTradingExperience**](ModelTradingExperience.md) |  | [optional] 
**futures_experience** | [**ModelTradingExperience**](ModelTradingExperience.md) |  | [optional] 
**gender** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**introducer** | **str** |  | [optional] 
**issue_date** | **str** |  | [optional] 
**kyc_status** | [**ModelKycStatus**](ModelKycStatus.md) |  | [optional] 
**language** | **str** |  | [optional] 
**last_contact_date** | **str** |  | [optional] 
**lead_campaign** | **str** |  | [optional] 
**lead_source** | **str** |  | [optional] 
**local_number** | **str** |  | [optional] 
**manager_id** | **int** |  | [optional] 
**messengers** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**national** | **str** | Regulation | [optional] 
**net_worth** | **float** |  | [optional] 
**preferred_group** | **int** |  | [optional] 
**preferred_method** | [**ModelClientPreferredMethod**](ModelClientPreferredMethod.md) |  | [optional] 
**social_networks** | **str** |  | [optional] 
**source_of_wealth** | [**ModelSourceOfWealth**](ModelSourceOfWealth.md) |  | [optional] 
**state** | **str** |  | [optional] 
**status** | [**ModelClientStatus**](ModelClientStatus.md) |  | [optional] 
**stocks_experience** | [**ModelTradingExperience**](ModelTradingExperience.md) |  | [optional] 
**tax_id** | **str** |  | [optional] 
**title** | **str** | Personal Properties | [optional] 
**type** | [**ModelClientType**](ModelClientType.md) | Client properties | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**zip_code** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.model_client import ModelClient

# TODO update the JSON string below
json = "{}"
# create an instance of ModelClient from a JSON string
model_client_instance = ModelClient.from_json(json)
# print the JSON string representation of the object
print(ModelClient.to_json())

# convert the object into a dict
model_client_dict = model_client_instance.to_dict()
# create an instance of ModelClient from a dict
model_client_from_dict = ModelClient.from_dict(model_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


