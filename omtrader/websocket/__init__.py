"""
OMTrader WebSocket API

This module provides access to the OMTrader WebSocket API functionality.
"""

from .client import WebSocketClient
from .models import (
    WebSocketMessage,
    EventMessageType,
    OrderUpdateMessage,
    PositionUpdateMessage,
    MarketDataMessage,
    ErrorMessage,
    WebSocketConnectionState,
    ConnectionInfo
)

__all__ = [
    "WebSocketClient",
    "WebSocketMessage",
    "EventMessageType",
    "OrderUpdateMessage",
    "PositionUpdateMessage", 
    "MarketDataMessage",
    "ErrorMessage",
    "WebSocketConnectionState",
    "ConnectionInfo"
]
