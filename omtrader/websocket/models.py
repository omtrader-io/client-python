"""
WebSocket Models

Data models and message types for WebSocket communication.
"""

from typing import Any, Dict, List, Optional, Union
from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from pydantic import BaseModel

from omtrader.rest.models.model_order import ModelOrder
from omtrader.rest.models.model_position import ModelPosition
from omtrader.rest.models.model_deal import ModelDeal
from omtrader.rest.models.model_symbol import ModelSymbol
from omtrader.rest.models.model_trade_account import ModelTradeAccount


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
    MARKET_FEED = "market_feed"  # For binary market data
    
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
    
    # Deal Events
    DEALS_CREATE = "deals_create"
    DEALS_UPDATE = "deals_update"
    


class WebSocketMessage(BaseModel):
    """Base WebSocket message structure."""
    
    type: str
    data: Any = None  # Can be dict, int, str, etc.
    timestamp: Optional[datetime] = None
    
    def __init__(self, **data):
        super().__init__(**data)
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()


class MarketDataTick(BaseModel):
    """Market data tick structure for binary messages."""
    
    symbol_id: int
    bid: float
    ask: float
    last: float
    volume: float
    high: float
    low: float


class ProfitUpdate(BaseModel):
    """Profit update structure for binary messages.
    Format: s,position_id,profit,total_profit
    """
    position_id: int
    profit: float
    total_profit: float


class OrderMessage(WebSocketMessage):
    """Order event message structure."""
    
    type: EventMessageType
    data: ModelOrder


class PositionMessage(WebSocketMessage):
    """Position event message structure."""
    
    type: EventMessageType
    data: ModelPosition


class DealMessage(WebSocketMessage):
    """Deal event message structure."""
    
    type: EventMessageType
    data: ModelDeal




class MarketDataMessage(WebSocketMessage):
    """Market data message structure."""
    
    type: EventMessageType = EventMessageType.MARKET_FEED
    data: MarketDataTick


class InfoMessage(WebSocketMessage):
    """Info message structure."""
    
    type: EventMessageType = EventMessageType.INFO
    data: Dict[str, str]  # {"message": "info message"}


class ErrorMessage(WebSocketMessage):
    """Error message structure."""
    
    type: EventMessageType = EventMessageType.ERROR
    data: Dict[str, str]  # {"message": "error message"}


class SessionLogoutMessage(WebSocketMessage):
    """Session logout message structure."""
    
    type: EventMessageType = EventMessageType.SESSION_LOGOUT
    data: Dict[str, str]  # {"session_id": "session_id"}


class WebSocketConnectionState(str, Enum):
    """WebSocket connection states."""
    
    DISCONNECTED = "disconnected"
    CONNECTING = "connecting"
    CONNECTED = "connected"
    RECONNECTING = "reconnecting"
    FAILED = "failed"


class ConnectionInfo(BaseModel):
    """WebSocket connection information."""
    
    state: WebSocketConnectionState
    url: str
    session_id: Optional[str] = None
    access_token: Optional[str] = None
    last_ping: Optional[datetime] = None
    last_pong: Optional[datetime] = None
    reconnect_attempts: int = 0
    max_reconnect_attempts: int = 5
