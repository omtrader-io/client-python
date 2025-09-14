# ModelRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**created_by** | **int** |  | [optional] 
**desc** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**original** | **bool** | Default system Roles (can&#39;t be changed) or deleted | [optional] 
**role_type** | [**ModelRoleType**](ModelRoleType.md) |  | [optional] 
**status** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_by** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.model_role import ModelRole

# TODO update the JSON string below
json = "{}"
# create an instance of ModelRole from a JSON string
model_role_instance = ModelRole.from_json(json)
# print the JSON string representation of the object
print(ModelRole.to_json())

# convert the object into a dict
model_role_dict = model_role_instance.to_dict()
# create an instance of ModelRole from a dict
model_role_from_dict = ModelRole.from_dict(model_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


