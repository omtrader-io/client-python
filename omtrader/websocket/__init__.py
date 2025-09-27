"""
OMTrader WebSocket API

This module provides access to the OMTrader WebSocket API functionality.
"""

from .client import WebSocketClient
from .models import (
    WebSocketMessage,
    EventMessageType,
    OrderMessage,
    PositionMessage,
    DealMessage,
    MarketDataMessage,
    MarketDataTick,
    ProfitUpdate,
    InfoMessage,
    ErrorMessage,
    SessionLogoutMessage,
    WebSocketConnectionState,
    ConnectionInfo
)

__all__ = [
    "WebSocketClient",
    "WebSocketMessage",
    "EventMessageType",
    "OrderMessage",
    "PositionMessage",
    "DealMessage",
    "MarketDataMessage",
    "MarketDataTick",
    "ProfitUpdate",
    "InfoMessage",
    "ErrorMessage",
    "SessionLogoutMessage",
    "WebSocketConnectionState",
    "ConnectionInfo"
]
