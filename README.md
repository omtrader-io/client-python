# OMTrader Python Client - REST & WebSocket APIs

Welcome to the official Python client library for the OMTrader REST and WebSocket APIs. To get started, please see the [Getting Started](#getting-started) section below, view the [examples](examples/) directory for code snippets, or explore the comprehensive API documentation.

## Prerequisites

Before installing the OMTrader Python client, ensure your environment has Python 3.8 or higher.

## Install

Since the package is not yet published to PyPI, install directly from GitHub:

```bash
pip install git+https://github.com/your-username/omtrader-client-python.git
```

## Getting Started

To get started, you'll need your OMTrader API key. You can either pass it directly to the client or set it as an environment variable:

**Option 1: Pass API key directly**
```python
client = RESTClient(api_key="your_api_key_here")
```

**Option 2: Use environment variable**
```bash
export OMTRADER_API_KEY="your_api_key_here"
```
```python
client = RESTClient()  # Will use OMTRADER_API_KEY env var
```

## REST API Client

The `RESTClient` provides a unified interface to all OMTrader REST API endpoints, handling authentication, configuration, and providing convenient methods for all trading operations.

### Quick Start

Import and initialize the client:

```python
from omtrader import RESTClient

client = RESTClient(api_key="<API_KEY>")
```

Basic usage example:

```python
# Get account information
account = client.get_account()
print(f"Balance: {account.balance}")

# Create a market order
order_data = {
    "account_id": 1,
    "user_id": 1,
    "symbol_id": 1,
    "volume": 0.01,
    "order_price": 1.2000,
    "side": 0,  # Buy
    "type": 0   # Market order
}
order_id = client.create_order(order_data)
```

### Available Methods

The REST client provides comprehensive methods for:

- Account Management (get_account, open_account)
- Order Management (create_order, update_order, cancel_order, etc.)
- Position Management (list_positions, update_position, close_position, etc.)
- Market Data (list_symbols, get_symbol_ticks_history)
- Trading History (list_deals, get_deal)

## Important: Asynchronous Operation Model

OMTrader uses an asynchronous operation model where:
1. REST endpoints are used to submit operations and query current state
2. WebSocket events provide real-time updates about operation status changes
3. Operations (orders, positions, etc.) are processed asynchronously

This means you should:
1. Set up WebSocket listeners before performing operations
2. Use REST endpoints to submit operations
3. Handle operation outcomes through WebSocket events

See [Asynchronous Operations Workflow](docs/async_workflow.md) for detailed explanation and examples.

## Documentation

For detailed documentation of:
- Available methods, parameters, and examples, see [REST Client Documentation](docs/rest_client.md)
- Response objects and their properties, see [Models Documentation](docs/models.md)
- Error handling and responses, see [Error Handling Documentation](docs/error_handling.md)
- Asynchronous workflow and best practices, see [Async Workflow Documentation](docs/async_workflow.md)

## WebSocket Client

The `WebSocketClient` provides real-time access to:

- Market data feeds
- Order updates
- Position changes
- Account balance updates
- Trade execution notifications

### Quick Start

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
ws.connect()
```

For detailed documentation of all event types, message formats, and examples, see [WebSocket Client Documentation](docs/websocket_client.md).

## Error Handling

The client uses structured exception handling. All API methods may raise `ApiException` for API-related errors:

```python
from omtrader import RESTClient
from omtrader.rest import ApiException

client = RESTClient(api_key="<API_KEY>")

try:
    account = client.get_account()
    print(f"Account balance: {account.balance}")
except ApiException as e:
    print(f"API error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Examples

Check out the [examples](examples/) directory for code samples covering all API endpoints.

## Contributing

If you found a bug or have an idea for a new feature, please first discuss it with us by submitting a new issue. We're also open to pull requests for bug fixes and improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.