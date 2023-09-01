import pandas as pd
import yfinance as yf
import pandas as pd

class Position:
    symbol = ""
    history = None
    take_profit_value = 0.0
    stop_loss_value = 0.0
    errors = {}
    position_series = {}

    def __init__(self, symbol):
        self.symbol = symbol
        self.retrieve_single_day()

    def retrieve_single_day(self):
        company = yf.Ticker(self.symbol)
        comp_hist = company.history(period='1d')
        comp_hist_df = pd.DataFrame(comp_hist).reset_index()
        self.history = comp_hist_df
        self.position_series = self.history

    def take_profit(self, profit_value):
        if profit_value > 0.0:
            self.take_profit_value = profit_value

    def stop_loss(self, loss_value):
        if loss_value >= 0.0:
            self.stop_loss_value = loss_value

    def advance_time(self):
        original_date = self.history["Date"]
        next_day = original_date + pd.Timedelta(days=1)
        print(next_day)

        company = yf.Ticker(self.symbol)
        comp_hist = company.history(start=original_date, end=next_day)
        comp_hist_df = pd.DataFrame(comp_hist).reset_index()
        self.history = comp_hist_df
        self.position_series = self.history
        # todo this is changing the date rather than pulling new data
        # todo refactor to call retrieve single day again with the new date
        self.position_series = pd.concat([self.position_series, self.history], ignore_index=True)
        return self.history
