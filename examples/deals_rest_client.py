"""Simple Deals API example"""

import os
from omtrader import RESTClient

# Initialize client
client = RESTClient(api_key=os.environ["OMTRADER_API_KEY"])

# List deals
deals = client.list_deals()
print(f"Found {len(deals)} deals")

# Show first few deals
for deal in deals[:3]:
    print(f"Deal {deal.id}: {deal.volume} volume, {deal.profit} profit")

# Get specific deal
if deals:
    deal_detail = client.get_deal(deals[0].id)
    print(f"Deal details: {deal_detail.volume} volume, {deal_detail.profit} profit")