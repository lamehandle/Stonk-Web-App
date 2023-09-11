import pandas as pd
import yfinance as yf
import pandas as pd
import datetime
from datetime import timedelta, datetime


class Position:
    symbol = ""
    history = None
    take_profit_value = 0.0
    stop_loss_value = 0.0
    errors = {}
    position_time_series = None
    period = '3mo'
    single_day = None

    def __init__(self, symbol):
        self.symbol = symbol
        self.retrieve_single_day(symbol)

    def retrieve_single_day(self, symbol):
        hist = yf.Ticker(symbol).history(self.period)
        hist_df = pd.DataFrame(hist).reset_index()
        self.history = hist_df
        self.position_time_series = self.history
        self.strip_first_day()

    def strip_first_day(self):
        self.single_day = self.history.iloc[0]

    def take_profit(self, profit_value):
        if profit_value > 0.0:
            self.take_profit_value = profit_value

    def stop_loss(self, loss_value):
        if loss_value >= 0.0:
            self.stop_loss_value = loss_value

    def advance_time(self, date=None):
        # print("<========= v Original History v ========>")
        # print(self.history)

        # Take original Datetime from history
        if date is not None:
            #  todo need to set up so that after the first iteration it uses the time series to calculate original date.
            original_date = self.position_time_series[-1]
        else:
            original_date = self.history["Date"].iloc[0]

        print("<========= v Original Date v ========>")
        print(original_date)

        next_day = (self.history["Date"].iloc[0] + timedelta(days=2))

        print("<========= v New Date v ========>")
        print(next_day)
        #                                                          start is inclusive;   end is exclusive.
        #                                                                     |             |
        self.position_time_series = yf.Ticker(self.symbol).history(start=original_date, end=next_day,
                                                                   prepost=True).reset_index()

        print("<========= v Position Series v ========>")
        print(self.position_time_series)
