from alpaca.data.live import StockDataStream
from alpaca.trading.stream import TradingStream
from config import *


# Receive Stock Data in Real time through Websocket
# API Documentation: https://docs.alpaca.markets/docs/websocket-streaming
stream = StockDataStream(api_key=api_key, secret_key=secret_key)

async def handle_trade(data):
    print(data)

stream.subscribe_trades(handle_trade, "AAPL")

# Runs the Websocket
stream.run()


# Receive updates on Trades made
# https://docs.alpaca.markets/docs/working-with-orders#listen-for-updates-to-orders
# trade_stream_client = TradingStream(api_key=api_key, secret_key=secret_key, paper=True)
# async def trade_updates_handler(data):
#     print(data)

# trade_stream_client.subscribe_trade_updates(trade_updates_handler)
# trade_stream_client.run()