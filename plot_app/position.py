import pandas as pd
import yfinance as yf
from datetime import timedelta, datetime


class Position:
    symbol = ""
    history = None
    take_profit_value = 0.0
    stop_loss_value = 0.0
    errors = {}
    position_history = None
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
        self.position_history = self.history.tail(1)
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
        print("<========= v Original History v ========>")
        print(self.history.head())

        # Take original Datetime from history
        # todo this if statement is not working as expected. I think I need to create a flag/counter to track days advanced and walk down the history dataframe
        if self.original_date is not None:
            #  todo need to set up so that after the first iteration it uses the time series to calculate original date.
            original_date = self.original_date.head(1)

        else:
            original_date = self.history["Date"].head(1)
            self.original_date = original_date

        print("<========= v Original Date v ========>")
        print(original_date)

        next_day = original_date + timedelta(days=2)

        print("<========= v New Date v ========>")
        print(next_day)
        #                                          start is inclusive;   end is exclusive.
        #                                                      |             |
        new_range = yf.Ticker(self.symbol).history(start=original_date.iloc[0], end=next_day.iloc[0]).reset_index()

        self.position_history = new_range
        print("<========= v Position Series v ========>")
        print(self.position_history)
