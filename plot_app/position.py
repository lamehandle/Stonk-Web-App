import pandas as pd
import yfinance as yf
from datetime import timedelta


class Position:
    symbol = ""
    history = None
    take_profit_value = 0.0
    stop_loss_value = 0.0
    errors = {}
    position_time_series = None
    period = '3mo'
    single_day = None
    original_date = None
    next_day = None

    def __init__(self, symbol):
        self.symbol = symbol
        self.retrieve_single_day(symbol)

    def retrieve_single_day(self, symbol):
        hist = yf.Ticker(symbol).history(self.period)
        hist_df = pd.DataFrame(hist).reset_index()
        self.history = hist_df
        self.position_time_series = self.history.tail(1)
        self.strip_first_day()

    def strip_first_day(self):
        self.single_day = self.history.iloc[0]

    def take_profit(self, profit_value):
        if profit_value > 0.0:
            self.take_profit_value = profit_value

    def stop_loss(self, loss_value):
        if loss_value >= 0.0:
            self.stop_loss_value = loss_value

    def advance_time(self):
        # print("<========= v Original History v ========>")
        # print(self.history)

        # Take original Datetime from history
        if self.original_date is not None:
            #  todo need to set up so that after the first iteration it uses the time series to calculate original date.
            self.original_date = self.position_time_series['Date'].tail(1)
        else:
            self.original_date = self.history["Date"].iloc[0]

        print("<========= v Original Date v ========>")
        print(self.original_date)

        self.next_day = self.original_date + timedelta(days=2)

        print("<========= v New Date v ========>")
        print(self.next_day)
        #                                                          start is inclusive;   end is exclusive.
        #                                                                     |             |
        self.position_time_series = yf.Ticker(self.symbol).history(start=self.original_date, end=self.next_day,
                                                                   prepost=True).reset_index()

        print("<========= v Position Series v ========>")
        print(self.position_time_series)
