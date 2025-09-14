"""Simple Orders API example"""

import os
from omtrader import RESTClient

# Initialize client
client = RESTClient(api_key=os.environ["OMTRADER_API_KEY"])

# List current orders
orders = client.list_orders()
print(f"Found {len(orders)} orders")

# Show orders
for order in orders:
    symbol_name = getattr(order.symbol, 'symbol', None) if order.symbol else None
    if not symbol_name:
        symbol_name = f"Symbol_ID_{order.symbol_id}" if order.symbol_id else "Unknown"
    print(f"Order {order.id}: {symbol_name} {order.volume_initial} volume, {order.type} type")

# Get specific order
if orders:
    order_detail = client.get_order(orders[0].id)
    symbol_name = getattr(order_detail.symbol, 'symbol', None) if order_detail.symbol else None
    if not symbol_name:
        symbol_name = f"Symbol_ID_{order_detail.symbol_id}" if order_detail.symbol_id else "Unknown"
    print(f"Order details: {symbol_name} {order_detail.volume_initial} volume, {order_detail.type} type")

# List order history
order_history = client.list_orders_history()
print(f"Found {len(order_history)} historical orders")

# Order management (demo - commented for safety)
order_data = {
    "account_id": 1,  # Get from account info
    "user_id": 1,     # Get from account info  
    "symbol_id": 1,   # Get from symbols list
    "volume": 0.1,
    "order_price": 1.05,
    "side": 0,        # 0=Buy, 1=Sell
    "type": 1         # 0=market_order
}
print(f"Order creation structure: {order_data}")
# new_order = client.create_order(order_data)  # Uncomment to create order

if orders:
    order_id = orders[0].id
    # Update requires: id, account_id, user_id, volume, order_price (MessagingUptOrder)
    update_data = {
        "id": order_id,
        "account_id": orders[0].account_id,
        "user_id": orders[0].account_id,  # Use account_id as user_id for now
        "volume": 0.2, 
        "order_price": 1.06
    }
    print(f"Update structure for order {order_id}: {update_data}")
    # client.update_order(order_id, update_data)  # Uncomment to update
    
    # Cancel order (will auto-create MessagingCancelOrder with required fields)
    print(f"Cancel order {order_id} - RESTClient handles the cancel structure automatically")
    client.cancel_order(order_id)  # Uncomment to cancel