import pandas as pd
import yfinance as yf
from datetime import timedelta, datetime


class Position:
    symbol = ""
    history = None
    period = '1mo'

    index = 0
    initial_record = None
    prev_date= None
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

    def retrieve_initial_day(self):
        self.initial_record = self.history.iloc[0, :]  # todo confirm that this is the frst row of the history dataframe
    #                                           .iloc[rows, columns]

    def take_profit(self, profit_value):
        if profit_value > 0.0:
            self.take_profit_value = profit_value

    def stop_loss(self, loss_value):
        if loss_value >= 0.0:
            self.stop_loss_value = loss_value

    def advance_time(self):
        print("<========= v History v ========>")
        print(self.history)
        # todo walk down the history dataframe one element at a time.
        if self.initial_record is not None:
            self.calc_date(self.index)

        print("<========= v New Date v ========>")
        print(self.next_day.loc["Date"])

    def calc_date(self, index):
        print("<========= v Original Date v ========>")
        print(self.initial_record["Date"])
        self.index = self.index + 2
        self.next_day = self.history.iloc[index]
