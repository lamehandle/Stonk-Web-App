import pandas as pd
import yfinance as yf
from datetime import timedelta, datetime


class Position:
    symbol = ""
    history = None
    period = '1mo'

    index = 0
    initial_record = None
    prev_date = None
    next_day = None

    # values
    take_profit_value = None
    stop_loss_value = None

    # dataframe slices
    take_prof_slice = None  # slice of self.history based on take_profit_value
    stop_loss_slice = None  # slice of self.history based on stop_loss_value

    def __init__(self, symbol):
        self.symbol = symbol
        self.retrieve_history()
        self.retrieve_initial_day()

    def __str__(self):
        pass

    def retrieve_history(self):
        self.history = yf.Ticker(self.symbol).history(self.period).reset_index()
        print("<========= v Company History v ========>")
        print(self.history)

    def retrieve_initial_day(self):
        self.initial_record = self.history.iloc[self.index]
        print("<========= v Original Record v ========>")
        print(self.initial_record)

    def set_take_profit(self, value):
        self.take_profit_value = value

    def set_stop_loss(self, value):
        self.stop_loss_value = value

    def take_profit(self, balance):
        close_val = self.history.iloc[self.index]["Close"]
        if balance.stock_units > 0:
            if self.take_profit_value:
                balance.cash_out(self, close_val)
                self.take_prof_slice = self.history[self.history["Close"].ge(self.take_profit_value) | self.history["Open"].ge(self.take_profit_value)]
                print("Take profit rows")
                print(self.take_prof_slice)
        else:
            return "Take Profit Order must be $0.00 or greater."

    def stop_loss(self, balance):
        close_val = self.history.iloc[self.index]["Close"]
        if balance.stock_units > 0.0:
            if self.stop_loss_value <= close_val:
                balance.cash_out(self, close_val)
            self.stop_loss_slice = self.history[self.history["Close"].le(self.stop_loss_value) | self.history["Open"].le(self.stop_loss_value)]
            print("Stop Loss rows")
            print(self.stop_loss_slice)
        else:
            return "Stop Loss Order must be $0.00 or greater."

    def advance_record(self):
        if self.initial_record is not None:
            # self.prev_date = self.initial_record
            self.calc_date()
        print("<========= v New Record v ========>")
        print(self.next_day)

    def calc_date(self):
        self.index = self.index + 1
        self.next_day = self.history.iloc[self.index]

    def match_records(self, match):

        if self.history:
            return self.history.where(self.history == match)
        else:
            return "No records to filter."
#       todo create filtering logic
