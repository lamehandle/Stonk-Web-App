import pandas as pd
import yfinance as yf


class Position:
    symbol = ""
    comp_hist_df = None
    take_profit = 0.0
    stop_loss = 0.0
    errors = {}

    def __init__(self, symbol):
        self.symbol = symbol
        self.retrieve_single_day()

    def retrieve_single_day(self):
        company = yf.Ticker(self.symbol)
        comp_hist = company.history(period='1d')
        comp_hist_df = pd.DataFrame(comp_hist).reset_index()
        self.comp_hist_df = comp_hist_df

    def take_profit(self, profit_value):
        set_stop_loss = float(input("Enter Take Profit dollar amount: $ "))
        self.user["take_profit"] = set_stop_loss
        if profit_value > 0.0:
            self.take_profit = profit_value

    def stop_loss(self, loss_value):
        set_stop_loss = float(input("Enter Stop Loss dollar amount: $ "))
        self.user["stop_loss"] = set_stop_loss
        if loss_value >= 0.0:
            self.stop_loss = loss_value

    def advance_time(self):
        original_date = self.comp_hist_df["Date"]
        add_day = original_date + pd.Timedelta(days=1)
        print(add_day)
        return add_day
