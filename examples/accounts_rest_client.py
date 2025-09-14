"""Simple Accounts API example"""

import os
from omtrader import RESTClient

# Initialize client
client = RESTClient(api_key=os.environ["OMTRADER_API_KEY"])

# Get account info
account = client.get_account()
print(f"Account: {account}")

# Account opening (demo structure - not executed)
account_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "leverage": 100,
    "currency": "USD"
}
print(f"Account opening structure: {account_data}")
# result = client.open_account(account_data)  # Uncomment to actually open account