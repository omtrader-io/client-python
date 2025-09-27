#!/usr/bin/env python3
import os
import time
import logging
from typing import Dict, Any, Optional
from omtrader import WebSocketClient, EventMessageType

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class WebSocketTester:
    def __init__(self):
        self.client = None
        self.running = True
        
    def connect(self):
        """Connect to WebSocket with credentials"""
        # Get API key and host from environment
        api_key = os.getenv("OMTRADER_API_KEY")
        host = os.getenv("OMTRADER_HOST")
        
        # Create and connect client
        self.client = WebSocketClient(
            api_key=api_key,
            host=host,
            trace=True  # Enable debug logging
        )
        
        # Connect (this will handle login and session validation)
        logger.info("Connecting to WebSocket...")
        self.client.connect()
        time.sleep(2)  # Give it time to connect
        
    def test_market_data(self):
        """Test market data subscription"""
        def market_callback(message):
            logger.info(f"Market data received: {message}")
            
        def error_callback(message):
            logger.error(f"Error received: {message}")
            
        symbol_id = int(input("Enter symbol ID to subscribe (e.g. 1 for EUR/USD): "))
        
        # Subscribe to market data and errors
        self.client.subscribe(EventMessageType.MARKET_FEED, market_callback)
        self.client.subscribe(EventMessageType.ERROR, error_callback)
        
        # Subscribe to market data
        self.client.send_market_subscribe(symbol_id)
        logger.info(f"Subscribed to market data for symbol {symbol_id}")
        
        # Wait for data
        try:
            logger.info("Waiting for market data... Press Ctrl+C to stop")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            # Unsubscribe on interrupt
            self.client.send_market_unsubscribe(symbol_id)
            logger.info("Unsubscribed from market data")
        
    def test_account_updates(self):
        """Test account updates subscription"""
        def account_callback(message):
            logger.info(f"Account update received: {message}")
            
        # Subscribe to all account events
        for event_type in [
            EventMessageType.ORDERS_PLACE,
            EventMessageType.ORDERS_UPDATE,
            EventMessageType.ORDERS_CANCEL,
            EventMessageType.POSITIONS_OPEN,
            EventMessageType.POSITIONS_UPDATE,
            EventMessageType.POSITIONS_CLOSE,
            EventMessageType.DEALS_CREATE,
            EventMessageType.DEALS_UPDATE
        ]:
            self.client.subscribe(event_type, account_callback)
            
        # Start account updates
        self.client.start_account_updates()
        logger.info("Started account updates")
        logger.info("Waiting for updates (30 seconds)...")
        time.sleep(30)
        
        # Stop updates
        self.client.stop_account_updates()
        logger.info("Stopped account updates")
        
    def test_heartbeat(self):
        """Test heartbeat mechanism"""
        logger.info("Monitoring heartbeat for 1 minute...")
        logger.info("(Heartbeat should occur every 30 seconds)")
        time.sleep(60)
        
    def test_session_validation(self):
        """Test session validation"""
        logger.info("Testing session validation...")
        
        # Create second client with same credentials to test session conflict
        api_key = os.getenv("OMTRADER_API_KEY")
        host = os.getenv("OMTRADER_WS_HOST", "wss://api.omtrader.io")
        
        second_client = WebSocketClient(
            api_key=api_key,
            host=host,
            trace=True
        )
        
        try:
            second_client.connect()
            logger.error("Expected session validation to fail!")
        except Exception as e:
            logger.info(f"Session validation failed as expected: {e}")
        finally:
            if second_client:
                second_client.close()
                
    def run(self):
        """Main menu loop"""
        if not self.client:
            self.connect()
            
        while self.running:
            print("\nWebSocket Test Menu")
            print("1. Test market data subscription")
            print("2. Test account updates")
            print("3. Monitor heartbeat")
            print("4. Test session validation")
            print("5. Reconnect")
            print("6. Exit")
            
            choice = input("\nEnter choice (1-6): ")
            
            try:
                if choice == "1":
                    self.test_market_data()
                elif choice == "2":
                    self.test_account_updates()
                elif choice == "3":
                    self.test_heartbeat()
                elif choice == "4":
                    self.test_session_validation()
                elif choice == "5":
                    if self.client:
                        self.client.close()
                    self.connect()
                elif choice == "6":
                    self.running = False
                    if self.client:
                        self.client.close()
                    logger.info("Exiting...")
                    break
                else:
                    print("Invalid choice")
                    
            except Exception as e:
                logger.error(f"Error in menu option {choice}: {e}")
                
            # Small delay to prevent menu from refreshing too quickly
            time.sleep(0.5)

if __name__ == "__main__":
    try:
        tester = WebSocketTester()
        tester.run()
    except KeyboardInterrupt:
        print("\nExiting due to user interrupt...")
        if tester.client:
            tester.client.close()
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        if tester.client:
            tester.client.close()