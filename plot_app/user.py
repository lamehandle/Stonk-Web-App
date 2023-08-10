import pandas as pd
import yfinance as yf


class User:
    bank = 10000.00
    invest_funds = 0
    stock_units = 0
    comp_hist_df = {}
    companies = []
    errors = []
    stop_loss = 0.0
    take_profit = 0.0


def __init__(self, bank, invest_funds, company_symbol):
    self.bank = bank
    self.invest_funds = invest_funds
    self.get_company(company_symbol,bank, invest_funds)


def get_company(self, symbol, bank=0.0, invest_funds=0.0, ):
    company = self.retrieve_single_day(symbol)
    self.companies.append(company)
    self.comp_hist_df = company


def retrieve_single_day(symbol):
    company = yf.Ticker(symbol)
    comp_hist = company.history(period='1d')
    comp_hist_df = pd.DataFrame(comp_hist).reset_index()
    return comp_hist_df


def purchase_stocks(self, bank, invest_funds, comp_hist_df):
    if invest_funds <= bank:
        stock_units = invest_funds // comp_hist_df["Open"].loc[0]
        # print(str(stock_units) + ' units.')
        cost = stock_units * comp_hist_df["Open"].loc[0]
        # print('$' + str(cost))
        self.bank = (bank - cost)
        # print('$' + str(bank) + 'mid-func')
        remaining = invest_funds - cost
    else:
        self.errors.append("fund",  "Not enough funds!")

    return bank


def take_profit(self, profit_value):
    if profit_value > 0.0:
        self.take_profit = profit_value


def stop_loss(self, loss_value):
    if loss_value
    self.take_profit = loss_value
