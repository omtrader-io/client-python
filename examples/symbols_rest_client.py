#!/usr/bin/env python3
"""Simple Symbols API example"""

import os
from omtrader import RESTClient

# Initialize client
client = RESTClient(api_key=os.environ["OMTRADER_API_KEY"])

# List symbols
symbols = client.list_symbols()
print(f"Found {len(symbols)} symbols")

# Show first few symbols
for symbol in symbols[:3]:
    print(f"Symbol {symbol.id}: {symbol.symbol}")

# Get specific symbol details
if symbols:
    symbol_detail = client.get_symbol(symbols[0].id)
    print(f"Symbol details: {symbol_detail.symbol} - {symbol_detail.digits} digits")

# Get symbol tick history (requires additional parameters)
if symbols:
    from datetime import datetime, timedelta
    now = int(datetime.now().timestamp())
    hour_ago = int((datetime.now() - timedelta(hours=1)).timestamp())
    
    try:
        ticks = client.get_symbol_ticks_history(
            symbols[0].id,
            var_from=hour_ago, 
            to=now, 
            resolution="1m", 
            count_back=60
        )
        print(f"Found {len(ticks)} ticks for {symbols[0].symbol}")
        print(ticks[:3])
    except Exception as e:
        print(f"Tick history error: {e}")
        print("Tick history requires: from/to timestamps, resolution, count_back")