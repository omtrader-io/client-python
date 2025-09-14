"""
Position Management Examples

This module demonstrates how to use the PositionsApi for:
- Getting current positions
- Getting specific position details
- Updating positions (stop loss, take profit)
- Closing positions
- Getting position history
"""

import openapi_client
from openapi_client.rest import ApiException
from examples.config import get_api_client, handle_api_exception
from pprint import pprint


@handle_api_exception
def get_all_positions():
    """
    Example: Get all current open positions.
    
    Returns:
        List[ModelPosition]: List of current positions
    """
    print("=== Getting All Current Positions ===")
    
    with get_api_client() as api_client:
        positions_api = openapi_client.PositionsApi(api_client)
        
        try:
            positions = positions_api.get_trader_positions()
            
            print(f"Found {len(positions)} open positions:")
            for position in positions:
                print(f"Position ID: {position.id}")
                print(f"  Symbol: {position.symbol}")
                side_text = "Buy" if position.side == 0 else "Sell" if position.side == 1 else f"Side {position.side}"
                print(f"  Type: {side_text}")
                print(f"  Volume: {position.volume_current}")
                print(f"  Open Price: {position.price_open}")
                print(f"  Current Price: {position.price_current}")
                print(f"  Stop Loss: {position.price_sl}")
                print(f"  Take Profit: {position.price_tp}")
                print(f"  Status: {position.status}")
                print("---")
            
            return positions
            
        except ApiException as e:
            print(f"Exception when calling PositionsApi->get_trader_positions: {e}")
            raise


@handle_api_exception
def get_position_details(position_id):
    """
    Example: Get details for a specific position.
    
    Args:
        position_id (int): The position ID
        
    Returns:
        ModelPosition: Position details
    """
    print(f"=== Getting Position Details for ID: {position_id} ===")
    
    with get_api_client() as api_client:
        positions_api = openapi_client.PositionsApi(api_client)
        
        try:
            position = positions_api.get_trader_position(position_id)
            
            print("Position Details:")
            print(f"ID: {position.id}")
            print(f"Symbol: {position.symbol}")
            side_text = "Buy" if position.side == 0 else "Sell" if position.side == 1 else f"Side {position.side}"
            print(f"Type: {side_text}")
            print(f"Volume: {position.volume_current}")
            print(f"Open Price: {position.price_open}")
            print(f"Current Price: {position.price_current}")
            print(f"Stop Loss: {position.price_sl}")
            print(f"Take Profit: {position.price_tp}")
            print(f"Commission: {position.commission}")
            print(f"Swap: {position.swaps}")
            print(f"Status: {position.status}")
            print(f"Opened At: {position.created_at}")
            
            return position
            
        except ApiException as e:
            print(f"Exception when calling PositionsApi->get_trader_position: {e}")
            raise


@handle_api_exception
def update_position(position_id, new_stop_loss=None, new_take_profit=None):
    """
    Example: Update position stop loss and/or take profit levels.
    
    Args:
        position_id (int): Position ID to update
        new_stop_loss (float, optional): New stop loss price
        new_take_profit (float, optional): New take profit price
        
    Returns:
        ModelPosition: Updated position
    """
    print(f"=== Updating Position ID: {position_id} ===")
    
    with get_api_client() as api_client:
        positions_api = openapi_client.PositionsApi(api_client)
        
        try:
            # First get the current position to extract required fields
            current_position = positions_api.get_trader_position(position_id)
            
            # Get account info to get user_id
            accounts_api = openapi_client.AccountsApi(api_client)
            account_info = accounts_api.get_trader_account()
            
            # Create update request with all required fields
            update_request = openapi_client.MessagingUptPosition(
                account_id=current_position.account_id,
                id=position_id,
                user_id=account_info.user_id,
                price_sl=new_stop_loss,
                price_tp=new_take_profit
            )
            
            # Update the position
            try:
                updated_position = positions_api.update_trader_position(position_id, update_request)
                print("Position Updated Successfully:")
                print(f"Position ID: {updated_position.id}")
                print(f"New Stop Loss: {updated_position.price_sl}")
                print(f"New Take Profit: {updated_position.price_tp}")
                return updated_position
            except Exception as parse_error:
                # Handle case where API returns string instead of object
                if "Position #" in str(parse_error) and "sent to the system" in str(parse_error):
                    print("Position Updated Successfully!")
                    print(f"API Response: Position #{position_id} has been sent to the system")
                    return "Position updated successfully"
                else:
                    raise parse_error
            
        except ApiException as e:
            print(f"Exception when calling PositionsApi->update_trader_position: {e}")
            raise


@handle_api_exception
def close_position(position_id, volume=None, reason="Manual close"):
    """
    Example: Close a position partially or completely.
    
    Args:
        position_id (int): Position ID to close
        volume (float, optional): Volume to close (None for complete close)
        reason (str): Reason for closing
        
    Returns:
        str: Close confirmation
    """
    print(f"=== Closing Position ID: {position_id} ===")
    
    with get_api_client() as api_client:
        positions_api = openapi_client.PositionsApi(api_client)
        
        try:
            # First get the current position to extract required fields
            current_position = positions_api.get_trader_position(position_id)
            
            # Get account info to get user_id
            accounts_api = openapi_client.AccountsApi(api_client)
            account_info = accounts_api.get_trader_account()
            
            # Use the position's current volume if no specific volume provided
            close_volume = volume if volume is not None else current_position.volume_current
            
            # Create close request with all required fields
            close_request = openapi_client.MessagingClosePosition(
                account_id=current_position.account_id,
                id=position_id,
                user_id=account_info.user_id,
                volume=close_volume
            )
            
            # Close the position
            try:
                result = positions_api.close_trader_position(position_id, close_request)
                close_type = "partially" if volume else "completely"
                print(f"Position {position_id} closed {close_type}")
                print(f"Result: {result}")
                return result
            except Exception as parse_error:
                # Handle case where API returns string instead of object
                if "Position #" in str(parse_error) and "sent to the system" in str(parse_error):
                    close_type = "partially" if volume else "completely"
                    print(f"Position {position_id} closed {close_type}!")
                    print(f"API Response: Position #{position_id} has been sent to the system")
                    return "Position closed successfully"
                else:
                    raise parse_error
            
        except ApiException as e:
            print(f"Exception when calling PositionsApi->close_trader_position: {e}")
            raise


@handle_api_exception
def get_position_history():
    """
    Example: Get historical positions.
    
    Returns:
        List[ModelPosition]: Historical positions
    """
    print("=== Getting Position History ===")
    
    with get_api_client() as api_client:
        positions_api = openapi_client.PositionsApi(api_client)
        
        try:
            position_history = positions_api.get_trader_positions_history()
            
            print(f"Found {len(position_history)} historical positions:")
            for position in position_history[:10]:  # Show first 10
                print(f"Position ID: {position.id}")
                print(f"  Symbol: {position.symbol}")
                side_text = "Buy" if position.side == 0 else "Sell" if position.side == 1 else f"Side {position.side}"
                print(f"  Type: {side_text}")
                print(f"  Volume: {position.volume_current}")
                print(f"  Open Price: {position.price_open}")
                print(f"  Current Price: {position.price_current}")
                print(f"  Stop Loss: {position.price_sl}")
                print(f"  Take Profit: {position.price_tp}")
                print(f"  Profit/Loss: {position.profit}")
                print(f"  Opened At: {position.created_at}")
                print(f"  Closed At: {position.updated_at}")
                print("---")
            
            return position_history
            
        except ApiException as e:
            print(f"Exception when calling PositionsApi->get_trader_positions_history: {e}")
            raise


@handle_api_exception
def get_profitable_positions():
    """
    Example: Filter and display only profitable positions.
    
    Returns:
        List[ModelPosition]: Profitable positions
    """
    print("=== Getting Profitable Positions ===")
    
    positions = get_all_positions()
    profitable_positions = [pos for pos in positions if pos.profit and pos.profit > 0]
    
    print(f"Found {len(profitable_positions)} profitable positions:")
    for position in profitable_positions:
        print(f"Position ID: {position.id}")
        print(f"  Symbol: {position.symbol}")
        print(f"  Profit: ${position.profit:.2f}")
        print("---")
    
    return profitable_positions


@handle_api_exception
def get_losing_positions():
    """
    Example: Filter and display losing positions.
    
    Returns:
        List[ModelPosition]: Losing positions
    """
    print("=== Getting Losing Positions ===")
    
    positions = get_all_positions()
    losing_positions = [pos for pos in positions if pos.profit and pos.profit < 0]
    
    print(f"Found {len(losing_positions)} losing positions:")
    for position in losing_positions:
        print(f"Position ID: {position.id}")
        print(f"  Symbol: {position.symbol}")
        print(f"  Loss: ${position.profit:.2f}")
        print("---")
    
    return losing_positions


def calculate_total_pnl(positions):
    """
    Helper function to calculate total profit/loss.
    
    Args:
        positions (List[ModelPosition]): List of positions
        
    Returns:
        float: Total P&L
    """
    total_pnl = sum(pos.profit for pos in positions if pos.profit)
    return total_pnl


def main():
    """
    Interactive test of all Position APIs with hardcoded values for mock account testing.
    
    Tests all position APIs with pauses between each test:
    1. Get all positions
    2. Get specific position details  
    3. Update position (stop loss/take profit)
    4. Close position
    5. Get positions history
    """
    print("Position API Testing - Interactive Mode")
    print("=" * 40)
    print("Press Enter after each test to continue to the next one...")
    
    try:
        # Test 1: Get all current positions
        print("\n1. Testing get_all_positions()...")
        positions = get_all_positions()
        
        if not positions:
            print("No open positions found. Testing with history...")
            input("\nPress Enter to continue to history test...")
            history = get_position_history()
            if history:
                print(f"Found {len(history)} historical positions")
            else:
                print("No historical positions found either.")
            return
        
        print(f"Found {len(positions)} open positions")
        input("\nPress Enter to continue to next test...")
        
        # Test 2: Get specific position details
        print("\n2. Testing get_position_details()...")
        first_position = positions[0]
        get_position_details(first_position.id)
        input("\nPress Enter to continue to next test...")
        
        # Test 3: Update position with hardcoded values
        print("\n3. Testing update_position()...")
        print("⚠️  This will modify the position with:")
        print("   Stop Loss: 1.1000")
        print("   Take Profit: 0.80963")
        user_input = input("\nContinue with update test? (y/N): ").strip().lower()
        
        if user_input == 'y':
            try:
                updated_position = update_position(
                    first_position.id, 
                    new_stop_loss=0.80020, 
                    new_take_profit=0.80070
                )
                print("Position update test completed")
            except Exception as e:
                print(f"Update test result: {e}")
        else:
            print("Update test skipped")
        
        input("\nPress Enter to continue to next test...")
        
        # Test 4: Close position
        print("\n4. Testing close_position()...")
        position_to_close = positions[-1] if len(positions) > 1 else positions[0]
        print(f"⚠️  This will close position ID: {position_to_close.id}")
        print(f"   Symbol: {position_to_close.symbol}")
        print(f"   Volume: {position_to_close.volume_current}")
        
        user_input = input("\nContinue with close test? (y/N): ").strip().lower()
        
        if user_input == 'y':
            try:
                close_result = close_position(
                    position_to_close.id, 
                    reason="API Test"
                )
                print("Position close test completed")
            except Exception as e:
                print(f"Close test result: {e}")
        else:
            print("Close test skipped")
        
        input("\nPress Enter to continue to final test...")
        
        # Test 5: Get positions history
        print("\n5. Testing get_position_history()...")
        history = get_position_history()
        print(f"Found {len(history) if history else 0} historical positions")
        
        print("\n✅ All Position API tests completed!")
        
    except Exception as e:
        print(f"Error during testing: {e}")


if __name__ == "__main__":
    main() 