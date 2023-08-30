import pandas as pd
import yfinance as yf


class Position:
    symbol = ""
    history = None
    take_profit_value = 0.0
    stop_loss_value = 0.0
    errors = {}

    def __init__(self, symbol):
        self.symbol = symbol
        self.retrieve_single_day()

    def retrieve_single_day(self):
        company = yf.Ticker(self.symbol)
        comp_hist = company.history(period='1d')
        comp_hist_df = pd.DataFrame(comp_hist).reset_index()
        self.history = comp_hist_df

    def take_profit(self, profit_value):
        if profit_value > 0.0:
            self.take_profit_value = profit_value

    def stop_loss(self, loss_value):
        if loss_value >= 0.0:
            self.stop_loss_value = loss_valu


    def advance_time(self):
        original_date = self.history["Date"]
        add_day = original_date + pd.Timedelta(days=1)
        print(add_day)
        return add_day
