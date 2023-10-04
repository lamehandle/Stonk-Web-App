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

    take_profit_value = 0.0
    stop_loss_value = 0.0

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

    def take_profit(self, balance):
        close_val = self.history.iloc[self.index]["Close"]
        if balance.unit_cost >= 0.0:
            self.take_profit_value >= close_val
            balance.cash_out(self, close_val)

        else:
            return "Take Profit Order must be greater than 0."

    #         # todo implement take profit/profit loss match logic

    def stop_loss(self, loss_value):
        close_val = self.history.iloc[self.index]["Close"]
        if loss_value >= 0.0:
            self.stop_loss_value = close_val
            # todo implement stop loss match logic
        else:
            return "Stop Loss Order must be 0 or greater."

    def advance_record(self):
        if self.initial_record is not None:
            # self.prev_date = self.initial_record
            self.calc_date()
        print("<========= v New Record v ========>")
        print(self.next_day)

    def calc_date(self):
        self.index = self.index + 1
        self.next_day = self.history.iloc[self.index]
