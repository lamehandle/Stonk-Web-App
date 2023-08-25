import pandas as pd
import yfinance as yf
from datetime import date, datetime, timedelta


class User:
    symbol = ""
    bank = 0.0
    invest_funds = 0
    stock_units = 0
    comp_hist_df = None
    companies = []
    errors = {}
    stop_loss = 0.0
    take_profit = 0.0

    def __init__(self, init_bank: float, company_symbol: str):
        self.bank = init_bank
        self.symbol = company_symbol
        self.get_company_hist()

    def get_company_hist(self, ):
        company = self.retrieve_single_day()
        self.companies.append(self.symbol)
        self.comp_hist_df = company

    def retrieve_single_day(self):
        company = yf.Ticker(self.symbol)
        comp_hist = company.history(period='1d')
        comp_hist_df = pd.DataFrame(comp_hist).reset_index()
        self.comp_hist_df = comp_hist_df
        return comp_hist_df

    def purchase_stocks(self, bank, invest_funds):
        if invest_funds <= bank:
            stock_units = invest_funds // self.comp_hist_df["Open"].loc[0]
            # print(str(stock_units) + ' units.')
            cost = stock_units * self.comp_hist_df["Open"].loc[0]
            # print('$' + str(cost))
            self.bank = (bank - cost)
            # print('$' + str(bank) + 'mid-func')
            remaining = invest_funds - cost
        else:
            self.errors = {"fund": "Not enough funds!"}
        return bank

    def invest_amt(self, init_invest: float):
        self.invest_funds = init_invest

    def take_profit(self, profit_value):
        if profit_value > 0.0:
            self.take_profit = profit_value

    def stop_loss(self, loss_value):
        if loss_value >= 0.0:
            self.take_profit = loss_value

    def advance_time(self):
        original_date = self.comp_hist_df["Date"]
        add_day = original_date + pd.Timedelta(days=1)
        print(add_day)
        return add_day

# todo  split User class in to balance and position classes
