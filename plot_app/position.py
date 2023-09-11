import pandas as pd
import yfinance as yf
import pandas as pd
import datetime
from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta


class Position:
    symbol = ""
    history = None
    take_profit_value = 0.0
    stop_loss_value = 0.0
    errors = {}
    position_series = None
    period = '3y'
    single_day = None

    def __init__(self, symbol):
        self.symbol = symbol
        self.retrieve_single_day(symbol)

    def retrieve_single_day(self, symbol):
        hist = yf.Ticker(symbol).history(self.period)
        hist_df = pd.DataFrame(hist).reset_index()
        self.history = hist_df
        self.position_series = self.history
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
        # Take original Datetime from
        original_date = self.history["Date"].iloc[0]
        # current_datetime = datetime.strptime(str(original_date), "%Y-%m-%d %H:%M:%S%z")
        print("<========= v Original Date v ========>")
        print(original_date)

        # next_day = self.history["Date"].iloc[0]
        next_day = (self.history["Date"].iloc[0] + timedelta(days=2))

        print("<========= v New Date + 1 Day v ========>")
        print(next_day)

        self.position_series = yf.Ticker(self.symbol).history(start=original_date, end=next_day).reset_index()
        # , axis = "columns"
        print("<========= v Position Series v ========>")
        print(self.position_series)
