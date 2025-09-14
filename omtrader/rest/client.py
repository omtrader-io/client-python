"""
OMTrader REST API Client

Main client class that provides a unified interface to all REST API endpoints.
"""

import os
from typing import Optional, Dict, Any, Iterator, Union
from .api_client import ApiClient
from .configuration import Configuration
from .exceptions import ApiException
from .api.accounts_api import AccountsApi
from .api.deals_api import DealsApi
from .api.orders_api import OrdersApi
from .api.positions_api import PositionsApi
from .api.symbols_api import SymbolsApi
import requests
import logging

logger = logging.getLogger(__name__)


class RESTClient:
    """
    Unified REST API client for OMTrader trading platform.
    
    This client provides a clean, unified interface to all OMTrader REST API endpoints,
    handling authentication, configuration, and providing convenient methods for all
    trading operations including account management, orders, positions, symbols, and deals.
    
    Features:
        - Automatic authentication with API key
        - Request/response tracing for debugging
        - Automatic model conversion (dict → API models)
        - Comprehensive error handling
        - Type hints for better development experience
    
    Args:
        api_key (str, optional): Your OMTrader API key. If not provided, will look 
            for OMTRADER_API_KEY environment variable.
        host (str, optional): API host URL. Defaults to production endpoint if not provided.
        debug (bool): Enable debug logging. Defaults to False.
        trace (bool): Enable request/response tracing for debugging. Defaults to False.
        timeout (float): Request timeout in seconds. Defaults to 30.0.
    
    Attributes:
        api_key (str): The API key being used
        host (str): The API host URL
        trace (bool): Whether tracing is enabled
        timeout (float): Request timeout in seconds
    
    Available Methods:
        Account Methods:
            - get_account(): Get account information
            - open_account(data): Open new account
        
        Order Methods:
            - list_orders(): List current orders
            - get_order(id): Get specific order
            - create_order(data): Create new order
            - update_order(id, data): Update existing order
            - cancel_order(id): Cancel order
            - list_orders_history(): Get order history
            - approve_order(id, data): Approve order
        
        Position Methods:
            - list_positions(): List current positions
            - get_position(id): Get specific position
            - update_position(id, data): Update position
            - close_position(id): Close position
            - list_positions_history(): Get position history
        
        Symbol Methods:
            - list_symbols(): List available symbols
            - get_symbol(id): Get specific symbol
            - get_symbol_ticks_history(id, **params): Get historical tick data
        
        Deal Methods:
            - list_deals(): List deals
            - get_deal(id): Get specific deal
    
    Raises:
        Exception: If API key is not provided and not found in environment
        ApiException: For API-related errors (authentication, validation, etc.)
    
    Examples:
        Basic Usage:
            >>> from omtrader import RESTClient
            >>> client = RESTClient(api_key="your_api_key")
            >>> account = client.get_account()
            >>> print(f"Balance: {account.balance}")
        
        With Environment Variable:
            >>> import os
            >>> os.environ["OMTRADER_API_KEY"] = "your_api_key"
            >>> client = RESTClient()  # Uses env var
        
        With Debugging:
            >>> client = RESTClient(api_key="your_key", trace=True)
            >>> # Will print request/response details
        
        Order Management:
            >>> # Create order
            >>> order_data = {
            ...     "account_id": 1,
            ...     "user_id": 1,
            ...     "symbol_id": 1,
            ...     "volume": 0.01,
            ...     "order_price": 1.2000,
            ...     "side": 0,  # Buy
            ...     "type": 0   # Market
            ... }
            >>> order_id = client.create_order(order_data)
            
            >>> # Cancel order
            >>> client.cancel_order(order_id)
        
        Position Management:
            >>> positions = client.list_positions()
            >>> if positions:
            ...     # Update stop loss
            ...     client.update_position(positions[0].id, {
            ...         "id": positions[0].id,
            ...         "account_id": positions[0].account_id,
            ...         "user_id": positions[0].account_id,
            ...         "price_sl": 1.1950
            ...     })
    
    Note:
        This client automatically converts dict inputs to the appropriate API model
        objects (MessagingCrtOrder, MessagingUptOrder, etc.) so you can work with
        simple dictionaries instead of complex model objects.
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        host: Optional[str] = None,
        debug: bool = False,
        trace: bool = False,
        timeout: float = 30.0
    ):
        """
        Initialize the REST client.
        
        Args:
            api_key: Your OMTrader API key. If not provided, will look for OMTRADER_API_KEY env var
            host: API host URL. Defaults to production if not provided
            debug: Enable debug logging
            trace: Enable request/response tracing
            timeout: Request timeout in seconds
        """
        # Get API key from parameter or environment
        self.api_key = api_key or os.environ.get("OMTRADER_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key is required. Provide it as a parameter or set OMTRADER_API_KEY environment variable."
            )
        
        # Set default host if not provided
        if not host:
            host = os.environ.get("OMTRADER_HOST", "http://api.omtrader.io")
        
        self.host = host
        self.debug = debug
        self.trace = trace
        self.timeout = timeout
        self._access_token: Optional[str] = None
        
        # Configure logging
        if debug:
            logging.basicConfig(level=logging.DEBUG)
        
        # Initialize the underlying API client
        self._setup_client()
    
    def _setup_client(self):
        """Setup the underlying OpenAPI client with authentication."""
        # First, get access token
        self._access_token = self._get_access_token()
        
        # Configure the API client
        configuration = Configuration(
            host=self.host,
            debug=self.debug
        )
        
        # Set authentication
        configuration.api_key['BearerAuth'] = self._access_token
        configuration.api_key_prefix['BearerAuth'] = 'Bearer'
        
        # Create API client
        self._api_client = ApiClient(configuration)
        
        # Initialize API instances
        self._accounts_api = AccountsApi(self._api_client)
        self._deals_api = DealsApi(self._api_client)
        self._orders_api = OrdersApi(self._api_client)
        self._positions_api = PositionsApi(self._api_client)
        self._symbols_api = SymbolsApi(self._api_client)
        
        if self.trace:
            logger.info(f"OMTrader REST client initialized for host: {self.host}")
    
    def _get_access_token(self) -> str:
        """Get access token using API key."""
        login_url = f"{self.host}/api/v1/oauth2/login"
        
        params = {
            'remember_me': 'false',
            'grant_type': 'api_key'
        }
        
        headers = {
            'API-Key': self.api_key,
            'Accept': 'application/json'
        }
        
        if self.trace:
            logger.info(f"Authenticating with OMTrader API at {login_url}")
        
        try:
            response = requests.post(
                login_url, 
                params=params, 
                headers=headers, 
                allow_redirects=True,
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                token_data = response.json()
                if token_data.get('success') and token_data.get('data'):
                    access_token = token_data['data'].get('access_token')
                    if self.trace:
                        logger.info(f"Authentication successful, token: {access_token[:10]}...")
                    return access_token
                else:
                    raise Exception("Login successful but no access token in response")
            else:
                raise Exception(f"OAuth2 login failed: {response.status_code} - {response.text}")
                
        except requests.RequestException as e:
            raise Exception(f"Failed to authenticate: {e}")
    
    # Account Methods
    def get_account(self):
        """Get trader account information.
        
        Returns:
            ModelTradeAccount: Account information object. See ModelTradeAccount 
            for available attributes.
            
        Raises:
            ApiException: If the request fails
            
        Example:
            >>> account = client.get_account()
            >>> print(f"Account balance: {account.balance}")
        """
        try:
            return self._accounts_api.get_trader_account()
        except ApiException as e:
            if self.trace:
                logger.error(f"get_account failed: {e}")
            raise
    
    def open_account(self, account_data):
        """Open a new trader account.
        
        Args:
            account_data (dict or MessagingOpenAccount): Account opening parameters.
            See MessagingOpenAccount model for required fields.
            
        Returns:
            ModelTradeAccount: Created account information
            
        Raises:
            ApiException: If account opening fails
            
        Example:
            >>> account = client.open_account(account_data)
        """
        try:
            return self._accounts_api.open_trader_account(account_data)
        except ApiException as e:
            if self.trace:
                logger.error(f"open_account failed: {e}")
            raise
    
    # Orders Methods
    def list_orders(self, **kwargs):
        """List all orders.
        
        Args:
            **kwargs: Additional request parameters
            
        Returns:
            List[ModelOrder]: List of order objects. See ModelOrder for available attributes.
            
        Raises:
            ApiException: If the request fails
            
        Example:
            >>> orders = client.list_orders()
            >>> for order in orders:
            ...     print(f"Order {order.id}")
        """
        try:
            return self._orders_api.get_trader_orders(**kwargs)
        except ApiException as e:
            if self.trace:
                logger.error(f"list_orders failed: {e}")
            raise
    
    def get_order(self, order_id: str):
        """Get specific order by ID.
        
        Args:
            order_id (str): Order ID to retrieve
            
        Returns:
            ModelOrder: Order object. See ModelOrder for available attributes.
            
        Raises:
            ApiException: If the request fails
            
        Example:
            >>> order = client.get_order("123")
            >>> print(f"Order status: {order.status}")
        """
        try:
            return self._orders_api.get_trader_order(order_id)
        except ApiException as e:
            if self.trace:
                logger.error(f"get_order failed: {e}")
            raise
    
    def create_order(self, order_data):
        """Create a new order.
        
        Args:
            order_data (dict or MessagingCrtOrder): Order parameters containing:
                - account_id (int): Account ID (required)
                - user_id (int): User ID (required)
                - symbol_id (int): Symbol ID (required)
                - volume (float): Order volume (required)
                - order_price (float): Order price (required)
                - side (int, optional): Order side - 0=Buy, 1=Sell
                - type (int, optional): Order type - 0=market, 1=buy_limit, etc.
                - price_sl (float, optional): Stop loss price
                - price_tp (float, optional): Take profit price
                - comment (str, optional): Order comment
                - expiration_police (ModelExpirationPolicy, optional): Expiration policy
                - time_expiration (str, optional): Expiration time
                
        Returns:
            str: Order ID of the created order
            
        Raises:
            ApiException: If the order creation fails
            
        Example:
            >>> order = client.create_order({
            ...     "account_id": 1,
            ...     "user_id": 1,
            ...     "symbol_id": 1,
            ...     "volume": 0.01,
            ...     "order_price": 1.2000,
            ...     "side": 0,  # Buy
            ...     "type": 0   # Market order
            ... })
        """
        try:
            # Convert dict to MessagingCrtOrder if needed
            if isinstance(order_data, dict):
                from omtrader.rest.models import MessagingCrtOrder
                order_data = MessagingCrtOrder(**order_data)
            return self._orders_api.create_trader_order(order_data)
        except ApiException as e:
            if self.trace:
                logger.error(f"create_order failed: {e}")
            raise
    
    def update_order(self, order_id: str, order_data):
        """Update an existing order.
        
        Args:
            order_id (str): Order ID to update
            order_data (dict or MessagingUptOrder): Update parameters.
            See MessagingUptOrder model for required fields.
            
        Returns:
            str: Updated order ID
            
        Raises:
            ApiException: If the update fails
            
        Example:
            >>> client.update_order("123", {"volume": 0.02})
        """
        try:
            # Convert dict to appropriate model if needed
            if isinstance(order_data, dict):
                from omtrader.rest.models import MessagingUptOrder
                order_data = MessagingUptOrder(**order_data)
            return self._orders_api.update_trader_order(order_id, order_data)
        except ApiException as e:
            if self.trace:
                logger.error(f"update_order failed: {e}")
            raise
    
    def cancel_order(self, order_id: str, cancel_data=None):
        """Cancel an order.
        
        Args:
            order_id (str): Order ID to cancel
            cancel_data (dict or MessagingCancelOrder, optional): Cancel parameters.
            If None, will automatically create with order details.
            
        Returns:
            str: Cancelled order ID
            
        Raises:
            ApiException: If the cancellation fails
            
        Example:
            >>> client.cancel_order("123")
        """
        try:
            # If no cancel_data provided, create a minimal one
            if cancel_data is None:
                # We need to get the order details to get account_id and user_id
                order = self.get_order(order_id)
                from omtrader.rest.models import MessagingCancelOrder
                cancel_data = MessagingCancelOrder(
                    id=int(order_id),
                    account_id=order.account_id,
                    user_id=order.account_id  # Use account_id as user_id
                )
            elif isinstance(cancel_data, dict):
                from omtrader.rest.models import MessagingCancelOrder
                cancel_data = MessagingCancelOrder(**cancel_data)
            return self._orders_api.cancel_trader_order(order_id, cancel_data)
        except ApiException as e:
            if self.trace:
                logger.error(f"cancel_order failed: {e}")
            raise
    
    def list_orders_history(self, **kwargs):
        """Get orders history.
        
        Args:
            **kwargs: Additional request parameters
            
        Returns:
            List[ModelOrder]: List of historical order objects
            
        Raises:
            ApiException: If the request fails
            
        Example:
            >>> history = client.list_orders_history()
        """
        try:
            return self._orders_api.get_trader_orders_history(**kwargs)
        except ApiException as e:
            if self.trace:
                logger.error(f"list_orders_history failed: {e}")
            raise
    
    def approve_order(self, order_id: str, approval_data):
        """Approve an order.
        
        Args:
            order_id (str): Order ID to approve
            approval_data: Approval parameters
            
        Returns:
            str: Approved order ID
            
        Raises:
            ApiException: If the approval fails
            
        Example:
            >>> client.approve_order("123", approval_data)
        """
        try:
            return self._orders_api.approval_trader_order(order_id, approval_data)
        except ApiException as e:
            if self.trace:
                logger.error(f"approve_order failed: {e}")
            raise
    
    # Positions Methods
    def list_positions(self, **kwargs):
        """List all positions.
        
        Args:
            **kwargs: Additional request parameters (passed to underlying API)
            
        Returns:
            List[ModelPosition]: List of position objects. See ModelPosition 
            documentation for available attributes.
                
        Raises:
            ApiException: If the request fails
            
        Example:
            >>> positions = client.list_positions()
            >>> for pos in positions:
            ...     print(f"Position {pos.id}")
        """
        try:
            return self._positions_api.get_trader_positions(**kwargs)
        except ApiException as e:
            if self.trace:
                logger.error(f"list_positions failed: {e}")
            raise
    
    def get_position(self, position_id: str):
        """Get specific position by ID.
        
        Args:
            position_id (str): Position ID to retrieve
            
        Returns:
            ModelPosition: Position object. See ModelPosition for available attributes.
            
        Raises:
            ApiException: If the request fails
            
        Example:
            >>> position = client.get_position("123")
            >>> print(f"Position profit: {position.profit}")
        """
        try:
            return self._positions_api.get_trader_position(position_id)
        except ApiException as e:
            if self.trace:
                logger.error(f"get_position failed: {e}")
            raise
    
    def update_position(self, position_id: str, position_data):
        """Update a position.
        
        Args:
            position_id (str): Position ID to update
            position_data (dict or MessagingUptPosition): Update parameters.
            See MessagingUptPosition model for required fields.
            
        Returns:
            str: Updated position ID
            
        Raises:
            ApiException: If the update fails
            
        Example:
            >>> client.update_position("123", {"price_sl": 1.2000})
        """
        try:
            # Convert dict to appropriate model if needed
            if isinstance(position_data, dict):
                from omtrader.rest.models import MessagingUptPosition
                position_data = MessagingUptPosition(**position_data)
            return self._positions_api.update_trader_position(position_id, position_data)
        except ApiException as e:
            if self.trace:
                logger.error(f"update_position failed: {e}")
            raise
    
    def close_position(self, position_id: str, close_data=None):
        """Close a position.
        
        Args:
            position_id (str): Position ID to close
            close_data (dict or MessagingClosePosition, optional): Close parameters.
            If None, will automatically create with position details.
            
        Returns:
            str: Closed position ID
            
        Raises:
            ApiException: If the close fails
            
        Example:
            >>> client.close_position("123")
        """
        try:
            # If no close_data provided, create a minimal one
            if close_data is None:
                # We need to get the position details to get account_id, user_id, and volume
                position = self.get_position(position_id)
                from omtrader.rest.models import MessagingClosePosition
                close_data = MessagingClosePosition(
                    id=int(position_id),
                    account_id=position.account_id,
                    user_id=position.account_id,  # Use account_id as user_id
                    volume=position.volume_current or position.volume_initial or 0.01  # Use current or initial volume
                )
            elif isinstance(close_data, dict):
                from omtrader.rest.models import MessagingClosePosition
                close_data = MessagingClosePosition(**close_data)
            return self._positions_api.close_trader_position(position_id, close_data)
        except ApiException as e:
            if self.trace:
                logger.error(f"close_position failed: {e}")
            raise
    
    def list_positions_history(self, **kwargs):
        """Get positions history.
        
        Args:
            **kwargs: Additional request parameters
            
        Returns:
            List[ModelPosition]: List of historical position objects
            
        Raises:
            ApiException: If the request fails
            
        Example:
            >>> history = client.list_positions_history()
        """
        try:
            return self._positions_api.get_trader_positions_history(**kwargs)
        except ApiException as e:
            if self.trace:
                logger.error(f"list_positions_history failed: {e}")
            raise
    
    # Symbols Methods
    def list_symbols(self, **kwargs):
        """List all available symbols.
        
        Args:
            **kwargs: Additional request parameters
            
        Returns:
            List[MessagingViewSymbol]: List of symbol objects. See MessagingViewSymbol 
            for available attributes.
            
        Raises:
            ApiException: If the request fails
            
        Example:
            >>> symbols = client.list_symbols()
            >>> for symbol in symbols:
            ...     print(f"Symbol: {symbol.symbol}")
        """
        try:
            return self._symbols_api.get_trader_symbols(**kwargs)
        except ApiException as e:
            if self.trace:
                logger.error(f"list_symbols failed: {e}")
            raise
    
    def get_symbol(self, symbol_id: str):
        """Get specific symbol by ID.
        
        Args:
            symbol_id (str): Symbol ID to retrieve
            
        Returns:
            MessagingViewSymbol: Symbol object. See MessagingViewSymbol for available attributes.
            
        Raises:
            ApiException: If the request fails
            
        Example:
            >>> symbol = client.get_symbol("1")
            >>> print(f"Symbol name: {symbol.symbol}")
        """
        try:
            return self._symbols_api.get_trader_symbol(symbol_id)
        except ApiException as e:
            if self.trace:
                logger.error(f"get_symbol failed: {e}")
            raise
    
    def get_symbol_ticks_history(self, symbol_id: str, **kwargs):
        """Get symbol ticks history.
        
        Args:
            symbol_id (str): Symbol ID to get ticks for
            **kwargs: Required parameters:
                - var_from (int): From timestamp
                - to (int): To timestamp  
                - resolution (str): Resolution (e.g., "1m", "1h", "1d")
                - count_back (int): Number of ticks to retrieve
                - type (str, optional): Type ("bid" or "ask")
                
        Returns:
            List[MessagingHistoryTick]: List of tick objects
            
        Raises:
            ApiException: If the request fails
            
        Example:
            >>> ticks = client.get_symbol_ticks_history(
            ...     "1", var_from=1234567890, to=1234567900, 
            ...     resolution="1m", count_back=60
            ... )
        """
        try:
            # The API expects id as first param and symbol_id as second param
            return self._symbols_api.get_trader_symbol_ticks_history(symbol_id, symbol_id=symbol_id, **kwargs)
        except ApiException as e:
            if self.trace:
                logger.error(f"get_symbol_ticks_history failed: {e}")
            raise
    
    # Deals Methods
    def list_deals(self, **kwargs):
        """List all deals.
        
        Args:
            **kwargs: Optional parameters:
                - page (int): Page number
                - limit (int): Limit number
                - var_from (str): From date
                - to (str): To date
                - sort_by (str): Sort by field
                - dir (str): Sort direction
                
        Returns:
            List[ModelDeal]: List of deal objects. See ModelDeal for available attributes.
            
        Raises:
            ApiException: If the request fails
            
        Example:
            >>> deals = client.list_deals(limit=10)
            >>> for deal in deals:
            ...     print(f"Deal {deal.id}: {deal.profit}")
        """
        try:
            return self._deals_api.get_trader_deals(**kwargs)
        except ApiException as e:
            if self.trace:
                logger.error(f"list_deals failed: {e}")
            raise
    
    def get_deal(self, deal_id: str):
        """Get specific deal by ID.
        
        Args:
            deal_id (str): Deal ID to retrieve
            
        Returns:
            ModelDeal: Deal object. See ModelDeal for available attributes.
            
        Raises:
            ApiException: If the request fails
            
        Example:
            >>> deal = client.get_deal("123")
            >>> print(f"Deal profit: {deal.profit}")
        """
        try:
            return self._deals_api.get_trader_deal(deal_id)
        except ApiException as e:
            if self.trace:
                logger.error(f"get_deal failed: {e}")
            raise
