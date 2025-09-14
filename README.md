# OMTrader Python Client - REST & WebSocket APIs

Welcome to the official Python client library for the OMTrader REST and WebSocket API. To get started, please see the [Getting Started](#getting-started) section below, view the [examples](examples/) directory for code snippets, or explore the comprehensive API documentation.

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

Import the RESTClient:

```python
from omtrader import RESTClient
```

Create a new client with your API key:

```python
client = RESTClient(api_key="<API_KEY>")
```

### Using the Client

Request data using client methods:

```python
# Get account information
account = client.get_account()
print(f"Balance: {account.balance}")

# List current positions
positions = client.list_positions()
for position in positions:
    print(f"Position {position.id}: {position.volume_current} lots")

# List available symbols
symbols = client.list_symbols()
for symbol in symbols:
    print(f"Symbol: {symbol.symbol}")

# Get order history
orders = client.list_orders_history()
print(f"Found {len(orders)} historical orders")

# Create a new order (example structure)
order_data = {
    "account_id": 1,
    "user_id": 1,
    "symbol_id": 1,
    "volume": 0.01,
    "order_price": 1.2000,
    "side": 0,  # 0=Buy, 1=Sell
    "type": 0   # 0=Market order
}
# order_id = client.create_order(order_data)  # Uncomment to execute
```

### Available Methods

**Account Management:**
- `get_account()` - Get account information
- `open_account(data)` - Open new trading account

**Order Management:**
- `list_orders()` - List current orders
- `get_order(id)` - Get specific order
- `create_order(data)` - Create new order
- `update_order(id, data)` - Update existing order
- `cancel_order(id)` - Cancel order
- `list_orders_history()` - Get order history

**Position Management:**
- `list_positions()` - List current positions
- `get_position(id)` - Get specific position
- `update_position(id, data)` - Update position
- `close_position(id)` - Close position
- `list_positions_history()` - Get position history

**Market Data:**
- `list_symbols()` - List available trading symbols
- `get_symbol(id)` - Get specific symbol details
- `get_symbol_ticks_history(id, **params)` - Get historical tick data

**Trading History:**
- `list_deals()` - List completed deals
- `get_deal(id)` - Get specific deal details

## Debugging with RESTClient

Sometimes you may find it useful to see the actual request and response details while working with the API. The `RESTClient` allows for this through its `trace=True` option:

```python
client = RESTClient(api_key="<API_KEY>", trace=True)
```

When debug mode is enabled, the client will print out useful debugging information for each API request, including the request URL, headers sent, and response details.

## WebSocket Client

The WebSocket client for real-time data streaming is coming soon. The client structure is prepared and will provide:

- Real-time market data feeds
- Live order and position updates
- Account balance changes
- Trade execution notifications

Stay tuned for WebSocket functionality in upcoming releases.

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

Check out the [examples](examples/) directory for comprehensive code samples covering all API endpoints and common use cases.

## Contributing

If you found a bug or have an idea for a new feature, please first discuss it with us by submitting a new issue. We're also open to pull requests for bug fixes and improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.