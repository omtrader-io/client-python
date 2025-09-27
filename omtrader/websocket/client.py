"""
OMTrader WebSocket Client

WebSocket client for real-time communication with OMTrader API.
"""

import json
import logging
import threading
import time
import os
from typing import Optional, Dict, Any, Callable, List
from datetime import datetime
import websocket
import requests

from .models import (
    EventMessageType,
    WebSocketMessage,
    WebSocketConnectionState,
    ConnectionInfo,
    OrderMessage,
    PositionMessage,
    DealMessage,
    MarketDataMessage,
    MarketDataTick,
    ProfitUpdate,
    InfoMessage,
    ErrorMessage,
    SessionLogoutMessage
)

from omtrader.rest.models.model_order import ModelOrder
from omtrader.rest.models.model_position import ModelPosition
from omtrader.rest.models.model_deal import ModelDeal

logger = logging.getLogger(__name__)

class WebSocketClient:
    """
    WebSocket client for OMTrader real-time data.
    
    This client provides real-time access to order updates, position changes,
    market data, and other trading events.
    
    Example:
        ```python
        from omtrader import WebSocketClient
        from omtrader.websocket.models import EventMessageType
        
        def handle_order_update(data):
            print(f"Order update: {data}")
        
        # Initialize client
        ws = WebSocketClient(api_key="your_api_key")
        
        # Subscribe to order updates
        ws.subscribe(EventMessageType.ORDERS_UPDATE, handle_order_update)
        
        # Connect and start receiving data
        ws.run()
        ```
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        host: Optional[str] = None,
        trace: bool = False,
        auto_reconnect: bool = True,
        max_reconnect_attempts: int = 5
    ):
        """
        Initialize WebSocket client.
        
        Args:
            api_key: Your OMTrader API key. If not provided, will look for OMTRADER_API_KEY env var
            host: WebSocket host URL. Defaults to production if not provided
            trace: Enable request/response tracing
            auto_reconnect: Enable automatic reconnection
            max_reconnect_attempts: Maximum number of reconnection attempts
        """
        # Get API key from parameter or environment
        self.api_key = api_key or os.environ.get("OMTRADER_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key is required. Provide it as a parameter or set OMTRADER_API_KEY environment variable."
            )
        
        # Set default host if not provided
        if not host:
            host = os.environ.get("OMTRADER_HOST", "https://api.omtrader.io")
            
        # Convert http(s):// to ws(s):// if needed
        if host.startswith('https://'):
            host = 'wss://' + host.split('://', 1)[1]
        elif host.startswith('http://'):
            host = 'ws://' + host.split('://', 1)[1]
        
        self.host = host
        self.trace = trace
        self.auto_reconnect = auto_reconnect
        
        # Connection state
        self.connection_info = ConnectionInfo(
            state=WebSocketConnectionState.DISCONNECTED,
            url="",
            max_reconnect_attempts=max_reconnect_attempts
        )
        
        # WebSocket and threading
        self.ws: Optional[websocket.WebSocketApp] = None
        self.event_queue: List[WebSocketMessage] = []
        self.callbacks: Dict[EventMessageType, List[Callable]] = {}
        self._heartbeat_thread: Optional[threading.Thread] = None
        self._ws_thread: Optional[threading.Thread] = None
        
        # Authentication
        self._access_token: Optional[str] = None
        self._session_id: Optional[str] = None

    def _login(self) -> None:
        """Login to get access token and session ID."""
        # Convert ws(s):// back to http(s):// for REST API calls
        login_url = self.host
        if login_url.startswith('wss://'):
            login_url = 'https://' + login_url.split('://', 1)[1]
        elif login_url.startswith('ws://'):
            login_url = 'http://' + login_url.split('://', 1)[1]
        login_url = f"{login_url}/api/v1/oauth2/login"
        print(login_url)
        params = {
            'remember_me': 'false',
            'grant_type': 'api_key'
        }
        
        headers = {
            'API-Key': self.api_key,
            'Accept': 'application/json'
        }
        
        if self.trace:
            logger.info(f"Authenticating with OMTrader API at {login_url}")
        
        try:
            response = requests.post(
                login_url, 
                params=params, 
                headers=headers, 
                allow_redirects=True,
                timeout=30.0
            )
            
            if response.status_code == 200:
                token_data = response.json()
                if token_data.get('success') and token_data.get('data'):
                    data = token_data['data']
                    self._access_token = data.get('access_token')
                    self._session_id = data.get('session_id')
                    
                    if not self._access_token or not self._session_id:
                        raise Exception("Login successful but missing access_token or session_id")
                        
                    if self.trace:
                        logger.info(f"Authentication successful")
                        logger.info(f"Access token: {self._access_token[:10]}...")
                        logger.info(f"Session ID: {self._session_id}")
                else:
                    raise Exception("Login successful but no data in response")
            else:
                raise Exception(f"OAuth2 login failed: {response.status_code} - {response.text}")
                
        except requests.RequestException as e:
            raise Exception(f"Failed to authenticate: {e}")
            
    def _validate_session(self) -> None:
        """Validate session before WebSocket connection."""
        if not self._session_id:
            raise ValueError("No session ID available")
            
        # Convert ws(s):// back to http(s):// for REST API calls
        validate_url = self.host
        if validate_url.startswith('wss://'):
            validate_url = 'https://' + validate_url.split('://', 1)[1]
        elif validate_url.startswith('ws://'):
            validate_url = 'http://' + validate_url.split('://', 1)[1]
        validate_url = f"{validate_url}/ws/v1/{self._session_id}"
        
        try:
            response = requests.post(validate_url, timeout=30.0)
            if response.status_code != 200:
                if response.status_code == 400 and "session is already used" in response.text:
                    raise Exception("Session is already in use in another tab")
                raise Exception(f"Session validation failed: {response.status_code} - {response.text}")
                
            if self.trace:
                logger.info("Session validated successfully")
                
        except requests.RequestException as e:
            raise Exception(f"Failed to validate session: {e}")

    def connect(self) -> None:
        """Establish WebSocket connection"""
        # First login to get access token and session ID
        if not self._access_token or not self._session_id:
            self._login()
            
        # Validate session
        self._validate_session()
        
        # Build WebSocket URL
        self._connect_url = f"{self.host}/ws/v1?session_id={self._session_id}&access_token={self._access_token}"
        
        # Create WebSocket connection
        self.ws = websocket.WebSocketApp(
            self._connect_url,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close
        )
        
        if self.trace:
            logger.info(f"Connecting to WebSocket at {self._connect_url}")
        
        ws_thread = threading.Thread(target=self.ws.run_forever)
        ws_thread.daemon = True
        ws_thread.start()

    def _start_heartbeat(self) -> None:
        """Start heartbeat thread"""
        def send_heartbeat():
            while self.connected:
                try:
                    self.ws.send("9")  # Heartbeat ping
                    time.sleep(10)  # 10 second interval
                except:
                    break
                    
        self._heartbeat_thread = threading.Thread(target=send_heartbeat)
        self._heartbeat_thread.daemon = True
        self._heartbeat_thread.start()

    def _on_open(self, ws) -> None:
        """Handle WebSocket connection open"""
        logger.info("WebSocket connection established")
        self.connected = True
        self._start_heartbeat()
        self._process_event_queue()

    def _decode_binary_message(self, binary_data: bytes) -> Optional[str]:
        """
        Decode binary message to text.
        All binary messages are UTF-8 encoded strings.
        """
        try:
            return binary_data.decode('utf-8')
        except Exception as e:
            logger.error(f"Failed to decode binary message: {e}")
            return None

    def _parse_market_data(self, text: str) -> Optional[MarketDataTick]:
        """
        Parse market data message.
        Format: symbolId,bid,ask,last,volume,high,low
        """
        try:
            parts = text.split(',')
            if len(parts) >= 7:
                return MarketDataTick(
                    symbol_id=int(parts[0]),
                    bid=float(parts[1]),
                    ask=float(parts[2]),
                    last=float(parts[3]),
                    volume=float(parts[4]),
                    high=float(parts[5]),
                    low=float(parts[6])
                )
            return None
        except Exception as e:
            logger.error(f"Failed to parse market data: {e}")
            return None

    def _parse_profit_update(self, text: str) -> Optional[ProfitUpdate]:
        """
        Parse profit update message.
        Format: s,position_id,profit,total_profit
        """
        try:
            parts = text.split(',')
            if len(parts) >= 4:
                return ProfitUpdate(
                    position_id=int(parts[1]),
                    profit=float(parts[2]),
                    total_profit=float(parts[3])
                )
            return None
        except Exception as e:
            logger.error(f"Failed to parse profit update: {e}")
            return None

    def _on_message(self, ws, message: str | bytes) -> None:
        """Handle incoming WebSocket messages"""
        # Handle heartbeat response
        if message == "10":
            return
            
        try:
            # Handle binary messages
            if isinstance(message, bytes):
                # First decode binary to text
                text = self._decode_binary_message(message)
                if not text:
                    return
                
                # Then check message type and parse accordingly
                if text.startswith('s,'):
                    # Profit update message
                    data = self._parse_profit_update(text)
                    if data and EventMessageType.POSITIONS_UPDATE in self.callbacks:
                        for callback in self.callbacks[EventMessageType.POSITIONS_UPDATE]:
                            callback(data)
                else:
                    # Market data message
                    data = self._parse_market_data(text)
                    if data and EventMessageType.MARKET_FEED in self.callbacks:
                        msg = MarketDataMessage(type=EventMessageType.MARKET_FEED, data=data)
                        for callback in self.callbacks[EventMessageType.MARKET_FEED]:
                            callback(msg)
                return
                
            # Parse JSON message
            data = json.loads(message)
            msg_type = data.get("type")
            msg_data = data.get("data")
            
            if not msg_type or msg_type not in EventMessageType.__members__.values():
                logger.error(f"Invalid message type: {msg_type}")
                return
                
            # Create appropriate message object based on type
            if msg_type == EventMessageType.ORDERS_PLACE:
                msg = OrderMessage(type=msg_type, data=ModelOrder.from_dict(msg_data))
            elif msg_type == EventMessageType.ORDERS_UPDATE:
                msg = OrderMessage(type=msg_type, data=ModelOrder.from_dict(msg_data))
            elif msg_type == EventMessageType.ORDERS_CANCEL:
                msg = OrderMessage(type=msg_type, data=ModelOrder.from_dict(msg_data))
            elif msg_type == EventMessageType.ORDERS_EXPIRED:
                msg = OrderMessage(type=msg_type, data=ModelOrder.from_dict(msg_data))
            elif msg_type == EventMessageType.ORDERS_REJECTED:
                msg = OrderMessage(type=msg_type, data=ModelOrder.from_dict(msg_data))
            elif msg_type == EventMessageType.ORDERS_REQUOTED:
                msg = OrderMessage(type=msg_type, data=ModelOrder.from_dict(msg_data))
            elif msg_type == EventMessageType.POSITIONS_OPEN:
                msg = PositionMessage(type=msg_type, data=ModelPosition.from_dict(msg_data))
            elif msg_type == EventMessageType.POSITIONS_UPDATE:
                msg = PositionMessage(type=msg_type, data=ModelPosition.from_dict(msg_data))
            elif msg_type == EventMessageType.POSITIONS_CLOSE:
                msg = PositionMessage(type=msg_type, data=ModelPosition.from_dict(msg_data))
            elif msg_type == EventMessageType.DEALS_CREATE:
                msg = DealMessage(type=msg_type, data=ModelDeal.from_dict(msg_data))
            elif msg_type == EventMessageType.DEALS_UPDATE:
                msg = DealMessage(type=msg_type, data=ModelDeal.from_dict(msg_data))
            elif msg_type == EventMessageType.INFO:
                msg = InfoMessage(type=msg_type, data=msg_data)
            elif msg_type == EventMessageType.ERROR:
                msg = ErrorMessage(type=msg_type, data=msg_data)
            elif msg_type == EventMessageType.SESSION_LOGOUT:
                msg = SessionLogoutMessage(type=msg_type, data=msg_data)
            else:
                msg = WebSocketMessage(type=msg_type, data=msg_data)
            
            # Call registered callbacks
            if msg_type in self.callbacks:
                for callback in self.callbacks[msg_type]:
                    callback(msg)
                    
        except json.JSONDecodeError:
            logger.error(f"Failed to parse message: {message}")
        except Exception as e:
            logger.error(f"Error processing message: {e}")

    def _on_error(self, ws, error: str) -> None:
        """Handle WebSocket errors"""
        logger.error(f"WebSocket error: {error}")
        self.reconnect_required = True

    def _on_close(self, ws, close_status_code: int, close_msg: str) -> None:
        """Handle WebSocket connection close"""
        logger.info(f"WebSocket closed: {close_status_code} - {close_msg}")
        self.connected = False
        if self.reconnect_required:
            self.connect()

    def send(self, message: WebSocketMessage) -> None:
        """
        Send WebSocket message.
        
        Args:
            message: A WebSocketMessage instance or subclass
        """
        if not self.connected:
            self.event_queue.append(message)
            return
            
        try:
            # Convert message to dict and send
            msg_dict = {
                "type": message.type,
                "data": message.data.to_dict() if hasattr(message.data, "to_dict") else message.data
            }
            self.ws.send(json.dumps(msg_dict))
        except Exception as e:
            logger.error(f"Error sending message: {e}")
            self.event_queue.append(message)
            
    def send_market_subscribe(self, symbol_id: int) -> None:
        """
        Subscribe to market data for a symbol.
        
        Args:
            symbol_id: The ID of the symbol to subscribe to
        """
        # According to docs, just send the symbol ID as data
        msg = WebSocketMessage(
            type=EventMessageType.MARKET_SUBSCRIBE_SYMBOL,
            data=symbol_id  # Not a dict, just the ID
        )
        self.send(msg)
        
    def send_market_unsubscribe(self, symbol_id: int) -> None:
        """
        Unsubscribe from market data for a symbol.
        
        Args:
            symbol_id: The ID of the symbol to unsubscribe from
        """
        # According to docs, just send the symbol ID as data
        msg = WebSocketMessage(
            type=EventMessageType.MARKET_UNSUBSCRIBE_SYMBOL,
            data=symbol_id  # Not a dict, just the ID
        )
        self.send(msg)
        
    def start_account_updates(self) -> None:
        """Start receiving account-wide updates."""
        msg = WebSocketMessage(
            type=EventMessageType.START_ACCOUNT_ALL,
            data=None
        )
        self.send(msg)
        
    def stop_account_updates(self) -> None:
        """Stop receiving account-wide updates."""
        msg = WebSocketMessage(
            type=EventMessageType.STOP_ACCOUNT_ALL,
            data=None
        )
        self.send(msg)

    def _process_event_queue(self) -> None:
        """Process queued events after reconnection"""
        while self.event_queue:
            message = self.event_queue.pop(0)
            try:
                self.send(message)  # Use our send method which handles message conversion
            except Exception as e:
                logger.error(f"Error sending queued message: {e}")
                self.event_queue.insert(0, message)
                break

    def subscribe(self, event_type: EventMessageType, callback: Callable) -> None:
        """Subscribe to event type with callback"""
        if event_type not in self.callbacks:
            self.callbacks[event_type] = []
        self.callbacks[event_type].append(callback)

    def unsubscribe(self, event_type: EventMessageType, callback: Callable) -> None:
        """Unsubscribe callback from event type"""
        if event_type in self.callbacks:
            self.callbacks[event_type].remove(callback)

    def close(self) -> None:
        """Close WebSocket connection"""
        if self.ws:
            self.reconnect_required = False
            self.ws.close()