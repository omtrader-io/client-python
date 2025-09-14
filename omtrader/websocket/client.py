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
    OrderUpdateMessage,
    PositionUpdateMessage,
    MarketDataMessage,
    ErrorMessage
)

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
            host = os.environ.get("OMTRADER_WS_HOST", "ws://api.omtrader.io")
        
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