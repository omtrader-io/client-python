# HttpHttpResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Http status Code | [optional] 
**data** | **object** | if the request were successful the data will be saved here | [optional] 
**error** | **str** | Generic General Error Message defined in the system | [optional] 
**message** | **str** | More detailed error message indicates why the request was unsuccessful | [optional] 
**success** | **bool** | Response flag indicates whether the HTTP request was successful or not | [optional] 

## Example

```python
from openapi_client.models.http_http_response import HttpHttpResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HttpHttpResponse from a JSON string
http_http_response_instance = HttpHttpResponse.from_json(json)
# print the JSON string representation of the object
print(HttpHttpResponse.to_json())

# convert the object into a dict
http_http_response_dict = http_http_response_instance.to_dict()
# create an instance of HttpHttpResponse from a dict
http_http_response_from_dict = HttpHttpResponse.from_dict(http_http_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


