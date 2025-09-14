"""Simple Positions API example"""

import os
from omtrader import RESTClient

# Initialize client
client = RESTClient(api_key=os.environ["OMTRADER_API_KEY"])

# List current positions
positions = client.list_positions()
print(f"Found {len(positions)} positions")

# Show positions
for position in positions:
    symbol_name = getattr(position.symbol, 'symbol', None) if position.symbol else None
    if not symbol_name:
        symbol_name = f"Symbol_ID_{position.symbol_id}" if position.symbol_id else "Unknown"
    print(f"Position {position.id}: {symbol_name} {position.volume_current} volume, {position.profit} profit")

# Get specific position
if positions:
    position_detail = client.get_position(positions[0].id)
    symbol_name = getattr(position_detail.symbol, 'symbol', None) if position_detail.symbol else None
    if not symbol_name:
        symbol_name = f"Symbol_ID_{position_detail.symbol_id}" if position_detail.symbol_id else "Unknown"
    print(f"Position details: {symbol_name} {position_detail.volume_current} volume, {position_detail.profit} profit")

# List position history
position_history = client.list_positions_history()
print(f"Found {len(position_history)} historical positions")

# Position management (demo - commented for safety)
if positions:
    position_id = positions[0].id
    # Update position with simple dict - RESTClient handles MessagingUptPosition conversion
    update_data = {
        "id": position_id,
        "account_id": positions[0].account_id,
        "user_id": positions[0].account_id,  # Use account_id as user_id
        "price_sl": 1.06,    # Stop loss (optional)
        "price_tp": 1.08     # Take profit (optional)
    }
    print(f"Update structure for position {position_id}: {update_data}")
    # client.update_position(position_id, update_data)  # Uncomment to update
    
    # Close position - RESTClient handles MessagingClosePosition automatically  
    print(f"Close position {position_id} - RESTClient gets volume from position automatically")
    # client.close_position(position_id)  # Uncomment to close