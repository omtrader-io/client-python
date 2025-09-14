"""
OMTrader Python SDK

The official Python client library for the OMTrader REST and WebSocket APIs.

Example usage:
    ```python
    from omtrader import RESTClient, WebSocketClient
    
    # REST API
    rest_client = RESTClient(api_key="your_api_key")
    account = rest_client.get_account()
    
    # WebSocket API (future)
    ws_client = WebSocketClient(api_key="your_api_key")
    ws_client.connect()
    ```
"""

__version__ = "1.0.0"

# Import main clients
from .rest import RESTClient
from .websocket import WebSocketClient

# Import commonly used models and exceptions
from .rest import (
    ApiException,
    ApiTypeError,
    ApiValueError,
    ApiKeyError,
    ApiAttributeError,
    OpenApiException
)

from .websocket import (
    WebSocketMessage,
    EventMessageType,
    WebSocketConnectionState
)

# Define package exports
__all__ = [
    # Main clients
    "RESTClient",
    "WebSocketClient",
    
    # REST exceptions
    "ApiException",
    "ApiTypeError",
    "ApiValueError", 
    "ApiKeyError",
    "ApiAttributeError",
    "OpenApiException",
    
    # WebSocket models
    "WebSocketMessage",
    "EventMessageType",
    "WebSocketConnectionState",
    
    # Version
    "__version__"
]
