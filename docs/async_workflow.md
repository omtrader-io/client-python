# Asynchronous Operations Workflow

## Table of Contents
- [Overview](#overview)
- [Request vs Operation Status](#request-vs-operation-status)
- [REST vs WebSocket Responsibilities](#rest-vs-websocket-responsibilities)
- [Common Workflows](#common-workflows)
- [Best Practices](#best-practices)

## Overview
[↑ Back to Table of Contents](#table-of-contents)

The OMTrader API uses an asynchronous workflow where:
1. REST endpoints are used to **submit** operations and **query** current state
2. WebSocket events provide **real-time updates** about operation status changes
3. Operations are processed asynchronously by the system

## Request vs Operation Status
[↑ Back to Table of Contents](#table-of-contents)

There are two distinct types of status you need to handle:

### 1. Request Status (Immediate REST Response)
This tells you if your request was accepted by the system:

```python
try:
    response = rest_client.create_order({
        "account_id": 1,
        "symbol_id": 1,
        "volume": 0.01,
        "order_price": 1.2000
    })
    
    if response.success:
        print("Request accepted by system")
        print(f"Status code: {response.code}")  # 200/201 for success
    else:
        print("Request rejected by system")
        print(f"Error: {response.error}")
        print(f"Message: {response.message}")
        
except ApiException as e:
    print("Request failed to reach system")
    print(f"Error: {e}")
```

Common request rejection reasons:
- Invalid input data (400)
- Authentication failure (401)
- Invalid permissions (403)
- Rate limiting (429)
- System unavailable (500)

### 2. Operation Status (WebSocket Events)
This tells you what happened after your request was accepted:

```python
def handle_order_events(msg):
    event_type = msg.type
    order = msg.data
    
    if event_type == EventMessageType.ORDERS_PLACE:
        print("Order placed in system")
        print(f"Order ID: {order.id}")
        
    elif event_type == EventMessageType.ORDERS_REJECTED:
        print("Order rejected during processing")
        print(f"Reason: {order.reason}")
        
    elif event_type == EventMessageType.ORDERS_UPDATE:
        print(f"Order status updated: {order.status}")
        
    elif event_type == EventMessageType.ORDERS_EXPIRED:
        print("Order expired")
        
    elif event_type == EventMessageType.ORDERS_REQUOTED:
        print("Order needs requoting")

# Subscribe to all order events
ws_client.subscribe(EventMessageType.ORDERS_PLACE, handle_order_events)
ws_client.subscribe(EventMessageType.ORDERS_REJECTED, handle_order_events)
ws_client.subscribe(EventMessageType.ORDERS_UPDATE, handle_order_events)
ws_client.subscribe(EventMessageType.ORDERS_EXPIRED, handle_order_events)
ws_client.subscribe(EventMessageType.ORDERS_REQUOTED, handle_order_events)
```

## REST vs WebSocket Responsibilities
[↑ Back to Table of Contents](#table-of-contents)

### REST Client (`RESTClient`)
- Submit new operations (create order, close position, etc.)
- Receive immediate validation/acceptance of requests
- Query current state (get account info, list positions, etc.)
- Get historical data (order history, position history, etc.)

### WebSocket Client (`WebSocketClient`)
- Receive real-time operation status updates
- Get notified of operation outcomes
- Monitor changes to positions, orders, etc.
- Track account balance changes
- Get market data updates

## Common Workflows
[↑ Back to Table of Contents](#table-of-contents)

### Complete Order Flow Example

```python
from omtrader import RESTClient, WebSocketClient
from omtrader.websocket.models import EventMessageType

# First, set up WebSocket to monitor order events
ws = WebSocketClient(api_key="your_api_key")

def handle_order_events(msg):
    event_type = msg.type
    order = msg.data
    
    if event_type == EventMessageType.ORDERS_PLACE:
        print("Order placed successfully")
        print(f"Order ID: {order.id}")
        print(f"Initial status: {order.status}")
        
    elif event_type == EventMessageType.ORDERS_UPDATE:
        print(f"Order {order.id} updated:")
        print(f"New status: {order.status}")
        if hasattr(order, 'filled_volume'):
            print(f"Filled volume: {order.filled_volume}")
        
    elif event_type == EventMessageType.ORDERS_REJECTED:
        print(f"Order {order.id} rejected during processing:")
        print(f"Reason: {order.reason}")
        print(f"Details: {order.comment}")
        
    elif event_type == EventMessageType.ORDERS_EXPIRED:
        print(f"Order {order.id} expired")
        
    elif event_type == EventMessageType.ORDERS_REQUOTED:
        print(f"Order {order.id} needs requoting")
        print(f"New price: {order.price_current}")

# Subscribe to all relevant order events
ws.subscribe(EventMessageType.ORDERS_PLACE, handle_order_events)
ws.subscribe(EventMessageType.ORDERS_UPDATE, handle_order_events)
ws.subscribe(EventMessageType.ORDERS_REJECTED, handle_order_events)
ws.subscribe(EventMessageType.ORDERS_EXPIRED, handle_order_events)
ws.subscribe(EventMessageType.ORDERS_REQUOTED, handle_order_events)

# Connect WebSocket
ws.connect()

# Now submit the order via REST
rest = RESTClient(api_key="your_api_key")

try:
    # Submit order request
    response = rest.create_order({
        "account_id": 1,
        "user_id": 1,
        "symbol_id": 1,
        "volume": 0.01,
        "order_price": 1.2000,
        "side": 0,  # Buy
        "type": 0   # Market
    })
    
    if response.success:
        print("Order request accepted:")
        print(f"Status code: {response.code}")
        print("Waiting for order events...")
    else:
        print("Order request rejected:")
        print(f"Error: {response.error}")
        print(f"Message: {response.message}")
        
except ApiException as e:
    print("Failed to submit order:")
    print(f"Error: {e}")
```

### Position Management Flow

```python
# Set up WebSocket first
ws = WebSocketClient(api_key="your_api_key")

def handle_position_events(msg):
    event_type = msg.type
    position = msg.data
    
    if event_type == EventMessageType.POSITIONS_OPEN:
        print(f"Position {position.id} opened:")
        print(f"Volume: {position.volume_initial}")
        print(f"Opening price: {position.price_open}")
        
    elif event_type == EventMessageType.POSITIONS_UPDATE:
        print(f"Position {position.id} updated:")
        print(f"Current volume: {position.volume_current}")
        print(f"Current profit: {position.profit}")
        
    elif event_type == EventMessageType.POSITIONS_CLOSE:
        print(f"Position {position.id} closed:")
        print(f"Final profit: {position.profit}")

# Subscribe to position events
ws.subscribe(EventMessageType.POSITIONS_OPEN, handle_position_events)
ws.subscribe(EventMessageType.POSITIONS_UPDATE, handle_position_events)
ws.subscribe(EventMessageType.POSITIONS_CLOSE, handle_position_events)
ws.connect()

# Now use REST to submit position operations
rest = RESTClient(api_key="your_api_key")

try:
    # Try to close position
    response = rest.close_position("123")
    
    if response.success:
        print("Close position request accepted")
        print("Waiting for position events...")
    else:
        print("Close position request rejected:")
        print(f"Error: {response.error}")
        print(f"Message: {response.message}")
        
except ApiException as e:
    print("Failed to submit close request:")
    print(f"Error: {e}")
```

## Best Practices
[↑ Back to Table of Contents](#table-of-contents)

1. **Always Set Up WebSocket First**
   - Connect to WebSocket before submitting operations
   - Subscribe to relevant events
   - Have handlers ready for all possible outcomes

2. **Handle Both Request and Operation Status**
   - Check REST response for request acceptance
   - Use WebSocket events for operation status
   - Log both types of status for debugging

3. **Implement Proper Error Handling**
   - Handle REST request errors (ApiException)
   - Handle request rejection (response.success = False)
   - Handle operation rejection (WebSocket events)
   - Consider timeouts and retries for REST requests

4. **Use Appropriate Status Checks**
   - Don't use REST endpoints to poll for status
   - Rely on WebSocket events for real-time updates
   - Keep track of operation state in your application
