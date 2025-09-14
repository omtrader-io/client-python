# WebSocket API Documentation

This document provides comprehensive documentation for the WebSocket implementation in the OneTrade WebTrader application. The WebSocket connection handles real-time communication between the client and server for trading operations, market data, and account updates.

## Table of Contents

- [Connection](#connection)
- [Message Format](#message-format)
- [Heartbeat](#heartbeat)
- [Authentication](#authentication)
- [Event Types](#event-types)
- [Outgoing Messages (Client → Server)](#outgoing-messages-client--server)
- [Incoming Messages (Server → Client)](#incoming-messages-server--client)
- [Error Handling](#error-handling)
- [Market Data](#market-data)
- [Session Management](#session-management)

## Connection

### WebSocket URL
```
wss://{wsURL}/ws/v1?session_id={sessionId}&access_token={accessToken}

```

### Connection Flow
1. Validate session ID via HTTP POST to `{httpURL}/ws/v1/{sessionId}`
2. Establish WebSocket connection with session and access token
3. Start heartbeat mechanism
4. Subscribe to account-wide updates
5. Process queued events

### Connection States
- **CONNECTING**: Initial connection attempt
- **OPEN**: Connection established and ready
- **CLOSING**: Connection terminating
- **CLOSED**: Connection terminated

## Message Format

### Base Message Structure

#### Outgoing Message (Client → Server)
```python
interface SendWebSocketEvent<T> {
  type: EventMessageType;
  data?: T;
}
```

#### Incoming Message (Server → Client)
```python
interface ReceiveWebSocketEvent<T> {
  type: EventMessageType;
  data?: T;
}
```

### Message Types
```python 

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

```

## Heartbeat

The WebSocket connection maintains a heartbeat mechanism to ensure connection stability.

### Heartbeat Interval
- **Frequency**: Every 30 seconds
- **Message**: String `"9"`
- **Response**: String `"10"` (ignored by client)

### Implementation
```python 
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
```

## Authentication

### Session Validation
Before establishing WebSocket connection, the client validates the session:

```http

POST {httpURL}/ws/v1/{sessionId}

```

### Possible Responses
- **Success**: Session validated, proceed with WebSocket connection
- **Error**: `"session is already used"` - Multiple tabs detected
- **Error**: Other errors trigger reconnection attempt

## Event Types

## Outgoing Messages (Client → Server)

### 1. Market Data Subscription

#### Subscribe to Symbol Market Data
```python 
{
  type: "market_subscribe_symbol",
  data: number // symbolId
}
```

**Purpose**: Subscribe to real-time price updates for a specific trading symbol.

**Example**:
```python
{
  type: "market_subscribe_symbol",
  data: 1 // EUR/USD symbol ID
}
```

#### Unsubscribe from Symbol Market Data
```python
{
  type: "market_unsubscribe_symbol",
  data: number // symbolId
}
```

**Purpose**: Stop receiving real-time price updates for a specific trading symbol.


### 2. Account Management

#### Start Account-Wide Updates
```python
{
  type: "start_account_all",
  data: null
}
```

**Purpose**: Begin receiving all account-related updates (orders, positions, deals, etc.).

#### Stop Account-Wide Updates
```python
{
  type: "stop_account_all",
  data: null
}
```

**Purpose**: Stop receiving account-related updates.

### 3. System Messages

#### Heartbeat (Ping)
```python
// Raw string message
"9"
```

**Purpose**: Maintain connection alive and detect disconnections.

---

## Incoming Messages (Server → Client)

### 1. Session Management

#### Session Logout
```python
{
  type: "session_logout",
  data: {
    session_id: string
  }
}
```

**Purpose**: Notify client that the session has been logged out from another location.

**Client Action**: 
- Compare session_id with current session
- If match, trigger logout flow

### 2. System Messages

#### Information Message
```python
{
  type: "info",
  data: {
    message: string
  }
}
```

**Purpose**: Display informational message to user.

**Client Action**: Show notification with type "info"

#### Error Message
```python
{
  type: "error",
  data: {
    message: string
  }
}
```

**Purpose**: Display error message to user.

**Client Action**: Show notification with type "error"

#### Heartbeat Response (Pong)
```python
// Raw string message
"10"
```

**Purpose**: Server response to client heartbeat.

**Client Action**: Ignore (connection confirmed alive)

### 3. Order Events

#### Order Placed
```python
{
  type: "orders_place",
  data: Order
}
```

**Order Interface**:
```python
@dataclass
class Order:
    id: int
    account_id: int
    symbol_id: int
    symbol: Symbol
    type: OrderType
    side: SideType
    volume_initial: float
    volume_current: float
    price_order: float
    price_current: float
    price_sl: Optional[float] = None
    price_tp: Optional[float] = None
    status: OrderStatus = OrderStatus.PENDING
    reason: Optional[ReasonType] = None
    comment: Optional[str] = None
    external_id: Optional[str] = None
    created_at: datetime = None
    updated_at: datetime = None
    time_setup: datetime = None
    time_expiration: Optional[datetime] = None
    time_done: Optional[datetime] = None
```

**Purpose**: Notify that a new order has been placed.

**Client Action**: Add order to orders list in Redux store

#### Order Updated
```python
{
  type: "orders_update",
  data: Order
}
```

**Purpose**: Notify that an existing order has been modified.

**Client Action**: Update order in Redux store

#### Order Cancelled
```python
{
  type: "orders_cancel",
  data: Order
}
```

**Purpose**: Notify that an order has been cancelled.

**Client Action**: Update order status in Redux store

#### Order Expired
```python
{
  type: "orders_expired",
  data: Order
}
```

**Purpose**: Notify that an order has expired.

**Client Action**: Update order status in Redux store

#### Order Rejected
```python
{
  type: "orders_rejected",
  data: Order
}
```

**Purpose**: Notify that an order has been rejected by the server.

**Client Action**: Update order status and show rejection reason

#### Order Requoted
```python
{
  type: "dealing_order_requote",
  data: Order
}
```

**Purpose**: Notify that an order has been requoted (new price offered).

**Client Action**: Show requote dialog for user decision

### 4. Position Events

#### Position Opened
```python
{
  type: "positions_open",
  data: Position
}
```

**Position Interface**:
```python
@dataclass
class Position:
    id: int
    account_id: int
    symbol_id: int
    symbol: Symbol
    side: SideType
    volume_initial: float
    volume_current: float
    price_open: float
    price_current: float
    price_sl: Optional[float] = None
    price_tp: Optional[float] = None
    profit: float = 0.0
    total_profit: float = 0.0
    swaps: float = 0.0
    storage: float = 0.0
    status: PositionStatus = PositionStatus.OPEN
    reason: Optional[ReasonType] = None
    comment: Optional[str] = None
    external_id: Optional[str] = None
    created_at: datetime = None
    updated_at: datetime = None
```

**Purpose**: Notify that a new position has been opened.

**Client Action**: Add position to positions list in Redux store

#### Position Updated
```python
{
  type: "positions_update",
  data: Position
}
```

**Purpose**: Notify that an existing position has been modified (usually profit/loss updates).

**Client Action**: Update position in Redux store

#### Position Closed
```python
{
  type: "positions_close",
  data: Position
}
```

**Purpose**: Notify that a position has been closed.

**Client Action**: Update position status in Redux store

### 5. Deal Events

#### Deal Created
```python
{
  type: "deals_create",
  data: Deal
}
```

**Deal Interface**:
```python
@dataclass
class Deal:
    id: int
    account_id: int
    order_id: int
    position_id: int
    symbol_id: int
    symbol: Symbol
    side: SideType
    direction: DirectionType
    volume: float
    price: float
    entry: float
    profit: float
    profit_raw: float
    commission: float
    swap: float
    fee: float
    storage: float
    market_bid: float
    market_ask: float
    market_last: float
    reason: ReasonType
    channel: ChannelType
    comment: Optional[str] = None
    external_id: Optional[str] = None
    created_at: datetime = None
    updated_at: datetime = None
```

**Purpose**: Notify that a new deal (trade execution) has been created.

**Client Action**: Add deal to deals history in Redux store

#### Deal Updated
```python
{
  type: "deals_update",
  data: Deal
}
```

**Purpose**: Notify that an existing deal has been modified.

**Client Action**: Update deal in Redux store

### 6. Journal Events

#### Journal Entry Created
```python
{
  type: "journal_create",
  data: Journal
}
```

**Journal Interface**:
```python

@dataclass
class Journal:
    id: int
    user_id: int
    desc: str
    ip: str
    device: str
    os: str
    channel: ChannelType
    created_at: datetime
```

**Purpose**: Notify of new activity log entry.

**Client Action**: Add journal entry to activity log in Redux store

### 7. Report Events

#### Report Created
```python
{
  type: "report_create",
  data: Report
}
```

**Report Interface**:
```python
@dataclass
class Report:
    id: int
    user_id: int
    type: ReportType
    status: ReportStatus
    kind: str
    desc: str
    query: str
    url: str
```

**Purpose**: Notify that a requested report has been generated.

**Client Action**: Update report status and provide download link

## Market Data

### Price Updates (Binary Data)

The WebSocket also receives binary market data in Blob format:

#### Price Data Format
```python
// Received as Blob, converted to text
// Format: Comma-separated values with symbol price information
```

#### Profit Updates Format
```python
// Received as Blob, converted to text starting with "s,"
// Format: s,{profit_data}
```

**Client Actions**:
- **Price Data**: Update symbol prices in DOM via `updatePricesFromDOM()`
- **Profit Data**: Update position profits in DOM via `updateProfitsFromDOM()`

## Error Handling

### Connection Errors

#### Session Already Used
```python
// HTTP Response during session validation
{
  message: "session is already used"
}
```

**Client Action**: Display two tabs detection warning

#### Other Connection Errors
**Client Action**: Trigger reconnection attempt

### WebSocket Event Errors

#### Unknown Message Type
```python
console.error("Unsupported message type received:", messageType);
```

#### Message Processing Errors
- Errors during message handling are logged
- Application continues operation
- User may be notified depending on error type

## Session Management

### Connection States

#### Two Tabs Detection
When the same session is used in multiple tabs:
1. HTTP validation returns "session is already used"
2. Client displays warning modal
3. User must choose which tab to keep active

#### Session Logout
When session is terminated from another location:
1. Server sends `SESSION_LOGOUT` event
2. Client checks session_id match
3. If match, user is logged out automatically

#### Reconnection Flow
On connection loss:
1. WebSocket `close` event triggers reconnection flag
2. Application attempts to reconnect
3. On successful reconnection, queued events are sent
4. Account subscriptions are restored

### Event Queue Management

When WebSocket is not connected:
- Outgoing events are queued in `eventQueue[]`
- Events are sent immediately upon reconnection
- Queue is cleared after successful transmission

## Usage Examples

### Subscribing to Market Data
```python
// Subscribe to EUR/USD (symbol ID: 1)

client.subscribe(EventMessageType.ORDERS_PLACE, handle_order_placed)

// Unsubscribe later
await ws.unsubscribe2marketBySymbol(1);
```

### Starting Account Updates
```python
// Begin receiving all account updates
await ws.startAccountAll();

// Stop account updates
await ws.stopAccountAll();
```

### Connection Management
```python
// Connect to WebSocket
await ws.connect();

// Disconnect
await ws.disconnect();
```

## Redux Integration

All WebSocket events are dispatched to Redux store using appropriate thunks:

- **Orders**: `handlePlaceOrderWs`, `handleUpdateOrderWs`, `handleCancelOrderWs`, etc.
- **Positions**: `handleOpenPositionWs`, `handleUpdatePositionWs`, `handleClosePositionWs`
- **Deals**: `handleCreateDealWs`, `handleUpdateDealWs`
- **Journal**: `handleCreateJournal`
- **Reports**: `handleReportCreateWs`
- **Notifications**: `setNotification`
- **User State**: `setSessionLoggedOut`, `setTwoTabsDetected`, `setWSReconnect`, `setWSStatus`

This ensures real-time updates are immediately reflected in the application state and UI.