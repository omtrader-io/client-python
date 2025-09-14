"""
Account Management Examples

This module demonstrates how to use the AccountsApi for:
- Getting account information
- Opening new trading accounts
"""

import openapi_client
from openapi_client.rest import ApiException
from examples.config import get_api_client, handle_api_exception
from pprint import pprint
import requests

@handle_api_exception
def get_account_info():
    """
    Example: Get current trader account information.
    
    Returns:
        ModelTradeAccount: Account information
    """
    print("=== Getting Account Information ===")
    
    with get_api_client() as api_client:
        # Create an instance of the API class
        accounts_api = openapi_client.AccountsApi(api_client)
        
        try:
            # Get trader account information
            account_info = accounts_api.get_trader_account()
            
            # DEBUG: Let's see the raw response
            print("=== RAW API Response Debug ===")
            
            # Try to access the raw response if possible
            # This might need adjustment based on the OpenAPI client structure
            if hasattr(accounts_api, 'api_client') and hasattr(accounts_api.api_client, 'last_response'):
                print(f"Raw response: {accounts_api.api_client.last_response}")
            
            print("Account Information:")
            print(f"Account ID: {account_info.id}")
            print(f"Balance: {account_info.balance}")
            print(f"Equity: {account_info.equity}")
            print(f"Margin: {account_info.margin}")
            print(f"Free Margin: {account_info.margin_free}")
            print(f"Currency: {account_info.currency}")
            print(f"Leverage: {account_info.leverage}")
            print(f"Profit: {account_info.profit}")
            print(f"Assets: {account_info.assets}")
            print(f"Floating: {account_info.floating}")
            
            # Show all available data
            print("\n=== Complete Account Data ===")
            print(account_info.to_str())
            
            return account_info
            
        except ApiException as e:
            print(f"Exception when calling AccountsApi->get_trader_account: {e}")
            raise


@handle_api_exception
def open_new_account():
    """
    Example: Open a new trading account.
    
    Note: This is typically used for demo accounts or when setting up new accounts.
    """
    print("=== Opening New Trading Account ===")
    
    with get_api_client() as api_client:
        accounts_api = openapi_client.AccountsApi(api_client)
        
        try:
            # Create account opening request
            account_request = openapi_client.MessagingOpenAccount(
                # Add required fields based on your API documentation
                # These are example fields - adjust based on actual model
                currency="USD",
                leverage=100,
                account_type="demo"  # or "live"
            )
            
            # Open the account
            new_account = accounts_api.open_trader_account(account_request)
            
            print("New Account Created:")
            print(f"Account ID: {new_account.id}")
            print(f"Currency: {new_account.currency}")
            print(f"Leverage: {new_account.leverage}")
            print(f"Status: {new_account.status}")
            
            return new_account
            
        except ApiException as e:
            print(f"Exception when calling AccountsApi->open_trader_account: {e}")
            raise


def debug_raw_account_response():
    """Debug function to see raw account response"""
    
    # Get the access token the same way
    from examples.config import get_access_token
    import os
    
    api_key = os.environ.get("OMTRADER_API_KEY")
    access_token = get_access_token(api_key)
    
    # Make direct request to see raw response
    url = "https://api.omtrader.io/api/v1/trader/account"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json'
    }
    
    response = requests.get(url, headers=headers)
    
    print(f"Raw response status: {response.status_code}")
    print(f"Raw response headers: {response.headers}")
    print(f"Raw response body: {response.text}")
    
    if response.status_code == 200:
        try:
            json_data = response.json()
            print(f"Parsed JSON: {json_data}")
        except:
            print("Could not parse as JSON")


def main():
    """Run account management examples."""
    print("Omtrader SDK - Account Management Examples")
    print("=" * 50)
    
    try:
        # Debug raw response first
        print("=== DEBUG: Raw Response ===")
        debug_raw_account_response()
        print()
        
        # Then try the normal flow
        account = get_account_info()
        
    except Exception as e:
        print(f"Error running examples: {e}")


if __name__ == "__main__":
    main() 