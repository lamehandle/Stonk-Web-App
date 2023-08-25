import pandas as pd
import yfinance as yf


class Position:
    symbol = ""
    comp_hist_df = None
    take_profit = 0.0
    stop_loss = 0.0
    errors = {}

    def __init__(self):
        self.symbol = input("Enter the company symbol ")
        self.retrieve_single_day()

    def retrieve_single_day(self):
        company = yf.Ticker(self.symbol)
        comp_hist = company.history(period='1d')
        comp_hist_df = pd.DataFrame(comp_hist).reset_index()
        self.comp_hist_df = comp_hist_df

    def advance_time(self):
        original_date = self.comp_hist_df["Date"]
        add_day = original_date + pd.Timedelta(days=1)
        print(add_day)
        return add_day

    def take_profit(self, profit_value):
        take_profit_flag = input("Do you wish to set a Take Profit Order? Y/N").upper()
        if take_profit_flag == "Y":
            set_stop_loss = float(input("Enter Take Profit dollar amount: $ "))
            self.user["take_profit"] = set_stop_loss
        else:
            self.user["take_profit"] = 0.0

        if profit_value > 0.0:
            self.take_profit = profit_value

    def stop_loss(self, loss_value):
        stop_loss_flag = input("Do you want to set a Stop Loss amount? Y/N").upper()
        if stop_loss_flag == "Y":
            set_stop_loss = float(input("Enter Stop Loss dollar amount: $ "))
            self.user["stop_loss"] = set_stop_loss
        else:
            self.user["stop_loss"] = 0.0

        if loss_value >= 0.0:
            self.stop_loss = loss_value
