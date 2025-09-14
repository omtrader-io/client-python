"""
Deal History Examples

This module demonstrates how to use the DealsApi for:
- Getting deal history
- Getting specific deal details
- Filtering deals by date range
- Analyzing trading performance
"""

import openapi_client
from openapi_client.rest import ApiException
from examples.config import get_api_client, handle_api_exception
from datetime import datetime, timedelta
from pprint import pprint


@handle_api_exception
def get_all_deals(page=1, limit=50, sort_by="created_at", direction="desc"):
    """
    Example: Get all deals with pagination and sorting.
    
    Args:
        page (int): Page number
        limit (int): Number of deals per page
        sort_by (str): Field to sort by
        direction (str): Sort direction ("asc" or "desc")
        
    Returns:
        List[ModelDeal]: List of deals
    """
    print(f"=== Getting All Deals (Page {page}, Limit {limit}) ===")
    
    with get_api_client() as api_client:
        deals_api = openapi_client.DealsApi(api_client)
        
        try:
            deals = deals_api.get_trader_deals(
                page=page,
                limit=limit,
                sort_by=sort_by,
                dir=direction
            )
            
            # Get symbols list to map symbol_id to symbol name
            symbols_api = openapi_client.SymbolsApi(api_client)
            all_symbols = symbols_api.get_trader_symbols()
            symbol_map = {symbol.id: symbol.symbol for symbol in all_symbols}
            
            print(f"Found {len(deals)} deals:")
            for deal in deals:
                print(f"Deal ID: {deal.id}")
                symbol_name = symbol_map.get(deal.symbol_id, f"ID:{deal.symbol_id}")
                print(f"  Symbol: {symbol_name}")
                print(f"  Side: {deal.side}")
                print(f"  Volume: {deal.volume}")
                print(f"  Price: {deal.price}")
                print(f"  Profit: {deal.profit}")
                print(f"  Commission: {deal.commission}")
                print(f"  Time: {deal.created_at}")
                print("---")
            
            return deals
            
        except ApiException as e:
            print(f"Exception when calling DealsApi->get_trader_deals: {e}")
            raise


@handle_api_exception
def get_deal_details(deal_id):
    """
    Example: Get details for a specific deal.
    
    Args:
        deal_id (int): The deal ID
        
    Returns:
        ModelDeal: Deal details
    """
    print(f"=== Getting Deal Details for ID: {deal_id} ===")
    
    with get_api_client() as api_client:
        deals_api = openapi_client.DealsApi(api_client)
        
        try:
            deal = deals_api.get_trader_deal(deal_id)
            
            # Get symbols list to map symbol_id to symbol name
            symbols_api = openapi_client.SymbolsApi(api_client)
            all_symbols = symbols_api.get_trader_symbols()
            symbol_map = {symbol.id: symbol.symbol for symbol in all_symbols}
            
            print("Deal Details:")
            print(f"ID: {deal.id}")
            print(f"Order ID: {deal.order_id}")
            print(f"Position ID: {deal.position_id}")
            symbol_name = symbol_map.get(deal.symbol_id, f"ID:{deal.symbol_id}")
            print(f"Symbol: {symbol_name}")
            print(f"Side: {deal.side}")
            print(f"Direction: {deal.direction}")
            print(f"Volume: {deal.volume}")
            print(f"Price: {deal.price}")
            print(f"Profit: {deal.profit}")
            print(f"Commission: {deal.commission}")
            print(f"Swap: {deal.swap}")
            print(f"Time: {deal.created_at}")
            print(f"Comment: {deal.comment}")
            
            return deal
            
        except ApiException as e:
            print(f"Exception when calling DealsApi->get_trader_deal: {e}")
            raise


@handle_api_exception
def get_deals_by_date_range(from_date, to_date, limit=100):
    """
    Example: Get deals within a specific date range.
    
    Args:
        from_date (str): Start date in ISO format (YYYY-MM-DD)
        to_date (str): End date in ISO format (YYYY-MM-DD)
        limit (int): Maximum number of deals to retrieve
        
    Returns:
        List[ModelDeal]: Deals within the date range
    """
    print(f"=== Getting Deals from {from_date} to {to_date} ===")
    
    with get_api_client() as api_client:
        deals_api = openapi_client.DealsApi(api_client)
        
        try:
            deals = deals_api.get_trader_deals(
                var_from=from_date,
                to=to_date,
                limit=limit,
                sort_by="created_at",
                dir="desc"
            )
            
            # Get symbols list to map symbol_id to symbol name
            symbols_api = openapi_client.SymbolsApi(api_client)
            all_symbols = symbols_api.get_trader_symbols()
            symbol_map = {symbol.id: symbol.symbol for symbol in all_symbols}
            
            print(f"Found {len(deals)} deals in the specified date range:")
            for deal in deals:
                print(f"Deal ID: {deal.id}")
                symbol_name = symbol_map.get(deal.symbol_id, f"ID:{deal.symbol_id}")
                print(f"  Symbol: {symbol_name}")
                profit_value = deal.profit if deal.profit is not None else 0
                print(f"  Profit: ${profit_value:.2f}")
                print(f"  Time: {deal.created_at}")
                print("---")
            
            return deals
            
        except ApiException as e:
            print(f"Exception when calling DealsApi->get_trader_deals: {e}")
            raise


@handle_api_exception
def get_recent_deals(days=7):
    """
    Example: Get deals from the last N days.
    
    Args:
        days (int): Number of days to look back
        
    Returns:
        List[ModelDeal]: Recent deals
    """
    print(f"=== Getting Deals from Last {days} Days ===")
    
    # Calculate date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    from_date = start_date.strftime("%Y-%m-%d")
    to_date = end_date.strftime("%Y-%m-%d")
    
    return get_deals_by_date_range(from_date, to_date)


def analyze_trading_performance(deals):
    """
    Example: Analyze trading performance from deals.
    
    Args:
        deals (List[ModelDeal]): List of deals to analyze
        
    Returns:
        dict: Performance metrics
    """
    print("=== Trading Performance Analysis ===")
    
    if not deals:
        print("No deals to analyze")
        return {}
    
    # Calculate metrics
    total_deals = len(deals)
    profitable_deals = [deal for deal in deals if deal.profit and deal.profit > 0]
    losing_deals = [deal for deal in deals if deal.profit and deal.profit < 0]
    
    total_profit = sum(deal.profit for deal in deals if deal.profit)
    total_commission = sum(deal.commission for deal in deals if deal.commission)
    
    win_rate = (len(profitable_deals) / total_deals * 100) if total_deals > 0 else 0
    
    avg_win = sum(deal.profit for deal in profitable_deals) / len(profitable_deals) if profitable_deals else 0
    avg_loss = sum(deal.profit for deal in losing_deals) / len(losing_deals) if losing_deals else 0
    
    # Display results
    print(f"Total Deals: {total_deals}")
    print(f"Profitable Deals: {len(profitable_deals)}")
    print(f"Losing Deals: {len(losing_deals)}")
    print(f"Win Rate: {win_rate:.2f}%")
    print(f"Total Profit: ${total_profit:.2f}")
    print(f"Total Commission: ${total_commission:.2f}")
    print(f"Net Profit: ${total_profit - total_commission:.2f}")
    print(f"Average Win: ${avg_win:.2f}")
    print(f"Average Loss: ${avg_loss:.2f}")
    
    if avg_loss != 0:
        profit_factor = abs(avg_win / avg_loss)
        print(f"Profit Factor: {profit_factor:.2f}")
    
    # Symbol analysis - need to get symbol names
    try:
        with get_api_client() as api_client:
            symbols_api = openapi_client.SymbolsApi(api_client)
            all_symbols = symbols_api.get_trader_symbols()
            symbol_map = {symbol.id: symbol.symbol for symbol in all_symbols}
    except Exception as e:
        print(f"Warning: Could not load symbol names: {e}")
        symbol_map = {}
    
    symbol_stats = {}
    for deal in deals:
        symbol_name = symbol_map.get(deal.symbol_id, f"ID:{deal.symbol_id}")
        if symbol_name not in symbol_stats:
            symbol_stats[symbol_name] = {'count': 0, 'profit': 0}
        symbol_stats[symbol_name]['count'] += 1
        symbol_stats[symbol_name]['profit'] += deal.profit if deal.profit else 0
    
    print("\nPerformance by Symbol:")
    for symbol, stats in sorted(symbol_stats.items(), key=lambda x: x[1]['profit'], reverse=True):
        print(f"  {symbol}: {stats['count']} deals, ${stats['profit']:.2f} profit")
    
    return {
        'total_deals': total_deals,
        'win_rate': win_rate,
        'total_profit': total_profit,
        'net_profit': total_profit - total_commission,
        'symbol_stats': symbol_stats
    }


def get_best_performing_symbols(deals, top_n=5):
    """
    Example: Get the best performing trading symbols.
    
    Args:
        deals (List[ModelDeal]): List of deals
        top_n (int): Number of top symbols to return
        
    Returns:
        List[tuple]: Top performing symbols with profit
    """
    print(f"=== Top {top_n} Performing Symbols ===")
    
    # Get symbol names
    try:
        with get_api_client() as api_client:
            symbols_api = openapi_client.SymbolsApi(api_client)
            all_symbols = symbols_api.get_trader_symbols()
            symbol_map = {symbol.id: symbol.symbol for symbol in all_symbols}
    except Exception as e:
        print(f"Warning: Could not load symbol names: {e}")
        symbol_map = {}
    
    symbol_profits = {}
    for deal in deals:
        symbol_name = symbol_map.get(deal.symbol_id, f"ID:{deal.symbol_id}")
        profit = deal.profit if deal.profit else 0
        
        if symbol_name not in symbol_profits:
            symbol_profits[symbol_name] = 0
        symbol_profits[symbol_name] += profit
    
    # Sort by profit
    sorted_symbols = sorted(symbol_profits.items(), key=lambda x: x[1], reverse=True)
    top_symbols = sorted_symbols[:top_n]
    
    for i, (symbol, profit) in enumerate(top_symbols, 1):
        print(f"{i}. {symbol}: ${profit:.2f}")
    
    return top_symbols


def main():
    """Run deal history and analysis examples."""
    print("Omtrader SDK - Deal History and Analysis Examples")
    print("=" * 60)
    
    try:
        # Try simple deals call first (without date filters)
        print("1. Testing basic deals API call...")
        all_deals_page1 = get_all_deals(page=1, limit=10)
        print()
        
        if all_deals_page1:
            print("✅ Basic deals API works!")
            
            # Get details for the first deal
            first_deal = all_deals_page1[0]
            get_deal_details(first_deal.id)
            print()
            
            # Analyze performance
            performance = analyze_trading_performance(all_deals_page1)
            print()
            
            # Get best performing symbols
            top_symbols = get_best_performing_symbols(all_deals_page1)
            print()
            
            # Try date range if basic call works
            print("2. Testing date range filtering...")
            recent_deals = get_recent_deals(30)  # Last 30 days
            print()
        else:
            print("ℹ️  No deals found. This might be normal if no trades have been executed.")
            print("   Deals are created when orders are filled/executed.")
        
    except Exception as e:
        print(f"Error running examples: {e}")
        print("\nTroubleshooting tips:")
        print("- Check if any orders have been executed (deals are created from executed orders)")
        print("- Verify API credentials and permissions")
        print("- Try creating and executing an order first to generate deals")


if __name__ == "__main__":
    main() 