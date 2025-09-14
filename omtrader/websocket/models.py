"""
WebSocket Models

Data models and message types for WebSocket communication.
"""

from typing import Any, Dict, List, Optional, Union
from enum import Enum
from dataclasses import dataclass
from datetime import datetime


class EventMessageType(str, Enum):
    """WebSocket message types for different events."""
    
    # System Messages
    INFO = "info"
    ERROR = "error" 
    PING = "ping"
    PONG = "pong"
    
    # Session Management
    SESSION_LOGOUT = "session_logout"
    
    # Market Data Subscription
    MARKET_SUBSCRIBE_SYMBOL = "market_subscribe_symbol"
    MARKET_UNSUBSCRIBE_SYMBOL = "market_unsubscribe_symbol"
    
    # Account Management
    START_ACCOUNT_ALL = "start_account_all"
    STOP_ACCOUNT_ALL = "stop_account_all"
    
    # Order Events
    ORDERS_PLACE = "orders_place"
    ORDERS_UPDATE = "orders_update"
    ORDERS_CANCEL = "orders_cancel"
    ORDERS_EXPIRED = "orders_expired"
    ORDERS_REJECTED = "orders_rejected"
    ORDERS_REQUOTED = "dealing_order_requote"
    
    # Position Events
    POSITIONS_OPEN = "positions_open"
    POSITIONS_UPDATE = "positions_update"
    POSITIONS_CLOSE = "positions_close"


@dataclass
class WebSocketMessage:
    """Base WebSocket message structure."""
    
    type: str
    data: Optional[Dict[str, Any]] = None
    timestamp: Optional[datetime] = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()


@dataclass
class OrderUpdateMessage(WebSocketMessage):
    """Order update WebSocket message."""
    
    order_id: Optional[str] = None
    symbol: Optional[str] = None
    status: Optional[str] = None
    volume: Optional[float] = None
    price: Optional[float] = None


@dataclass
class PositionUpdateMessage(WebSocketMessage):
    """Position update WebSocket message."""
    
    position_id: Optional[str] = None
    symbol: Optional[str] = None
    status: Optional[str] = None
    volume: Optional[float] = None
    current_price: Optional[float] = None
    profit: Optional[float] = None


@dataclass
class MarketDataMessage(WebSocketMessage):
    """Market data WebSocket message."""
    
    symbol: Optional[str] = None
    bid: Optional[float] = None
    ask: Optional[float] = None
    timestamp: Optional[datetime] = None


@dataclass
class ErrorMessage(WebSocketMessage):
    """Error WebSocket message."""
    
    error_code: Optional[str] = None
    error_message: Optional[str] = None
    details: Optional[Dict[str, Any]] = None


class WebSocketConnectionState(str, Enum):
    """WebSocket connection states."""
    
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    RECONNECTING = "reconnecting"
    FAILED = "failed"


@dataclass
class ConnectionInfo:
    """WebSocket connection information."""
    
    state: WebSocketConnectionState
    url: str
    session_id: Optional[str] = None
    access_token: Optional[str] = None
    last_ping: Optional[datetime] = None
    last_pong: Optional[datetime] = None
    reconnect_attempts: int = 0
    max_reconnect_attempts: int = 5
