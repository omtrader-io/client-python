import json
import logging
import threading
import time
from typing import Optional, Dict, Any, Callable, List
from enum import Enum
import websocket

logger = logging.getLogger(__name__)

class EventMessageType(str, Enum):
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

class WebSocketClient:
    def __init__(self, url: str, session_id: str, access_token: str):
        """Initialize WebSocket client"""
        self.base_url = url
        self.session_id = session_id
        self.access_token = access_token
        self.ws: Optional[websocket.WebSocketApp] = None
        self.connected = False
        self.reconnect_required = False
        self.event_queue: List[Dict] = []
        self.callbacks: Dict[str, List[Callable]] = {}
        self._heartbeat_thread: Optional[threading.Thread] = None
        self._connect_url = f"{self.base_url}/ws/v1?session_id={session_id}&access_token={access_token}"

    def connect(self) -> None:
        """Establish WebSocket connection"""
        self.ws = websocket.WebSocketApp(
            self._connect_url,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close
        )
        
        ws_thread = threading.Thread(target=self.ws.run_forever)
        ws_thread.daemon = True
        ws_thread.start()

    def _start_heartbeat(self) -> None:
        """Start heartbeat thread"""
        def send_heartbeat():
            while self.connected:
                try:
                    self.ws.send("9")  # Heartbeat ping
                    time.sleep(30)  # 30 second interval
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

    def _on_message(self, ws, message: str) -> None:
        """Handle incoming WebSocket messages"""
        # Handle heartbeat response
        if message == "10":
            return
            
        try:
            if message.startswith("s,"):
                # Handle profit updates
                self._handle_profit_update(message)
                return
                
            # Parse JSON message
            data = json.loads(message)
            msg_type = data.get("type")
            
            if msg_type in self.callbacks:
                for callback in self.callbacks[msg_type]:
                    callback(data.get("data"))
                    
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

    def send(self, event_type: EventMessageType, data: Any = None) -> None:
        """Send WebSocket message"""
        message = {
            "type": event_type,
            "data": data
        }
        
        if not self.connected:
            self.event_queue.append(message)
            return
            
        try:
            self.ws.send(json.dumps(message))
        except Exception as e:
            logger.error(f"Error sending message: {e}")
            self.event_queue.append(message)

    def _process_event_queue(self) -> None:
        """Process queued events after reconnection"""
        while self.event_queue:
            message = self.event_queue.pop(0)
            try:
                self.ws.send(json.dumps(message))
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