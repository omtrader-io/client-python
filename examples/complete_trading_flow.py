"""
Complete Trading Flow Examples

This module demonstrates end-to-end trading workflows:
- Complete trading session example
- Risk management examples
- Portfolio monitoring
- Automated trading strategies
"""

import openapi_client
from openapi_client.rest import ApiException
from examples.config import get_api_client, handle_api_exception
from examples.accounts import get_account_info
from examples.symbols import get_all_symbols, find_symbol_by_name
from examples.orders import create_market_order, get_all_orders
from examples.positions import get_all_positions, update_position
from examples.deals import get_recent_deals, analyze_trading_performance
import time


class TradingSession:
    """A complete trading session manager."""
    
    def __init__(self):
        self.api_client = get_api_client()
        self.accounts_api = openapi_client.AccountsApi(self.api_client)
        self.symbols_api = openapi_client.SymbolsApi(self.api_client)
        self.orders_api = openapi_client.OrdersApi(self.api_client)
        self.positions_api = openapi_client.PositionsApi(self.api_client)
        self.deals_api = openapi_client.DealsApi(self.api_client)
    
    @handle_api_exception
    def start_session(self):
        """Initialize a trading session with account and market data."""
        print("=== Starting Trading Session ===")
        
        # Get account information
        account = self.accounts_api.get_trader_account()
        print(f"Account Balance: ${account.balance}")
        print(f"Free Margin: ${account.free_margin}")
        print(f"Equity: ${account.equity}")
        
        # Get available symbols
        symbols = self.symbols_api.get_trader_symbols()
        print(f"Available Symbols: {len(symbols)}")
        
        return account, symbols
    
    @handle_api_exception
    def check_portfolio_status(self):
        """Check current portfolio status."""
        print("=== Portfolio Status ===")
        
        # Get current positions
        positions = self.positions_api.get_trader_positions()
        
        # Get pending orders
        orders = self.orders_api.get_trader_orders()
        
        # Calculate total P&L
        total_pnl = sum(pos.profit for pos in positions if pos.profit)
        
        print(f"Open Positions: {len(positions)}")
        print(f"Pending Orders: {len(orders)}")
        print(f"Total P&L: ${total_pnl:.2f}")
        
        return positions, orders, total_pnl
    
    @handle_api_exception
    def execute_trade_with_risk_management(self, symbol, volume, trade_type, 
                                         risk_percent=2.0, reward_ratio=2.0):
        """
        Execute a trade with proper risk management.
        
        Args:
            symbol (str): Trading symbol
            volume (float): Trade volume
            trade_type (str): "buy" or "sell"
            risk_percent (float): Risk percentage of account balance
            reward_ratio (float): Reward to risk ratio
        """
        print(f"=== Executing Trade with Risk Management ===")
        print(f"Symbol: {symbol}, Volume: {volume}, Type: {trade_type}")
        
        # Get account info for risk calculation
        account = self.accounts_api.get_trader_account()
        
        # Get symbol info for price calculation
        symbols = self.symbols_api.get_trader_symbols()
        symbol_info = next((s for s in symbols if s.name == symbol), None)
        
        if not symbol_info:
            print(f"Symbol {symbol} not found")
            return None
        
        # Calculate risk management levels
        account_balance = account.balance
        risk_amount = account_balance * (risk_percent / 100)
        
        current_price = symbol_info.ask if trade_type == "buy" else symbol_info.bid
        
        # Calculate stop loss and take profit (simplified calculation)
        if trade_type == "buy":
            stop_loss = current_price - (risk_amount / volume)
            take_profit = current_price + (risk_amount * reward_ratio / volume)
        else:
            stop_loss = current_price + (risk_amount / volume)
            take_profit = current_price - (risk_amount * reward_ratio / volume)
        
        print(f"Current Price: {current_price}")
        print(f"Stop Loss: {stop_loss}")
        print(f"Take Profit: {take_profit}")
        print(f"Risk Amount: ${risk_amount:.2f}")
        
        # Execute the trade (commented out for safety)
        # order_request = openapi_client.MessagingCrtOrder(
        #     symbol=symbol,
        #     volume=volume,
        #     type=trade_type,
        #     stop_loss=stop_loss,
        #     take_profit=take_profit
        # )
        # 
        # new_order = self.orders_api.create_trader_order(order_request)
        # print(f"Order created: ID {new_order.id}")
        # return new_order
        
        print("Trade execution commented out for safety")
        return None
    
    @handle_api_exception
    def monitor_positions(self, max_loss_percent=5.0):
        """
        Monitor positions and apply risk management.
        
        Args:
            max_loss_percent (float): Maximum loss percentage before action
        """
        print("=== Monitoring Positions ===")
        
        positions = self.positions_api.get_trader_positions()
        account = self.accounts_api.get_trader_account()
        
        for position in positions:
            if not position.profit:
                continue
                
            loss_percent = (position.profit / account.balance) * 100
            
            print(f"Position {position.id} ({position.symbol}):")
            print(f"  P&L: ${position.profit:.2f} ({loss_percent:.2f}%)")
            
            # Check if position needs attention
            if loss_percent < -max_loss_percent:
                print(f"  WARNING: Position exceeds max loss threshold!")
                # In a real scenario, you might close or adjust the position
                
            elif position.profit > 0:
                print(f"  Position is profitable")
                # Consider trailing stop or partial close
    
    def run_daily_analysis(self):
        """Run daily trading analysis."""
        print("=== Daily Trading Analysis ===")
        
        # Get recent deals
        recent_deals = self.deals_api.get_trader_deals(limit=100)
        
        if recent_deals:
            # Analyze performance
            performance = analyze_trading_performance(recent_deals)
            
            # Check if any adjustments needed
            if performance['win_rate'] < 50:
                print("WARNING: Win rate below 50%")
            
            if performance['net_profit'] < 0:
                print("WARNING: Net loss detected")
        
        return recent_deals


@handle_api_exception
def scalping_strategy_example():
    """
    Example of a scalping strategy workflow.
    
    Note: This is for educational purposes only.
    """
    print("=== Scalping Strategy Example ===")
    
    session = TradingSession()
    
    # Start session
    account, symbols = session.start_session()
    
    # Find a liquid symbol (e.g., EURUSD)
    eurusd = next((s for s in symbols if s.name == "EURUSD"), None)
    
    if not eurusd:
        print("EURUSD not available")
        return
    
    print(f"EURUSD Spread: {eurusd.spread}")
    print(f"Current Bid: {eurusd.bid}, Ask: {eurusd.ask}")
    
    # Check if spread is suitable for scalping
    if eurusd.spread > 3:  # 3 pips
        print("Spread too high for scalping")
        return
    
    # Simulate scalping conditions check
    print("Checking market conditions...")
    print("- Low spread: ✓")
    print("- High liquidity hours: ✓ (assumed)")
    print("- Volatility check: ✓ (assumed)")
    
    # In a real strategy, you would:
    # 1. Analyze recent price movements
    # 2. Check technical indicators
    # 3. Execute quick trades with tight stops
    # 4. Monitor and close positions quickly
    
    print("Scalping strategy conditions met (simulation)")


@handle_api_exception
def swing_trading_strategy_example():
    """
    Example of a swing trading strategy workflow.
    
    Note: This is for educational purposes only.
    """
    print("=== Swing Trading Strategy Example ===")
    
    session = TradingSession()
    
    # Start session
    account, symbols = session.start_session()
    
    # Check current portfolio
    positions, orders, total_pnl = session.check_portfolio_status()
    
    # Risk management check
    max_positions = 5
    if len(positions) >= max_positions:
        print(f"Maximum positions ({max_positions}) reached")
        return
    
    # Find symbols suitable for swing trading
    major_pairs = ["EURUSD", "GBPUSD", "USDJPY", "USDCHF"]
    available_pairs = [s for s in symbols if s.name in major_pairs]
    
    print(f"Available major pairs: {[s.name for s in available_pairs]}")
    
    # In a real strategy, you would:
    # 1. Analyze daily/4H charts
    # 2. Look for trend reversals or continuations
    # 3. Set wider stops and targets
    # 4. Hold positions for days/weeks
    
    for pair in available_pairs[:2]:  # Check first 2 pairs
        print(f"\nAnalyzing {pair.name}:")
        print(f"  Current Price: {pair.bid}")
        print(f"  Daily Range: {pair.ask - pair.bid} pips (simplified)")
        # Here you would add technical analysis
        print("  Technical analysis: Pending implementation")


def portfolio_rebalancing_example():
    """
    Example of portfolio rebalancing workflow.
    """
    print("=== Portfolio Rebalancing Example ===")
    
    session = TradingSession()
    
    # Get current positions
    positions, orders, total_pnl = session.check_portfolio_status()
    
    # Analyze position allocation
    symbol_allocation = {}
    total_volume = sum(pos.volume for pos in positions)
    
    for position in positions:
        symbol = position.symbol
        if symbol not in symbol_allocation:
            symbol_allocation[symbol] = 0
        symbol_allocation[symbol] += position.volume
    
    print("Current Allocation:")
    for symbol, volume in symbol_allocation.items():
        percentage = (volume / total_volume * 100) if total_volume > 0 else 0
        print(f"  {symbol}: {volume} lots ({percentage:.1f}%)")
    
    # Check for over-concentration
    max_allocation_percent = 30.0
    for symbol, volume in symbol_allocation.items():
        percentage = (volume / total_volume * 100) if total_volume > 0 else 0
        if percentage > max_allocation_percent:
            print(f"WARNING: {symbol} over-allocated at {percentage:.1f}%")


def main():
    """Run complete trading flow examples."""
    print("Omtrader SDK - Complete Trading Flow Examples")
    print("=" * 60)
    
    try:
        # Basic session management
        session = TradingSession()
        account, symbols = session.start_session()
        print()
        
        # Portfolio monitoring
        session.monitor_positions()
        print()
        
        # Daily analysis
        session.run_daily_analysis()
        print()
        
        # Strategy examples
        scalping_strategy_example()
        print()
        
        swing_trading_strategy_example()
        print()
        
        # Portfolio management
        portfolio_rebalancing_example()
        
    except Exception as e:
        print(f"Error running examples: {e}")


if __name__ == "__main__":
    main()
