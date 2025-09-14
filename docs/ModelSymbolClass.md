# ModelSymbolClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**desc** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**parent_id** | **int** |  | [optional] 
**symbol_classes** | [**List[ModelSymbolClass]**](ModelSymbolClass.md) |  | [optional] 
**symbols** | [**List[ModelSymbol]**](ModelSymbol.md) |  | [optional] 

## Example

```python
from openapi_client.models.model_symbol_class import ModelSymbolClass

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSymbolClass from a JSON string
model_symbol_class_instance = ModelSymbolClass.from_json(json)
# print the JSON string representation of the object
print(ModelSymbolClass.to_json())

# convert the object into a dict
model_symbol_class_dict = model_symbol_class_instance.to_dict()
# create an instance of ModelSymbolClass from a dict
model_symbol_class_from_dict = ModelSymbolClass.from_dict(model_symbol_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


