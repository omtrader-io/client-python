# ModelDataSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ask_markup** | **int** |  | [optional] 
**bid_markup** | **int** |  | [optional] 
**digits** | **int** |  | [optional] 
**feeder** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**symbols** | [**List[ModelSymbol]**](ModelSymbol.md) |  | [optional] 

## Example

```python
from openapi_client.models.model_data_source import ModelDataSource

# TODO update the JSON string below
json = "{}"
# create an instance of ModelDataSource from a JSON string
model_data_source_instance = ModelDataSource.from_json(json)
# print the JSON string representation of the object
print(ModelDataSource.to_json())

# convert the object into a dict
model_data_source_dict = model_data_source_instance.to_dict()
# create an instance of ModelDataSource from a dict
model_data_source_from_dict = ModelDataSource.from_dict(model_data_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


