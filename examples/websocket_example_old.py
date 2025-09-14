from openapi_client.ws_client import WebSocketClient, EventMessageType
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Example usage
def handle_order_placed(data):
    print(f"Order placed: {data}")

client = WebSocketClient(
    url="wss://api.omtrader.io",
    session_id="your-session-id",
    access_token="your-access-token"
)

# Subscribe to order placement events
client.subscribe(EventMessageType.ORDERS_PLACE, handle_order_placed)

# Connect to WebSocket
client.connect()

# Send market subscription
client.send(
    EventMessageType.MARKET_SUBSCRIBE_SYMBOL,
    data=1  # symbolId for EUR/USD
)

# To close connection
# client.close()

if __name__ == "__main__":
    try:
        # Keep the main thread alive
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        client.close()
        print("\nWebSocket connection closed")