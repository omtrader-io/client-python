# Omtrader Python SDK Examples

This directory contains comprehensive examples demonstrating how to use the Omtrader Python SDK effectively. Each module focuses on different aspects of the trading API.

## Prerequisites

1. **Install the SDK**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up authentication**:
   ```bash
   export OMTRADER_API_KEY="your_api_key_here"
   ```

3. **Configure the API endpoint** (if different from default):
   The examples use `http://api.omtrader.io/swagger/v1/trader` by default. Modify `config.py` if needed.

## Available Examples

### 1. Configuration (`config.py`)
- API client setup and configuration
- Authentication management
- Common utilities and error handling decorators

### 2. Account Management (`accounts.py`)
- Get account information (balance, equity, margin)
- Open new trading accounts
- Account status monitoring

**Usage:**
```bash
python examples/accounts.py
```

### 3. Symbol and Market Data (`symbols.py`)
- Get all available trading symbols
- Get specific symbol details (spreads, prices, limits)
- Retrieve historical tick data
- Find symbols by name

**Usage:**
```bash
python examples/symbols.py
```

### 4. Order Management (`orders.py`)
- Create market orders and pending orders
- Get order information and history
- Update order parameters (price, stop loss, take profit)
- Cancel orders
- Order approval workflow

**Usage:**
```bash
python examples/orders.py
```

### 5. Position Management (`positions.py`)
- Get current open positions
- Update position stop loss and take profit
- Close positions (partial or complete)
- Position history and analysis
- Filter profitable/losing positions

**Usage:**
```bash
python examples/positions.py
```

### 6. Deal History and Analysis (`deals.py`)
- Retrieve deal history with pagination
- Get specific deal details
- Filter deals by date range
- Performance analysis and metrics
- Symbol-based performance breakdown

**Usage:**
```bash
python examples/deals.py
```

### 7. Complete Trading Workflows (`complete_trading_flow.py`)
- End-to-end trading session management
- Risk management implementation
- Portfolio monitoring and rebalancing
- Trading strategy examples (scalping, swing trading)
- Automated trading workflows

**Usage:**
```bash
python examples/complete_trading_flow.py
```

### 8. Error Handling and Best Practices (`error_handling.py`)
- Robust error handling techniques
- API rate limiting and retry logic
- Connection management
- Parameter validation
- Graceful shutdown procedures

**Usage:**
```bash
python examples/error_handling.py
```

## Common Patterns

### Basic API Setup
```python
from examples.config import get_api_client
import openapi_client

with get_api_client() as api_client:
    accounts_api = openapi_client.AccountsApi(api_client)
    account = accounts_api.get_trader_account()
```

### Error Handling
```python
from examples.config import handle_api_exception

@handle_api_exception
def your_trading_function():
    # Your API calls here
    pass
```

### Rate Limiting
```python
from examples.error_handling import rate_limited

@rate_limited
def api_call():
    # This will be rate limited automatically
    pass
```

## Safety Notes

⚠️ **Important**: Many examples include commented-out trading operations for safety. Uncomment and modify these carefully:

- Order creation examples are commented out to prevent accidental trades
- Position closing examples are commented out to prevent accidental closures
- Always test with demo accounts first

## Environment Variables

Set these environment variables before running examples:

```bash
# Required
export OMTRADER_API_KEY="your_api_key_here"

# Optional
export OMTRADER_API_HOST="http://api.omtrader.io/swagger/v1/trader"  # Default host
```

## Example Workflows

### 1. Basic Account Check
```bash
python examples/accounts.py
```

### 2. Market Analysis
```bash
python examples/symbols.py
python examples/deals.py
```

### 3. Portfolio Management
```bash
python examples/positions.py
python examples/orders.py
```

### 4. Complete Trading Session
```bash
python examples/complete_trading_flow.py
```

## Error Handling

All examples include proper error handling:

- **API Exceptions**: Handled with detailed error messages
- **Network Issues**: Retry logic with exponential backoff
- **Rate Limiting**: Automatic request throttling
- **Parameter Validation**: Input validation before API calls

## Logging

Examples use Python's built-in logging module. To see debug information:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Testing

Before using the examples with live accounts:

1. Test with demo accounts
2. Use small volumes for testing
3. Verify all parameters carefully
4. Monitor positions closely

## API Reference

For detailed API documentation, see:
- [README.md](../README.md) - Main SDK documentation
- [docs/](../docs/) - API endpoint documentation
- Individual model documentation in the docs folder

## Support

If you encounter issues:

1. Check the error handling examples
2. Verify your API key and permissions
3. Review the API documentation
4. Test with minimal examples first

## Contributing

To add new examples:

1. Follow the existing code structure
2. Include proper error handling
3. Add safety comments for trading operations
4. Update this README with your new example 