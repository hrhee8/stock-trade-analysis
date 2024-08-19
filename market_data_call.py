from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from config import *
from datetime import datetime as dt

data_client =  StockHistoricalDataClient(api_key=api_key,secret_key=secret_key)

request_params = StockTradesRequest(
    symbol_or_symbols="AAPL",
    start=dt(2024,8,16,14,00,00,00),
    end=dt(2024,8,16,15,00,00,00)
)

trades = data_client.get_stock_trades(request_params=request_params)

