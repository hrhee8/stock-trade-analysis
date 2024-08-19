from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest, LimitOrderRequest, GetOrdersRequest
from alpaca.trading.enums import OrderSide, TimeInForce, QueryOrderStatus
from config import *

trade_client = TradingClient(api_key=api_key,secret_key=secret_key)

class stock_order:
    def __init__(self):
        self.make_order = self.order_input()
        self.open_orders = self.check_open_orders()
    # Take order parameters
    def order_input():
        symbol = input("Enter the Ticker: ")
        qty = input("Quantity: ")
        while True:
            buy_sell = input("Enter 'buy' or 'sell': ").upper()
            if buy_sell in ["BUY", "SELL"]:
                if buy_sell == "BUY":
                    side = OrderSide.BUY
                elif buy_sell == "SELL":
                    side = OrderSide.SELL
                break
            else:
                print("Invalid input. Please enter either 'buy' or 'sell'")
        while True:
            marketorlimit = input("'market' or 'limit' order?").upper()
            if marketorlimit in ["MARKET", "LIMIT"]:
                break
            else:
                print("Invalid input. Please enter either 'market' or 'limit'")
        detail = {"symbol" : symbol,
                  "qty" : qty,
                  "buy_sell" : side,
                  "marketorlimit": marketorlimit}
        return detail

    # Execute market order
    def marketorder(self):
        market_order_data = MarketOrderRequest(
            symbol = self.make_order["symbol"],
            qty = self.make_order["qty"],
            side = self.make_order["buy_sell"],
            time_in_force = TimeInForce.DAY
        )
        market_order = trade_client.submit_order(market_order_data)
        print(market_order)
    
    # Execute limit order
    def limitorder(self):
        while True:
            price_limit = input("Enter Limit Price(XXX.XX): ")
            if type(price_limit) == float:
                price_limit = "{:.2f}".format(price_limit)
                break
            else:
                print("Invalid input. Please enter a numeric value")
        limit_order_data = LimitOrderRequest(
            symbol = self.make_order["symbol"],
            qty = self.make_order["qty"],
            side = self.make_order["buy_sell"],
            time_in_force = TimeInForce.DAY,
            limit_price = price_limit
        )
        limit_order = trade_client.submit_order(limit_order_data)
        print(limit_order)
    
    # gives full list of open orders
    def check_open_orders():
        request_params = GetOrdersRequest(
            status = QueryOrderStatus.OPEN
        )
        orders = trade_client.get_orders(request_params)
        return orders

    # cancel open orders
    def cancel_open_orders(self):
        orders = self.open_orders
        if orders is not None:
            for order in orders:
                print(order)
        cancel_order_id = input("Copy and Paste id to cancel: ")
        trade_client.cancel_order_by_id(order_id=cancel_order_id)
        