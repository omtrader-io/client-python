"""
Error Handling and Best Practices Examples

This module demonstrates:
- Proper error handling techniques
- API rate limiting and retry logic
- Connection management
- Logging best practices
- Testing API connectivity
"""

import openapi_client
from openapi_client.rest import ApiException
from examples.config import get_api_client
import time
import logging
from functools import wraps
from typing import Optional, Callable, Any


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def retry_on_failure(max_retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """
    Decorator for retrying API calls on failure.
    
    Args:
        max_retries: Maximum number of retry attempts
        delay: Initial delay between retries in seconds
        backoff: Multiplier for delay on each retry
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            current_delay = delay
            last_exception = None
            
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except ApiException as e:
                    last_exception = e
                    
                    # Don't retry on client errors (4xx)
                    if 400 <= e.status < 500:
                        logger.error(f"Client error {e.status}: {e.reason}")
                        raise
                    
                    # Retry on server errors (5xx) and network issues
                    if attempt < max_retries:
                        logger.warning(
                            f"API call failed (attempt {attempt + 1}/{max_retries + 1}): "
                            f"{e.status} - {e.reason}. Retrying in {current_delay}s..."
                        )
                        time.sleep(current_delay)
                        current_delay *= backoff
                    else:
                        logger.error(f"All retry attempts failed: {e}")
                        raise
                except Exception as e:
                    last_exception = e
                    logger.error(f"Unexpected error: {e}")
                    raise
            
            # This shouldn't be reached, but just in case
            raise last_exception
        
        return wrapper
    return decorator


class APIErrorHandler:
    """Centralized error handling for API operations."""
    
    @staticmethod
    def handle_api_exception(e: ApiException, operation: str) -> None:
        """
        Handle API exceptions with detailed logging.
        
        Args:
            e: The ApiException that occurred
            operation: Description of the operation that failed
        """
        logger.error(f"API Exception in {operation}")
        logger.error(f"Status Code: {e.status}")
        logger.error(f"Reason: {e.reason}")
        
        if e.body:
            logger.error(f"Response Body: {e.body}")
        
        # Handle specific error codes
        if e.status == 401:
            logger.error("Authentication failed. Check your API key.")
        elif e.status == 403:
            logger.error("Access forbidden. Check your permissions.")
        elif e.status == 404:
            logger.error("Resource not found.")
        elif e.status == 429:
            logger.error("Rate limit exceeded. Please slow down your requests.")
        elif e.status >= 500:
            logger.error("Server error. The issue is on the server side.")
    
    @staticmethod
    def is_retryable_error(e: ApiException) -> bool:
        """
        Determine if an API error is retryable.
        
        Args:
            e: The ApiException to check
            
        Returns:
            bool: True if the error is retryable
        """
        # Retry on server errors and rate limiting
        return e.status >= 500 or e.status == 429


class RateLimiter:
    """Simple rate limiter for API calls."""
    
    def __init__(self, calls_per_second: float = 5.0):
        self.calls_per_second = calls_per_second
        self.min_interval = 1.0 / calls_per_second
        self.last_call_time = 0.0
    
    def wait_if_needed(self) -> None:
        """Wait if necessary to respect rate limits."""
        current_time = time.time()
        time_since_last_call = current_time - self.last_call_time
        
        if time_since_last_call < self.min_interval:
            sleep_time = self.min_interval - time_since_last_call
            logger.debug(f"Rate limiting: sleeping for {sleep_time:.2f}s")
            time.sleep(sleep_time)
        
        self.last_call_time = time.time()


# Global rate limiter instance
rate_limiter = RateLimiter(calls_per_second=5.0)


def rate_limited(func: Callable) -> Callable:
    """Decorator to apply rate limiting to API calls."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        rate_limiter.wait_if_needed()
        return func(*args, **kwargs)
    return wrapper


@retry_on_failure(max_retries=3, delay=1.0)
@rate_limited
def test_api_connectivity():
    """
    Test basic API connectivity.
    
    Returns:
        bool: True if API is accessible
    """
    print("=== Testing API Connectivity ===")
    
    try:
        with get_api_client() as api_client:
            accounts_api = openapi_client.AccountsApi(api_client)
            
            # Try to get account information
            account = accounts_api.get_trader_account()
            
            print("✓ API connectivity test passed")
            print(f"✓ Account ID: {account.id}")
            print(f"✓ Account Currency: {account.currency}")
            
            return True
            
    except ApiException as e:
        APIErrorHandler.handle_api_exception(e, "connectivity test")
        return False
    except Exception as e:
        logger.error(f"Unexpected error during connectivity test: {e}")
        return False


@retry_on_failure(max_retries=2, delay=0.5)
@rate_limited
def robust_get_symbols():
    """
    Example of robust symbol retrieval with error handling.
    
    Returns:
        List or None: List of symbols or None if failed
    """
    print("=== Robust Symbol Retrieval ===")
    
    try:
        with get_api_client() as api_client:
            symbols_api = openapi_client.SymbolsApi(api_client)
            symbols = symbols_api.get_trader_symbols()
            
            logger.info(f"Successfully retrieved {len(symbols)} symbols")
            return symbols
            
    except ApiException as e:
        APIErrorHandler.handle_api_exception(e, "symbol retrieval")
        return None
    except Exception as e:
        logger.error(f"Unexpected error retrieving symbols: {e}")
        return None


def validate_trading_parameters(symbol: str, volume: float, order_type: str) -> bool:
    """
    Validate trading parameters before placing orders.
    
    Args:
        symbol: Trading symbol
        volume: Order volume
        order_type: Type of order
        
    Returns:
        bool: True if parameters are valid
    """
    print("=== Validating Trading Parameters ===")
    
    # Basic validation
    if not symbol or not isinstance(symbol, str):
        logger.error("Invalid symbol")
        return False
    
    if volume <= 0:
        logger.error("Volume must be positive")
        return False
    
    valid_order_types = ["buy", "sell", "buy_limit", "sell_limit", "buy_stop", "sell_stop"]
    if order_type not in valid_order_types:
        logger.error(f"Invalid order type. Must be one of: {valid_order_types}")
        return False
    
    # Get symbol information for further validation
    try:
        with get_api_client() as api_client:
            symbols_api = openapi_client.SymbolsApi(api_client)
            symbols = symbols_api.get_trader_symbols()
            
            # Find the symbol
            symbol_info = next((s for s in symbols if s.name == symbol), None)
            
            if not symbol_info:
                logger.error(f"Symbol {symbol} not found")
                return False
            
            # Check volume limits
            if volume < symbol_info.volume_min:
                logger.error(f"Volume {volume} below minimum {symbol_info.volume_min}")
                return False
            
            if volume > symbol_info.volume_max:
                logger.error(f"Volume {volume} above maximum {symbol_info.volume_max}")
                return False
            
            # Check volume step
            if symbol_info.volume_step and (volume % symbol_info.volume_step) != 0:
                logger.error(f"Volume must be multiple of {symbol_info.volume_step}")
                return False
            
            logger.info("✓ Trading parameters validated successfully")
            return True
            
    except ApiException as e:
        APIErrorHandler.handle_api_exception(e, "parameter validation")
        return False
    except Exception as e:
        logger.error(f"Unexpected error during validation: {e}")
        return False


def handle_network_issues_example():
    """
    Example of handling network connectivity issues.
    """
    print("=== Network Issues Handling Example ===")
    
    max_attempts = 3
    base_delay = 2.0
    
    for attempt in range(max_attempts):
        try:
            # Test connectivity
            if test_api_connectivity():
                print("✓ Network connectivity restored")
                break
                
        except Exception as e:
            logger.warning(f"Network attempt {attempt + 1} failed: {e}")
            
            if attempt < max_attempts - 1:
                delay = base_delay * (2 ** attempt)  # Exponential backoff
                logger.info(f"Waiting {delay}s before next attempt...")
                time.sleep(delay)
            else:
                logger.error("All network connectivity attempts failed")
                return False
    
    return True


def graceful_shutdown_example():
    """
    Example of graceful shutdown handling.
    """
    print("=== Graceful Shutdown Example ===")
    
    try:
        # Check for open positions
        with get_api_client() as api_client:
            positions_api = openapi_client.PositionsApi(api_client)
            positions = positions_api.get_trader_positions()
            
            if positions:
                print(f"WARNING: {len(positions)} open positions detected")
                print("Consider closing positions before shutdown:")
                
                for pos in positions:
                    print(f"  Position {pos.id}: {pos.symbol} ({pos.type})")
                    print(f"    Volume: {pos.volume}, P&L: ${pos.profit:.2f}")
            
            # Check for pending orders
            orders_api = openapi_client.OrdersApi(api_client)
            orders = orders_api.get_trader_orders()
            
            if orders:
                print(f"WARNING: {len(orders)} pending orders detected")
                print("Consider canceling orders before shutdown:")
                
                for order in orders:
                    print(f"  Order {order.id}: {order.symbol} ({order.type})")
                    print(f"    Volume: {order.volume}, Price: {order.price}")
            
            if not positions and not orders:
                print("✓ No open positions or pending orders")
                print("✓ Safe to shutdown")
            
    except Exception as e:
        logger.error(f"Error during shutdown check: {e}")


def main():
    """Run error handling and best practices examples."""
    print("Omtrader SDK - Error Handling and Best Practices Examples")
    print("=" * 70)
    
    # Test API connectivity
    if not test_api_connectivity():
        print("❌ API connectivity test failed")
        return
    print()
    
    # Test robust API calls
    symbols = robust_get_symbols()
    if symbols:
        print(f"✓ Retrieved {len(symbols)} symbols")
    print()
    
    # Validate trading parameters
    validate_trading_parameters("EURUSD", 0.1, "buy")
    validate_trading_parameters("INVALID", -1.0, "invalid_type")  # This should fail
    print()
    
    # Network issues handling
    handle_network_issues_example()
    print()
    
    # Graceful shutdown
    graceful_shutdown_example()


if __name__ == "__main__":
    main() 