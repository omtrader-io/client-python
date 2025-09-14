"""
Order Management Examples

This module demonstrates how to use the OrdersApi for:
- Creating new orders
- Getting order information
- Updating orders
- Canceling orders
- Getting order history
- Order approval workflow
"""

import openapi_client
from openapi_client.rest import ApiException
from examples.config import get_api_client, handle_api_exception
from pprint import pprint


def find_symbol_by_name(symbol_name, api_client):
    """
    Helper function to find symbol_id by symbol name.
    
    Args:
        symbol_name (str): Symbol name (e.g., "EURUSD")
        api_client: API client instance
        
    Returns:
        int: Symbol ID
        
    Raises:
        Exception: If symbol not found or API call fails
    """
    symbols_api = openapi_client.SymbolsApi(api_client)
    
    # Get symbols using the API
    symbols = symbols_api.get_trader_symbols()
    
    # Handle both cases: list of objects or list of dicts
    for symbol in symbols:
        symbol_name_attr = None
        symbol_id_attr = None
        
        if hasattr(symbol, 'symbol'):
            # It's a proper MessagingViewSymbol object
            symbol_name_attr = symbol.symbol
            symbol_id_attr = symbol.id
        elif isinstance(symbol, dict):
            # It's a dictionary
            symbol_name_attr = symbol.get('symbol') or symbol.get('name')
            symbol_id_attr = symbol.get('id')
        
        if symbol_name_attr and symbol_name_attr.upper() == symbol_name.upper():
            return symbol_id_attr
            
    raise Exception(f"Symbol '{symbol_name}' not found")


@handle_api_exception
def get_all_orders():
    """
    Example: Get all current orders.
    
    Returns:
        List[ModelOrder]: List of current orders
    """
    print("=== Getting All Current Orders ===")
    
    with get_api_client() as api_client:
        orders_api = openapi_client.OrdersApi(api_client)
        
        try:
            orders = orders_api.get_trader_orders()
            
            print(f"Found {len(orders)} orders:")
            for order in orders:
                print(f"Order ID: {order.id}")
                symbol_name = order.symbol.name if hasattr(order.symbol, 'name') and order.symbol else order.symbol
                print(f"  Symbol: {symbol_name}")
                print(f"  Type: {order.type}")
                print(f"  Volume: {order.volume_current or order.volume_initial}")
                print(f"  Price: {order.price_order}")
                print(f"  Status: {order.status}")
                print(f"  Created: {order.created_at}")
                print("---")
            
            return orders
            
        except ApiException as e:
            print(f"Exception when calling OrdersApi->get_trader_orders: {e}")
            raise


@handle_api_exception
def get_order_details(order_id):
    """
    Example: Get details for a specific order.
    
    Args:
        order_id (int): The order ID
        
    Returns:
        ModelOrder: Order details
    """
    print(f"=== Getting Order Details for ID: {order_id} ===")
    
    with get_api_client() as api_client:
        orders_api = openapi_client.OrdersApi(api_client)
        
        try:
            order = orders_api.get_trader_order(order_id)
            
            print("Order Details:")
            print(f"ID: {order.id}")
            symbol_name = order.symbol.name if hasattr(order.symbol, 'name') and order.symbol else order.symbol
            print(f"Symbol: {symbol_name}")
            print(f"Type: {order.type}")
            print(f"Volume Current: {order.volume_current}")
            print(f"Volume Initial: {order.volume_initial}")
            print(f"Price: {order.price_order}")
            print(f"Stop Loss: {order.price_sl}")
            print(f"Take Profit: {order.price_tp}")
            print(f"Status: {order.status}")
            print(f"Created: {order.created_at}")
            print(f"Updated: {order.updated_at}")
            
            return order
            
        except ApiException as e:
            print(f"Exception when calling OrdersApi->get_trader_order: {e}")
            raise


@handle_api_exception
def create_market_order(symbol_name, volume, side_type, stop_loss=None, take_profit=None):
    """
    Example: Create a new market order.
    
    Args:
        symbol_name (str): Trading symbol (e.g., "EURUSD")
        volume (float): Order volume
        side_type (int): Order side (0=Buy, 1=Sell)
        stop_loss (float, optional): Stop loss price
        take_profit (float, optional): Take profit price
        
    Returns:
        ModelOrder: Created order
    """
    print(f"=== Creating Market Order ===")
    print(f"Symbol: {symbol_name}, Volume: {volume}, Side: {side_type}")
    
    with get_api_client() as api_client:
        orders_api = openapi_client.OrdersApi(api_client)
        
        try:
            # Get account info for required fields
            accounts_api = openapi_client.AccountsApi(api_client)
            account_info = accounts_api.get_trader_account()
            
            print(f"Account info: ID={account_info.id}, User_ID={account_info.user_id}")
            
            # Find symbol_id by name
            symbol_id = find_symbol_by_name(symbol_name, api_client)
            
            print(f"Using symbol_id: {symbol_id}")
            
            # Get current market price from symbols list (individual symbol call returns zeros)
            symbols_api = openapi_client.SymbolsApi(api_client)
            all_symbols = symbols_api.get_trader_symbols()
            
            # Find our symbol in the list to get current prices
            symbol_details = None
            for symbol in all_symbols:
                if symbol.id == symbol_id:
                    symbol_details = symbol
                    break
            
            if not symbol_details:
                raise Exception(f"Symbol with ID {symbol_id} not found in symbols list")
            
            # Use bid price for sell orders, ask price for buy orders
            if side_type == 1:  # Sell
                market_price = float(symbol_details.last_bid)
            else:  # Buy
                market_price = float(symbol_details.last_ask)
                
            print(f"Current market price: {market_price}")
            
            # Try creating the order request with minimal required fields first
            try:
                print("Creating order request object...")
                order_request = openapi_client.MessagingCrtOrder(
                    account_id=account_info.id,
                    user_id=account_info.user_id,
                    symbol_id=symbol_id,
                    volume=volume,
                    order_price=market_price  # Use actual market price
                )
                print("Basic order request created successfully")
                
                # Add optional fields
                if side_type is not None:
                    order_request.side = openapi_client.ModelSideType(side_type)
                    print(f"Added side: {side_type}")
                
                order_request.type = openapi_client.ModelOrderType.OrderType_market_order
                print("Added type: market order")
                
                if stop_loss is not None:
                    order_request.price_sl = stop_loss
                    print(f"Added stop_loss: {stop_loss}")
                
                if take_profit is not None:
                    order_request.price_tp = take_profit
                    print(f"Added take_profit: {take_profit}")
                
                print("Order request object completed")
                
            except Exception as model_error:
                print(f"Error creating order request object: {model_error}")
                raise
            
            # Create the order
            print("Sending order to API...")
            response = orders_api.create_trader_order(order_request)
            
            if response.success:
                print("Order Created Successfully:")
                print(f"Message: {response.data}")
                return response
            else:
                # API returned an error
                error_msg = response.error or "Order creation failed"
                if response.message:
                    error_msg += f": {response.message}"
                print(f"Order Creation Failed: {error_msg}")
                raise Exception(error_msg)
            
        except ApiException as e:
            print(f"Exception when calling OrdersApi->create_trader_order: {e}")
            raise


@handle_api_exception
def create_pending_order(symbol_name, volume, side_type, order_price, stop_loss=None, take_profit=None):
    """
    Create a pending order (stays in orders list until executed or cancelled)
    
    Args:
        symbol_name (str): Symbol name (e.g., "EURUSD")
        volume (float): Order volume
        side_type (int): 0 for Buy, 1 for Sell
        order_price (float): Specific price for the order (different from market price)
        stop_loss (float, optional): Stop loss price
        take_profit (float, optional): Take profit price
    
    Returns:
        str: Success message or raises exception
    """
    print("=== Creating Pending Order ===")
    print(f"Symbol: {symbol_name}, Volume: {volume}, Side: {side_type}, Price: {order_price}")
    
    with get_api_client() as api_client:
        try:
            # Get account information for required fields
            accounts_api = openapi_client.AccountsApi(api_client)
            account_info = accounts_api.get_trader_account()
            print(f"Account info: ID={account_info.id}, User_ID={account_info.user_id}")
            
            # Find symbol ID
            symbol_id = find_symbol_by_name(symbol_name, api_client)
            print(f"Using symbol_id: {symbol_id}")
            
            orders_api = openapi_client.OrdersApi(api_client)
            
            print("Creating pending order request object...")
            
            # Create the order request
            order_request = openapi_client.MessagingCrtOrder(
                account_id=account_info.id,
                user_id=account_info.user_id,
                symbol_id=symbol_id,
                volume=volume,
                order_price=order_price
            )
            
            print("Basic order request created successfully")
            
            # Set side and type as enum objects
            order_request.side = openapi_client.ModelSideType(side_type)
            print(f"Added side: {side_type}")
            
            # Use pending order type (limit order) - choose based on side
            if side_type == 0:  # Buy
                order_request.type = openapi_client.ModelOrderType.OrderType_buy_limit
                print("Added type: buy limit order (pending)")
            else:  # Sell
                order_request.type = openapi_client.ModelOrderType.OrderType_sell_limit
                print("Added type: sell limit order (pending)")
            
            # Add optional SL/TP
            if stop_loss is not None:
                order_request.price_sl = stop_loss
                print(f"Added stop_loss: {stop_loss}")
            
            if take_profit is not None:
                order_request.price_tp = take_profit
                print(f"Added take_profit: {take_profit}")
            
            print("Order request object completed")
            
            # Create the order
            print("Sending pending order to API...")
            print("DEBUG: About to call create_trader_order")
            
            try:
                response = orders_api.create_trader_order(order_request)
                print("DEBUG: API call completed successfully")
                print(f"DEBUG: Response type: {type(response)}")
                
                if response.success:
                    print("Pending Order Created Successfully:")
                    print(f"Message: {response.data}")
                    return response
                else:
                    # API returned an error
                    error_msg = response.error or "Pending order creation failed"
                    if response.message:
                        error_msg += f": {response.message}"
                    print(f"Pending Order Creation Failed: {error_msg}")
                    raise Exception(error_msg)
                    
            except Exception as api_error:
                print(f"DEBUG: Exception caught in example: {type(api_error)}")
                print(f"DEBUG: Exception message: {str(api_error)}")
                raise
                    
        except ApiException as e:
            print(f"Exception when calling OrdersApi->create_trader_order: {e}")
            raise


@handle_api_exception
def update_order(order_id, new_price=None, new_stop_loss=None, new_take_profit=None, new_volume=None):
    """
    Example: Update an existing order.
    
    Args:
        order_id (int): Order ID to update
        new_price (float, optional): New entry price
        new_stop_loss (float, optional): New stop loss
        new_take_profit (float, optional): New take profit
        new_volume (float, optional): New volume
        
    Returns:
        ModelOrder: Updated order
    """
    print(f"=== Updating Order ID: {order_id} ===")
    
    with get_api_client() as api_client:
        orders_api = openapi_client.OrdersApi(api_client)
        
        try:
            # Get current order details and account info for required fields
            current_order = orders_api.get_trader_order(order_id)
            accounts_api = openapi_client.AccountsApi(api_client)
            account_info = accounts_api.get_trader_account()
            
            # Create update request with all required fields
            update_request = openapi_client.MessagingUptOrder(
                account_id=account_info.id,
                id=order_id,
                user_id=account_info.user_id,
                order_price=new_price if new_price is not None else current_order.price_order,
                volume=new_volume if new_volume is not None else (current_order.volume_current or current_order.volume_initial),
                price_sl=new_stop_loss,
                price_tp=new_take_profit
            )
            
            # Update the order
            updated_order = orders_api.update_trader_order(order_id, update_request)
            print("Order Updated Successfully:")
            print(f"Order ID: {updated_order.id}")
            print(f"New Price: {updated_order.price_order}")
            print(f"New Stop Loss: {updated_order.price_sl}")
            print(f"New Take Profit: {updated_order.price_tp}")
            return updated_order
            
        except ApiException as e:
            print(f"Exception when calling OrdersApi->update_trader_order: {e}")
            raise


@handle_api_exception
def cancel_order(order_id, reason="User cancellation"):
    """
    Example: Cancel an existing order.
    
    Args:
        order_id (int): Order ID to cancel
        reason (str): Cancellation reason
        
    Returns:
        str: Cancellation confirmation
    """
    print(f"=== Canceling Order ID: {order_id} ===")
    
    with get_api_client() as api_client:
        orders_api = openapi_client.OrdersApi(api_client)
        
        try:
            # Get account info for required fields
            accounts_api = openapi_client.AccountsApi(api_client)
            account_info = accounts_api.get_trader_account()
            
            # Create cancellation request with all required fields
            cancel_request = openapi_client.MessagingCancelOrder(
                account_id=account_info.id,
                id=order_id,
                user_id=account_info.user_id
            )
            
            # Cancel the order
            result = orders_api.cancel_trader_order(order_id, cancel_request)
            print(f"Order {order_id} cancelled successfully")
            print(f"Result: {result}")
            return result
            
        except ApiException as e:
            print(f"Exception when calling OrdersApi->cancel_trader_order: {e}")
            raise


@handle_api_exception
def get_order_history():
    """
    Example: Get order history.
    
    Returns:
        List[ModelOrder]: Historical orders
    """
    print("=== Getting Order History ===")
    
    with get_api_client() as api_client:
        orders_api = openapi_client.OrdersApi(api_client)
        
        try:
            order_history = orders_api.get_trader_orders_history()
            
            # Get symbols list to map symbol_id to symbol name
            symbols_api = openapi_client.SymbolsApi(api_client)
            all_symbols = symbols_api.get_trader_symbols()
            symbol_map = {symbol.id: symbol.symbol for symbol in all_symbols}
            
            print(f"Found {len(order_history)} historical orders:")
            for order in order_history[:10]:  # Show first 10
                print(f"Order ID: {order.id}")
                symbol_name = symbol_map.get(order.symbol_id, f"ID:{order.symbol_id}")
                print(f"  Symbol: {symbol_name}")
                print(f"  Type: {order.type}")
                print(f"  Volume: {order.volume_current or order.volume_initial}")
                print(f"  Status: {order.status}")
                print(f"  Created: {order.created_at}")
                print("---")
            
            return order_history
            
        except ApiException as e:
            print(f"Exception when calling OrdersApi->get_trader_orders_history: {e}")
            raise


def main():
    """
    Interactive test of all Order APIs with proper error handling.
    
    Tests all order APIs with pauses between each test:
    1. Get all orders
    2. Get specific order details  
    3. Create market order
    4. Update order
    5. Cancel order
    6. Get order history
    """
    print("Order API Testing - Interactive Mode")
    print("=" * 40)
    print("Press Enter after each test to continue to the next one...")
    
    try:
        # Test 1: Get all current orders
        print("\n1. Testing get_all_orders()...")
        orders = get_all_orders()
        input("\nPress Enter to continue to next test...")
        
        # Test 2: Get order history
        print("\n2. Testing get_order_history()...")
        history = get_order_history()
        input("\nPress Enter to continue to next test...")
        
                        # Test 3: Create order first (so we have orders for other tests)
        print("\n3. Testing order creation...")
        print("💡 Choose order type:")
        print("   - Market Order: Executes immediately, becomes a position")
        print("   - Pending Order: Stays in orders list for testing update/cancel")
        
        created_order = None
        user_input = input("\nContinue with create order test? (y/N): ").strip().lower()
        
        if user_input == 'y':
            try:
                print("\nOrder Type:")
                print("1. Market Order (executes immediately)")
                print("2. Pending Order (stays in orders list)")
                order_type_input = input("Choose (1 or 2): ").strip()
                
                print("\nEnter order details:")
                
                symbol_name = input("Symbol (e.g., EURUSD, GBPUSD): ").strip().upper()
                if not symbol_name:
                    print("Symbol is required. Create order test skipped.")
                else:
                    volume_input = input("Volume (e.g., 0.01): ").strip()
                    volume = float(volume_input) if volume_input else 0.01
                    
                    print("Side: 0=Buy, 1=Sell")
                    side_input = input("Side (0 or 1): ").strip()
                    side_type = int(side_input) if side_input in ['0', '1'] else 0
                    
                    stop_loss_input = input("Stop Loss (optional): ").strip()
                    stop_loss = float(stop_loss_input) if stop_loss_input else None
                    
                    take_profit_input = input("Take Profit (optional): ").strip()
                    take_profit = float(take_profit_input) if take_profit_input else None
                    
                    if order_type_input == '2':
                        # Pending order needs a specific price
                        order_price_input = input("Order Price (e.g., 1.1000): ").strip()
                        order_price = float(order_price_input) if order_price_input else 1.1000
                        
                        print(f"\nCreating pending order:")
                        print(f"  Symbol: {symbol_name}")
                        print(f"  Volume: {volume}")
                        print(f"  Side: {'Buy' if side_type == 0 else 'Sell'}")
                        print(f"  Price: {order_price}")
                        print(f"  Stop Loss: {stop_loss}")
                        print(f"  Take Profit: {take_profit}")
                        
                        created_order = create_pending_order(
                            symbol_name=symbol_name,
                            volume=volume,
                            side_type=side_type,
                            order_price=order_price,
                            stop_loss=stop_loss,
                            take_profit=take_profit
                        )
                    else:
                        # Market order
                        print(f"\nCreating market order:")
                        print(f"  Symbol: {symbol_name}")
                        print(f"  Volume: {volume}")
                        print(f"  Side: {'Buy' if side_type == 0 else 'Sell'}")
                        print(f"  Stop Loss: {stop_loss}")
                        print(f"  Take Profit: {take_profit}")
                        
                        created_order = create_market_order(
                            symbol_name=symbol_name,
                            volume=volume,
                            side_type=side_type,
                            stop_loss=stop_loss,
                            take_profit=take_profit
                        )
                    
                    print("Order creation test completed")
            except ValueError:
                print("Invalid number format. Create order test skipped.")
            except Exception as e:
                print(f"Create order test result: {e}")
        else:
            print("Create order test skipped")
        
        input("\nPress Enter to continue to next test...")
        
        # Now get fresh orders list (including the one we just created)
        print("\n4. Getting updated orders list...")
        
        # Add a small delay to allow order processing
        import time
        print("Waiting 2 seconds for order processing...")
        time.sleep(2)
        
        try:
            updated_orders = get_all_orders()
            print(f"Found {len(updated_orders) if updated_orders else 0} orders after creation")
            
            # Check if the market order became a position instead
            print("Checking if order became a position...")
            try:
                from examples.positions import get_all_positions
                current_positions = get_all_positions()
                print(f"Current positions count: {len(current_positions) if current_positions else 0}")
                if current_positions:
                    latest_position = current_positions[0]  # Most recent position
                    print(f"Latest position - Symbol: {latest_position.symbol.name if hasattr(latest_position.symbol, 'name') else latest_position.symbol}, Volume: {latest_position.volume_current}")
            except Exception as pos_error:
                print(f"Could not check positions: {pos_error}")
                
        except Exception as e:
            print(f"Error getting updated orders: {e}")
            updated_orders = orders  # Use original list if refresh fails
        
        # If no orders found, suggest creating a pending order for testing
        if not updated_orders and created_order:
            print("\n💡 Market orders execute immediately and become positions.")
            print("   For testing order operations (get details, update, cancel),")
            print("   you might want to create a pending order with a specific price.")
            print("   The market order you created likely became a position.")
        
        if updated_orders or created_order:
            # Test 5: Get specific order details
            print("\n5. Testing get_order_details()...")
            if updated_orders:
                test_order = updated_orders[0]
                print(f"Testing with order ID: {test_order.id}")
                get_order_details(test_order.id)
            else:
                print("No orders available for details test")
            
            input("\nPress Enter to continue to next test...")
            
            # Test 6: Update order (only if we have orders)
            if updated_orders:
                print("\n6. Testing update_order()...")
                first_order = updated_orders[0]
                print(f"⚠️  This will modify order ID: {first_order.id}")
                print(f"   Current Price: {first_order.price_order}")
                print(f"   Current Stop Loss: {first_order.price_sl}")
                print(f"   Current Take Profit: {first_order.price_tp}")
                print(f"   Current Volume: {first_order.volume_current or first_order.volume_initial}")
                
                user_input = input("\nContinue with update test? (y/N): ").strip().lower()
                
                if user_input == 'y':
                    try:
                        print("\nEnter new values (press Enter to keep current value):")
                        
                        new_price_input = input(f"New Price (current: {first_order.price_order}): ").strip()
                        new_price = float(new_price_input) if new_price_input else None
                        
                        new_sl_input = input(f"New Stop Loss (current: {first_order.price_sl}): ").strip()
                        new_stop_loss = float(new_sl_input) if new_sl_input else None
                        
                        new_tp_input = input(f"New Take Profit (current: {first_order.price_tp}): ").strip()
                        new_take_profit = float(new_tp_input) if new_tp_input else None
                        
                        current_volume = first_order.volume_current or first_order.volume_initial
                        new_vol_input = input(f"New Volume (current: {current_volume}): ").strip()
                        new_volume = float(new_vol_input) if new_vol_input else None
                        
                        update_order(
                            first_order.id, 
                            new_price=new_price,
                            new_stop_loss=new_stop_loss, 
                            new_take_profit=new_take_profit,
                            new_volume=new_volume
                        )
                        print("Order update test completed")
                    except ValueError:
                        print("Invalid number format. Update test skipped.")
                    except Exception as e:
                        print(f"Update test result: {e}")
                else:
                    print("Update test skipped")
                
                input("\nPress Enter to continue to next test...")
                
                # Test 7: Cancel order
                print("\n7. Testing cancel_order()...")
                order_to_cancel = updated_orders[-1] if len(updated_orders) > 1 else updated_orders[0]
                print(f"⚠️  This will cancel order ID: {order_to_cancel.id}")
                symbol_name = order_to_cancel.symbol.name if hasattr(order_to_cancel.symbol, 'name') and order_to_cancel.symbol else order_to_cancel.symbol
                print(f"   Symbol: {symbol_name}")
                print(f"   Volume: {order_to_cancel.volume_current or order_to_cancel.volume_initial}")
                
                user_input = input("\nContinue with cancel test? (y/N): ").strip().lower()
                
                if user_input == 'y':
                    try:
                        cancel_order(
                            order_to_cancel.id, 
                            reason="API Testing"
                        )
                        print("Order cancel test completed")
                    except Exception as e:
                        print(f"Cancel test result: {e}")
                else:
                    print("Cancel test skipped")
            else:
                print("No orders available for update/cancel tests")
        else:
            print("No orders available for testing order details, update, or cancel")
        
        print("\n✅ All Order API tests completed!")
        
    except Exception as e:
        print(f"Error during testing: {e}")


if __name__ == "__main__":
    main()
