# Error Handling Documentation

## Table of Contents
- [Overview](#overview)
- [Error Response Structure](#error-response-structure)
- [Common Error Scenarios](#common-error-scenarios)
- [Error Handling Examples](#error-handling-examples)

## Overview
[↑ Back to Table of Contents](#table-of-contents)

All API errors in the OMTrader client are handled through:
1. The `ApiException` class which wraps all API errors
2. The `HttpHttpResponse` object which contains detailed error information

When an API call fails, it will:
1. Return an `HttpHttpResponse` with error details
2. Wrap it in an `ApiException`
3. Include the HTTP status code and error message

## Error Response Structure
[↑ Back to Table of Contents](#table-of-contents)

The `HttpHttpResponse` object contains:

| Field | Type | Description |
|-------|------|-------------|
| code | int | HTTP status code (e.g., 400, 401, 403, 500) |
| success | bool | Always false for errors |
| error | str | Generic error message (e.g., "Unauthorized", "Invalid Input") |
| message | str | Detailed error message explaining what went wrong |
| data | Dict/List/str | Optional additional error data |

Common status codes:
- 400: Bad Request - Invalid input or validation error
- 401: Unauthorized - Invalid or missing API key
- 403: Forbidden - Insufficient permissions
- 404: Not Found - Resource doesn't exist
- 500: Server Error - Internal server error

## Common Error Scenarios
[↑ Back to Table of Contents](#table-of-contents)

### Authentication Errors
```python
try:
    client = RESTClient(api_key="invalid_key")
    account = client.get_account()
except ApiException as e:
    # e.response will be HttpHttpResponse with:
    # code = 401
    # error = "Unauthorized"
    # message = "Invalid API key"
```

### Validation Errors
```python
try:
    client.create_order({
        "volume": -1  # Invalid volume
    })
except ApiException as e:
    # e.response will be HttpHttpResponse with:
    # code = 400
    # error = "Invalid Input"
    # message = "Volume must be positive"
```

### Resource Not Found
```python
try:
    client.get_order("non_existent_id")
except ApiException as e:
    # e.response will be HttpHttpResponse with:
    # code = 404
    # error = "Not Found"
    # message = "Order not found"
```

## Error Handling Examples
[↑ Back to Table of Contents](#table-of-contents)

### Basic Error Handling
```python
from omtrader import RESTClient
from omtrader.rest import ApiException

client = RESTClient(api_key="your_api_key")

try:
    order = client.create_order(order_data)
except ApiException as e:
    print(f"API Error: {e.response.code} - {e.response.message}")
    if e.response.code == 400:
        print("Validation error - check your input")
    elif e.response.code == 401:
        print("Authentication error - check your API key")
```

### Detailed Error Information
```python
try:
    position = client.get_position("123")
except ApiException as e:
    print(f"Status Code: {e.response.code}")
    print(f"Error Type: {e.response.error}")
    print(f"Error Message: {e.response.message}")
    if e.response.data:
        print(f"Additional Data: {e.response.data}")
```

### Handling Multiple Error Types
```python
try:
    result = client.create_order(order_data)
except ApiException as e:
    if e.response.code == 400:
        # Handle validation errors
        print(f"Invalid input: {e.response.message}")
    elif e.response.code == 401:
        # Handle authentication errors
        print("Please check your API key")
    elif e.response.code == 403:
        # Handle permission errors
        print("Insufficient permissions")
    elif e.response.code == 500:
        # Handle server errors
        print("Server error - please try again later")
    else:
        # Handle other errors
        print(f"Unexpected error: {e.response.message}")
```

### With Debug Logging
```python
client = RESTClient(api_key="your_api_key", trace=True)

try:
    result = client.update_position("123", position_data)
except ApiException as e:
    # With trace=True, error details will be logged automatically
    # You can still handle the error as needed
    if e.response.success is False:
        print(f"Operation failed: {e.response.message}")
```
