from alpaca.trading.client import TradingClient
from alpaca.trading.stream import TradingStream
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, GetOrdersRequest
from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from datetime import datetime as dt
from config import *

trade_client = TradingClient(api_key=api_key,secret_key=secret_key)
print("account number: ", trade_client.get_account().account_number)
print("buying power:  $", trade_client.get_account().buying_power)


# trade_stream_client = TradingStream(api_key=config.alpaca_api_key, secret_key=config.alpaca_api_secret_key, paper=True)
# async def trade_updates_handler(data):
#     print(data)

# trade_stream_client.subscribe_trade_updates(trade_updates_handler)

# trade_stream_client.run()
