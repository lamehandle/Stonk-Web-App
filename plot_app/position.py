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
    period = '1d'

    def __init__(self, symbol):
        self.symbol = symbol
        self.retrieve_single_day(symbol)

    def retrieve_single_day(self, symbol):
        hist = yf.Ticker(symbol).history(self.period)
        hist_df = pd.DataFrame(hist).reset_index()
        self.history = hist_df
        self.position_series = self.history

    def take_profit(self, profit_value):
        if profit_value > 0.0:
            self.take_profit_value = profit_value

    def stop_loss(self, loss_value):
        if loss_value >= 0.0:
            self.stop_loss_value = loss_value

    def advance_time(self):
        # Take original Datetime from
        original_date = self.history["Date"].iloc[0]
        current_datetime = datetime.strptime(str(original_date), "%Y-%m-%d %H:%M:%S%z")
        print("<========= v Original Date v ========>")
        print(original_date)

        next_day = (current_datetime + timedelta(days=1))
        # todo fix not advancing a day!
        # need to convert this to an acceptable datetime string

        print("<========= v New Date v ========>")
        print(next_day)

        print("<========= v Original History v ========>")
        print(self.history)

        new_hist = yf.Ticker(self.symbol).history(start=next_day).reset_index()
        # think I need to format the dates
        # hist_df = pd.DataFrame(new_hist).reset_index()
        print("<========= v New History v ========>")
        print(new_hist)
        # print(hist_df)
        self.position_series = pd.concat([self.history, new_hist], axis="rows", ignore_index=True)
        # , axis = "columns"
        print(self.position_series)
        # comp_hist_df = pd.DataFrame(new_hist).reset_index()
        # self.history = comp_hist_df
        # self.position_series = self.history
        # # todo this is changing the date rather than pulling new data
        # # todo refactor to call retrieve single day again with the new date
        # self.position_series = pd.concat([self.position_series, self.history], ignore_index=True)
        # return self.position_series.all()
