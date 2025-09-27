# RESTClient Documentation

## Table of Contents
- [Initialization](#initialization)
  - [Parameters](#parameters)
- [Account Methods](#account-methods)
  - [get_account()](#get_account)
  - [open_account()](#open_accountaccount_data)
- [Order Methods](#order-methods)
  - [list_orders()](#list_orderskwargs)
  - [get_order()](#get_orderorder_id)
  - [create_order()](#create_orderorder_data)
  - [update_order()](#update_orderorder_id-order_data)
  - [cancel_order()](#cancel_orderorder_id-cancel_datanone)
  - [list_orders_history()](#list_orders_historykwargs)
  - [approve_order()](#approve_orderorder_id-approval_data)
- [Position Methods](#position-methods)
  - [list_positions()](#list_positionskwargs)
  - [get_position()](#get_positionposition_id)
  - [update_position()](#update_positionposition_id-position_data)
  - [close_position()](#close_positionposition_id-close_datanone)
  - [list_positions_history()](#list_positions_historykwargs)
- [Symbol Methods](#symbol-methods)
  - [list_symbols()](#list_symbolskwargs)
  - [get_symbol()](#get_symbolsymbol_id)
  - [get_symbol_ticks_history()](#get_symbol_ticks_historysymbol_id-kwargs)
- [Deal Methods](#deal-methods)
  - [list_deals()](#list_dealskwargs)
  - [get_deal()](#get_dealdeal_id)
- [Error Handling](#error-handling)
- [Debugging](#debugging)

The `RESTClient` provides a unified interface to all OMTrader REST API endpoints, handling authentication, configuration, and providing convenient methods for all trading operations.

## Initialization
[↑ Back to Table of Contents](#table-of-contents)

```python
from omtrader import RESTClient

# With API key directly
client = RESTClient(api_key="your_api_key")

# With environment variable
# export OMTRADER_API_KEY="your_api_key"
client = RESTClient()  # Uses env var
```

### Parameters

- `api_key` (str, optional): Your OMTrader API key. If not provided, will look for OMTRADER_API_KEY environment variable.
- `host` (str, optional): API host URL. If not provided, will look for OMTRADER_HOST environment variable and defaults to production endpoint if none are provided.
- `debug` (bool): Enable debug logging. Defaults to False.
- `trace` (bool): Enable request/response tracing for debugging. Defaults to False.
- `timeout` (float): Request timeout in seconds. Defaults to 30.0.

## Account Methods
[↑ Back to Table of Contents](#table-of-contents)

### get_account()
Get trader account information.

```python
account = client.get_account()
print(f"Balance: {account.balance}")
```

**Returns:** [`ModelTradeAccount`](models.md#trade-account-model) object with account information.

### open_account(account_data)
Open a new trader account.

```python
account = client.open_account(account_data)
```

**Parameters:**
- `account_data` (dict or MessagingOpenAccount): Account opening parameters.

**Returns:** [`ModelTradeAccount`](models.md#trade-account-model) object with created account information.

## Order Methods
[↑ Back to Table of Contents](#table-of-contents)

### list_orders(**kwargs)
List all orders.

```python
orders = client.list_orders()
for order in orders:
    print(f"Order {order.id}")
```

**Parameters:**
- `**kwargs`: Additional request parameters

**Returns:** List of [`ModelOrder`](models.md#order-model) objects.

### get_order(order_id)
Get specific order by ID.

```python
order = client.get_order("123")
print(f"Order status: {order.status}")
```

**Parameters:**
- `order_id` (str): Order ID to retrieve

**Returns:** [`ModelOrder`](models.md#order-model) object.

### create_order(order_data)
Create a new order.

```python
order_data = {
    "account_id": 1,
    "user_id": 1,
    "symbol_id": 1,
    "volume": 0.01,
    "order_price": 1.2000,
    "side": 0,  # Buy
    "type": 0   # Market order
}
response = client.create_order(order_data)
```

**Parameters:**
- `order_data` (dict or MessagingCrtOrder): Order parameters containing:
  - `account_id` (int): Account ID (required)
  - `user_id` (int): User ID (required)
  - `symbol_id` (int): Symbol ID (required)
  - `volume` (float): Order volume (required)
  - `order_price` (float): Order price (required)
  - `side` (int, optional): Order side - 0=Buy, 1=Sell
  - `type` (int, optional): Order type - 0=market, 1=buy_limit, etc.
  - `price_sl` (float, optional): Stop loss price
  - `price_tp` (float, optional): Take profit price
  - `comment` (str, optional): Order comment
  - `expiration_police` (ModelExpirationPolicy, optional): Expiration policy
  - `time_expiration` (str, optional): Expiration time

**Returns:** `HttpHttpResponse` object containing the API response. Check response.status_code for success (200/201).

### update_order(order_id, order_data)
Update an existing order.

```python
client.update_order("123", {"volume": 0.02})
```

**Parameters:**
- `order_id` (str): Order ID to update
- `order_data` (dict or MessagingUptOrder): Update parameters

**Returns:** `str` containing the API response.

### cancel_order(order_id, cancel_data=None)
Cancel an order.

```python
client.cancel_order("123")
```

**Parameters:**
- `order_id` (str): Order ID to cancel
- `cancel_data` (dict or MessagingCancelOrder, optional): Cancel parameters. If None, will be created automatically with order details.

**Returns:** `str` containing the API response.

### list_orders_history(**kwargs)
Get orders history.

```python
history = client.list_orders_history()
```

**Parameters:**
- `**kwargs`: Additional request parameters

**Returns:** List of historical [`ModelOrder`](models.md#order-model) objects.

### approve_order(order_id, approval_data)
Approve an order.

```python
client.approve_order("123", approval_data)
```

**Parameters:**
- `order_id` (str): Order ID to approve
- `approval_data`: Approval parameters

**Returns:** `str` containing the API response.

## Position Methods
[↑ Back to Table of Contents](#table-of-contents)

### list_positions(**kwargs)
List all positions.

```python
positions = client.list_positions()
for pos in positions:
    print(f"Position {pos.id}")
```

**Parameters:**
- `**kwargs`: Additional request parameters

**Returns:** List of [`ModelPosition`](models.md#position-model) objects.

### get_position(position_id)
Get specific position by ID.

```python
position = client.get_position("123")
print(f"Position profit: {position.profit}")
```

**Parameters:**
- `position_id` (str): Position ID to retrieve

**Returns:** [`ModelPosition`](models.md#position-model) object.

### update_position(position_id, position_data)
Update a position.

```python
client.update_position("123", {"price_sl": 1.2000})
```

**Parameters:**
- `position_id` (str): Position ID to update
- `position_data` (dict or MessagingUptPosition): Update parameters

**Returns:** `str` containing the API response.

### close_position(position_id, close_data=None)
Close a position.

```python
client.close_position("123")
```

**Parameters:**
- `position_id` (str): Position ID to close
- `close_data` (dict or MessagingClosePosition, optional): Close parameters. If None, will be created automatically with position details.

**Returns:** `str` containing the API response.

### list_positions_history(**kwargs)
Get positions history.

```python
history = client.list_positions_history()
```

**Parameters:**
- `**kwargs`: Additional request parameters

**Returns:** List of historical [`ModelPosition`](models.md#position-model) objects.

## Symbol Methods
[↑ Back to Table of Contents](#table-of-contents)

### list_symbols(**kwargs)
List all available symbols.

```python
symbols = client.list_symbols()
for symbol in symbols:
    print(f"Symbol: {symbol.symbol}")
```

**Parameters:**
- `**kwargs`: Additional request parameters

**Returns:** List of `MessagingViewSymbol` objects (see [Symbol Model](models.md#symbol-model)).

### get_symbol(symbol_id)
Get specific symbol by ID.

```python
symbol = client.get_symbol("1")
print(f"Symbol name: {symbol.symbol}")
```

**Parameters:**
- `symbol_id` (str): Symbol ID to retrieve

**Returns:** `MessagingViewSymbol` object (see [Symbol Model](models.md#symbol-model)).

### get_symbol_ticks_history(symbol_id, **kwargs)
Get symbol ticks history.

```python
ticks = client.get_symbol_ticks_history(
    "1", 
    var_from=1234567890, 
    to=1234567900,
    resolution="1m",
    count_back=60
)
```

**Parameters:**
- `symbol_id` (str): Symbol ID to get ticks for
- `**kwargs`: Required parameters:
  - `var_from` (int): From timestamp
  - `to` (int): To timestamp
  - `resolution` (str): Resolution (e.g., "1m", "1h", "1d")
  - `count_back` (int): Number of ticks to retrieve
  - `type` (str, optional): Type ("bid" or "ask")

**Returns:** List of `MessagingHistoryTick` objects (see [MarketDataTick Model](models.md#marketdatatick)).

## Deal Methods
[↑ Back to Table of Contents](#table-of-contents)

### list_deals(**kwargs)
List all deals.

```python
deals = client.list_deals(limit=10)
for deal in deals:
    print(f"Deal {deal.id}: {deal.profit}")
```

**Parameters:**
- `**kwargs`: Optional parameters:
  - `page` (int): Page number
  - `limit` (int): Limit number
  - `var_from` (str): From date
  - `to` (str): To date
  - `sort_by` (str): Sort by field
  - `dir` (str): Sort direction

**Returns:** List of [`ModelDeal`](models.md#deal-model) objects.

### get_deal(deal_id)
Get specific deal by ID.

```python
deal = client.get_deal("123")
print(f"Deal profit: {deal.profit}")
```

**Parameters:**
- `deal_id` (str): Deal ID to retrieve

**Returns:** [`ModelDeal`](models.md#deal-model) object.

## Error Handling
[↑ Back to Table of Contents](#table-of-contents)

All methods may raise `ApiException` for API-related errors:

```python
from omtrader import RESTClient
from omtrader.rest import ApiException

client = RESTClient(api_key="your_api_key")

try:
    account = client.get_account()
    print(f"Account balance: {account.balance}")
except ApiException as e:
    print(f"API error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Debugging
[↑ Back to Table of Contents](#table-of-contents)

Enable request/response tracing for debugging:

```python
client = RESTClient(api_key="your_api_key", trace=True)
```

This will print out useful debugging information for each API request, including:
- Request URL
- Headers sent
- Response details