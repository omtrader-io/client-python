"""
Configuration module for API examples.

This module provides common configuration and setup utilities
for all the example scripts.
"""

import os
import openapi_client
from openapi_client.rest import ApiException
import logging
import http.client as http_client
import requests


def get_access_token(api_key):
    """
    Login to get access token using API key
    """
    login_url = "https://api.omtrader.io/api/v1/oauth2/login"
    
    # Query parameters in URL
    params = {
        'remember_me': 'false',
        'grant_type': 'api_key'
    }
    
    # Correct header format from Postman
    headers = {
        'API-Key': api_key,
        'Accept': 'application/json'
    }
    
    # POST with allow_redirects=True (equivalent to --location in curl)
    response = requests.post(login_url, params=params, headers=headers, allow_redirects=True)
    
    print(f"Login response status: {response.status_code}")
    print(f"Login response body: {response.text}")
    
    if response.status_code == 200:
        try:
            token_data = response.json()
            print(f"Token data structure: {token_data}")
            
            # The access token is nested in data.access_token
            if token_data.get('success') and token_data.get('data'):
                access_token = token_data['data'].get('access_token')
                print(f"Extracted access token: {access_token}")
                return access_token
            else:
                raise Exception("Login successful but no access token in response")
            
        except Exception as e:
            print(f"Error parsing JSON response: {e}")
            raise Exception(f"Failed to parse login response: {response.text}")
    else:
        raise Exception(f"OAuth2 login failed: {response.status_code} - {response.text}")


def get_api_client():
    """
    Create and configure an API client instance.
    
    Returns:
        openapi_client.ApiClient: Configured API client
    """
    # Enable detailed HTTP logging
    http_client.HTTPConnection.debuglevel = 1
    logging.basicConfig(level=logging.DEBUG)
    
    # Get API key from environment
    api_key = os.environ.get("OMTRADER_API_KEY")
    if not api_key:
        raise ValueError(
            "OMTRADER_API_KEY environment variable is required. "
            "Please set it with your API key."
        )
    
    # First, login to get access token
    print("Authenticating with Omtrader...")
    access_token = get_access_token(api_key)
    
    # Fix the string slicing error
    if access_token and isinstance(access_token, str):
        print(f"Received access token: {access_token[:10]}...")
    else:
        print(f"No valid access token received: {access_token}")
        raise Exception("Failed to get valid access token")
    
    # Configure the API client with the access token
    configuration = openapi_client.Configuration(
        host="https://api.omtrader.io",  # Just the base domain
        debug=True
    )
    
    # Use the access token for API calls
    configuration.api_key['BearerAuth'] = access_token
    configuration.api_key_prefix['BearerAuth'] = 'Bearer'
    
    return openapi_client.ApiClient(configuration)


def handle_api_exception(func):
    """
    Decorator to handle common API exceptions.
    
    Args:
        func: Function to wrap
        
    Returns:
        Wrapped function with exception handling
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ApiException as e:
            print(f"API Exception in {func.__name__}: {e}")
            print(f"Status code: {e.status}")
            print(f"Reason: {e.reason}")
            if e.body:
                print(f"Response body: {e.body}")
            raise
        except Exception as e:
            print(f"Unexpected error in {func.__name__}: {e}")
            raise
    
    return wrapper


# Common constants
DEFAULT_TIMEOUT = 30.0 