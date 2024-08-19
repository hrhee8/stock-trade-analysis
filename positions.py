from alpaca.trading.client import TradingClient
from config import *

trading_client = TradingClient(api_key=api_key, secret_key=secret_key)

positions = trading_client.get_all_positions()

for position in positions:
    print(position.symbol, position.current_price)

# Sell & Close all positions
# trading_client.close_all_positions(True)