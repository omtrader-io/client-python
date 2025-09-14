"""
Symbol and Market Data Examples

This module demonstrates how to use the SymbolsApi for:
- Getting available trading symbols
- Getting specific symbol information
- Getting historical tick data
"""

import openapi_client
from openapi_client.rest import ApiException
from examples.config import get_api_client, handle_api_exception


@handle_api_exception
def get_all_symbols():
    """
    Example: Get all available trading symbols.
    
    Returns:
        List[MessagingViewSymbol]: List of available symbols
    """
    print("=== Getting All Available Symbols ===")
    
    with get_api_client() as api_client:
        symbols_api = openapi_client.SymbolsApi(api_client)
        
        # Get all symbols
        symbols = symbols_api.get_trader_symbols()
        print(f"Retrieved {len(symbols)} symbols")
        
        # Display first few symbols
        for i, symbol in enumerate(symbols[:10]):
            print(f"{i+1}. {symbol.symbol} (ID: {symbol.id}) - {symbol.desc}")
            if symbol.spread is not None:
                print(f"   Spread: {symbol.spread}, Digits: {symbol.digits}")
            if symbol.last_bid is not None and symbol.last_ask is not None:
                print(f"   Last Bid: {symbol.last_bid}, Last Ask: {symbol.last_ask}")
        
        if len(symbols) > 10:
            print(f"... and {len(symbols) - 10} more symbols")
        
        return symbols


@handle_api_exception
def get_symbol_details(symbol_id):
    """
    Example: Get detailed information for a specific symbol.
    
    Args:
        symbol_id (int): The symbol ID to get details for
        
    Returns:
        MessagingViewSymbol: Symbol details
    """
    print(f"=== Getting Symbol Details for ID: {symbol_id} ===")
    
    with get_api_client() as api_client:
        symbols_api = openapi_client.SymbolsApi(api_client)
        
        # Get specific symbol details
        symbol = symbols_api.get_trader_symbol(symbol_id)
        
        print("Symbol Details:")
        print(f"ID: {symbol.id}")
        print(f"Symbol: {symbol.symbol}")
        print(f"Description: {symbol.desc}")
        print(f"Base Currency: {symbol.base_currency}")
        print(f"Quote Currency: {symbol.quote_currency}")
        print(f"Digits: {symbol.digits}")
        print(f"Contract Size: {symbol.contract_size}")
        print(f"Min Volume: {symbol.min_value}")
        print(f"Max Volume: {symbol.max_value}")
        print(f"Volume Step: {symbol.step}")
        print(f"Enabled: {symbol.enabled}")
        
        # Market data
        if symbol.last_bid is not None and symbol.last_ask is not None:
            print(f"Last Bid: {symbol.last_bid}")
            print(f"Last Ask: {symbol.last_ask}")
            print(f"Spread: {symbol.spread}")
        
        # Trading conditions
        if symbol.margin_buy is not None:
            print(f"Margin Buy: {symbol.margin_buy}")
            print(f"Margin Sell: {symbol.margin_sell}")
        
        return symbol


@handle_api_exception
def get_symbol_tick_history(symbol_id, symbol_id_param, var_from, to, resolution, count_back, tick_type=None):
    """
    Example: Get historical bar/candlestick data for a symbol.
    
    Args:
        symbol_id (int): The symbol ID (path parameter)
        symbol_id_param (int): The symbol ID (query parameter)
        var_from (int): From timestamp
        to (int): To timestamp
        resolution (str): Resolution (e.g., "1m", "1h", "1d")
        count_back (int): Number of bars to retrieve
        tick_type (str, optional): Type of data ("bid" or "ask")
        
    Returns:
        List[MessagingHistoryTick]: Historical OHLCV bar data
    """
    print(f"=== Getting Historical Bar Data for Symbol ID: {symbol_id} ===")
    
    with get_api_client() as api_client:
        symbols_api = openapi_client.SymbolsApi(api_client)
        
        # Get tick history
        ticks = symbols_api.get_trader_symbol_ticks_history(
            id=symbol_id,
            symbol_id=symbol_id_param,
            var_from=var_from,
            to=to,
            resolution=resolution,
            count_back=count_back,
            type=tick_type
        )
        
        print(f"Retrieved {len(ticks)} historical bars:")
        for i, tick in enumerate(ticks[:5]):  # Show first 5
            print(f"{i+1}. Time: {tick.time}, Open: {tick.open}, High: {tick.high}, Low: {tick.low}, Close: {tick.close}, Volume: {tick.volume}")
        
        if len(ticks) > 5:
            print(f"... and {len(ticks) - 5} more bars")
        
        return ticks


@handle_api_exception
def find_symbol_by_name(symbol_name):
    """
    Example: Find a symbol by name from the available symbols.
    
    Args:
        symbol_name (str): Name of the symbol to find (e.g., "EURUSD")
        
    Returns:
        MessagingViewSymbol: The found symbol, or None if not found
    """
    print(f"=== Finding Symbol: {symbol_name} ===")
    
    with get_api_client() as api_client:
        symbols_api = openapi_client.SymbolsApi(api_client)
        
        # Get all symbols
        symbols = symbols_api.get_trader_symbols()
        print(f"Searching through {len(symbols)} symbols...")
        
        # Search for the symbol
        for symbol in symbols:
            if symbol.symbol and symbol.symbol.upper() == symbol_name.upper():
                print(f"Found symbol: {symbol.symbol} (ID: {symbol.id})")
                return symbol
        
        print(f"Symbol {symbol_name} not found")
        return None


def main():
    """Run comprehensive symbol and market data tests."""
    print("Omtrader SDK - Symbol and Market Data API Tests")
    print("=" * 60)
    
    try:
        # Test 1: Get all available symbols
        print("\n1. Testing get_all_symbols()...")
        symbols = get_all_symbols()
        
        if not symbols:
            print("❌ No symbols returned from API")
            return
        
        input("\nPress Enter to continue to next test...")
        
        # Test 2: Get symbol details
        print("\n2. Testing get_symbol_details()...")
        first_symbol = symbols[0]
        print(f"Testing with symbol: {first_symbol.symbol} (ID: {first_symbol.id})")
        
        symbol_details = get_symbol_details(first_symbol.id)
        
        input("\nPress Enter to continue to next test...")
        
        # Test 3: Find symbol by name
        print("\n3. Testing find_symbol_by_name()...")
        test_symbols = ["EURUSD", "GBPUSD", "USDCHF", "USDJPY"]
        
        found_symbol = None
        for symbol_name in test_symbols:
            print(f"\nSearching for {symbol_name}...")
            found_symbol = find_symbol_by_name(symbol_name)
            if found_symbol:
                print(f"✅ Found {symbol_name} with ID: {found_symbol.id}")
                break
            else:
                print(f"❌ {symbol_name} not found")
        
        input("\nPress Enter to continue to next test...")
        
        # Test 4: Get historical bar data (requires specific parameters)
        print("\n4. Testing get_symbol_tick_history() - Historical Bar Data...")
        print("⚠️  This test requires specific timestamp and resolution parameters")
        print("⚠️  It may not work on all account types or without proper parameters")
        
        user_input = input("Continue with historical bar data test? (y/N): ").strip().lower()
        
        if user_input == 'y':
            if found_symbol:
                try:
                    # Example parameters - these would need to be adjusted for real use
                    import time
                    current_time = int(time.time())
                    from_time = current_time - 3600  # 1 hour ago
                    
                    print(f"Getting historical bar data for symbol: {found_symbol.symbol} (ID: {found_symbol.id})")
                    print("Using example parameters - may need adjustment for your specific use case")
                    
                    bar_history = get_symbol_tick_history(
                        symbol_id=found_symbol.id,
                        symbol_id_param=found_symbol.id,
                        var_from=from_time,
                        to=current_time,
                        resolution="1m",
                        count_back=10
                    )
                    
                except Exception as e:
                    print(f"Historical bar data test failed: {e}")
                    print("This is often expected - historical data may require specific account permissions")
            else:
                print("No symbol found for historical bar data test")
        else:
            print("Historical bar data test skipped")
        
        print("\n✅ All Symbol API tests completed!")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        raise


if __name__ == "__main__":
    main()