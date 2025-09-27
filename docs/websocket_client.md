# WebSocketClient Documentation

## Table of Contents
- [Initialization](#initialization)
  - [Parameters](#parameters)
- [Event Types](#event-types)
  - [Order Events](#order-events)
  - [Position Events](#position-events)
  - [Deal Events](#deal-events)
  - [Market Data Events](#market-data-events)
  - [Account Events](#account-events)
  - [System Events](#system-events)
- [Message Types](#message-types)
  - [OrderMessage](#ordermessage)
  - [PositionMessage](#positionmessage)
  - [DealMessage](#dealmessage)
  - [MarketDataMessage](#marketdatamessage)
  - [MarketDataTick](#marketdatatick)
  - [ProfitUpdate](#profitupdate)
  - [InfoMessage](#infomessage)
  - [ErrorMessage](#errormessage)
  - [SessionLogoutMessage](#sessionlogoutmessage)
- [Usage Examples](#usage-examples)
  - [Basic Connection and Event Handling](#basic-connection-and-event-handling)
  - [Market Data Subscription](#market-data-subscription)
  - [Account Updates](#account-updates)
  - [Sending Custom Messages](#sending-custom-messages)
  - [Closing Connection](#closing-connection)
- [Error Handling](#error-handling)
- [Debugging](#debugging)
- [Best Practices](#best-practices)
- [Notes](#notes)

The `WebSocketClient` provides real-time access to order updates, position changes, market data, and other trading events through WebSocket connection.

## Initialization
[↑ Back to Table of Contents](#table-of-contents)

```python
from omtrader import WebSocketClient
from omtrader.websocket.models import EventMessageType

# With API key directly
client = WebSocketClient(api_key="your_api_key")

# With environment variable
# export OMTRADER_API_KEY="your_api_key"
client = WebSocketClient()  # Uses env var
```

### Parameters

- `api_key` (str, optional): Your OMTrader API key. If not provided, will look for OMTRADER_API_KEY environment variable.
- `host` (str, optional): WebSocket host URL. If not provided, will look for OMTRADER_HOST environment variable and defaults to production endpoint if none are provided. Replaces http or https in host url with ws or wss.
- `trace` (bool): Enable request/response tracing. Defaults to False.
- `auto_reconnect` (bool): Enable automatic reconnection. Defaults to True.
- `max_reconnect_attempts` (int): Maximum number of reconnection attempts. Defaults to 5.

## Event Types
[↑ Back to Table of Contents](#table-of-contents)

The WebSocket client supports various event types through the `EventMessageType` enum:

### Order Events
- `ORDERS_PLACE`: Order placed
- `ORDERS_UPDATE`: Order updated
- `ORDERS_CANCEL`: Order cancelled
- `ORDERS_EXPIRED`: Order expired
- `ORDERS_REJECTED`: Order rejected
- `ORDERS_REQUOTED`: Order requoted

### Position Events
- `POSITIONS_OPEN`: Position opened
- `POSITIONS_UPDATE`: Position updated
- `POSITIONS_CLOSE`: Position closed

### Deal Events
- `DEALS_CREATE`: Deal created
- `DEALS_UPDATE`: Deal updated

### Market Data Events
- `MARKET_FEED`: Market data updates
- `MARKET_SUBSCRIBE_SYMBOL`: Subscribe to symbol
- `MARKET_UNSUBSCRIBE_SYMBOL`: Unsubscribe from symbol

### Account Events
- `START_ACCOUNT_ALL`: Start account updates
- `STOP_ACCOUNT_ALL`: Stop account updates

### System Events
- `INFO`: Information messages
- `ERROR`: Error messages
- `SESSION_LOGOUT`: Session logout

## Message Types
[↑ Back to Table of Contents](#table-of-contents)

### OrderMessage
Contains order-related data. See [`ModelOrder`](models.md#order-model) for details.

```python
class OrderMessage:
    type: EventMessageType  # Event type
    data: ModelOrder       # Order data
```

### PositionMessage
Contains position-related data. See [`ModelPosition`](models.md#position-model) for details.

```python
class PositionMessage:
    type: EventMessageType  # Event type
    data: ModelPosition    # Position data
```

### DealMessage
Contains deal-related data. See [`ModelDeal`](models.md#deal-model) for details.

```python
class DealMessage:
    type: EventMessageType  # Event type
    data: ModelDeal       # Deal data
```

### MarketDataMessage
Contains market data updates. See [MarketDataTick](#marketdatatick) for details.

```python
class MarketDataMessage:
    type: EventMessageType  # Event type
    data: MarketDataTick  # Market data tick
```

### MarketDataTick
Contains tick data:
```python
class MarketDataTick:
    symbol_id: int    # Symbol ID
    bid: float       # Bid price
    ask: float       # Ask price
    last: float      # Last price
    volume: float    # Volume
    high: float      # High price
    low: float       # Low price
```

### ProfitUpdate
Contains profit update data:
```python
class ProfitUpdate:
    position_id: int    # Position ID
    profit: float       # Current profit
    total_profit: float # Total profit
```

### InfoMessage
Contains information messages:
```python
class InfoMessage:
    type: EventMessageType.INFO
    data: Dict[str, str]  # {"message": "info message"}
```

### ErrorMessage
Contains error messages:
```python
class ErrorMessage:
    type: EventMessageType.ERROR
    data: Dict[str, str]  # {"message": "error message"}
```

### SessionLogoutMessage
Contains session logout information:
```python
class SessionLogoutMessage:
    type: EventMessageType.SESSION_LOGOUT
    data: Dict[str, str]  # {"session_id": "session_id"}
```

## Usage Examples
[↑ Back to Table of Contents](#table-of-contents)

### Basic Connection and Event Handling

```python
from omtrader import WebSocketClient
from omtrader.websocket.models import EventMessageType

def handle_order_update(data):
    print(f"Order update: {data}")

def handle_position_update(data):
    print(f"Position update: {data}")

def handle_market_data(data):
    print(f"Market data: {data}")

# Initialize client
ws = WebSocketClient(api_key="your_api_key")

# Subscribe to events
ws.subscribe(EventMessageType.ORDERS_UPDATE, handle_order_update)
ws.subscribe(EventMessageType.POSITIONS_UPDATE, handle_position_update)
ws.subscribe(EventMessageType.MARKET_FEED, handle_market_data)

# Connect and start receiving data
ws.connect()
```

### Market Data Subscription

```python
# Subscribe to market data for a symbol
ws.send_market_subscribe(symbol_id=1)

# Unsubscribe from market data
ws.send_market_unsubscribe(symbol_id=1)
```

### Account Updates

```python
# Start receiving account-wide updates
ws.start_account_updates()

# Stop receiving account updates
ws.stop_account_updates()
```

### Sending Custom Messages

```python
from omtrader.websocket.models import WebSocketMessage

# Send a custom message
message = WebSocketMessage(
    type=EventMessageType.MARKET_SUBSCRIBE_SYMBOL,
    data=1  # Symbol ID
)
ws.send(message)
```

### Closing Connection

```python
# Close WebSocket connection
ws.close()
```

## Error Handling
[↑ Back to Table of Contents](#table-of-contents)

The WebSocket client includes built-in error handling and reconnection logic:

```python
def handle_error(error_msg):
    print(f"Error received: {error_msg}")

ws.subscribe(EventMessageType.ERROR, handle_error)
```

## Debugging
[↑ Back to Table of Contents](#table-of-contents)

Enable request/response tracing for debugging:

```python
ws = WebSocketClient(api_key="your_api_key", trace=True)
```

This will print out useful debugging information including:
- Connection details
- Authentication process
- Message sending/receiving
- Errors and reconnection attempts

## Best Practices
[↑ Back to Table of Contents](#table-of-contents)

1. **Error Handling**: Always subscribe to the ERROR event type to handle any errors that occur.

2. **Reconnection**: The client automatically handles reconnection if the connection is lost. You can control this with:
   - `auto_reconnect` parameter
   - `max_reconnect_attempts` parameter

3. **Resource Cleanup**: Always call `close()` when you're done with the WebSocket connection.

4. **Message Queue**: The client maintains a message queue for messages sent while disconnected. These will be sent automatically upon reconnection.

5. **Heartbeat**: The client automatically handles heartbeat messages to keep the connection alive.

## Notes
[↑ Back to Table of Contents](#table-of-contents)

1. Binary messages (market data and profit updates) are automatically decoded and parsed into appropriate objects.

2. The client maintains the WebSocket connection in a separate thread, so your main application can continue running.

3. All callbacks are executed in the WebSocket thread. If you need to perform long-running operations, consider using a separate thread or queue.

4. The client automatically handles authentication and session management.