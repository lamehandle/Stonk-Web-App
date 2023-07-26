import yfinance as yf
import pandas as pd
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


def retrieve_company_data():
    print("<==================== imported ===============================>")
    company_symbol = input("Select a company using their stock symbol: ")
    company = yf.Ticker(company_symbol)
    print("<==================== imported ==========================>")
    print("do you have a start and end date?")
    use_period = input('Y or N: ')
    if use_period.capitalize() == 'N':
        print("Available timeframes are:")
        # period: data period to download (Either Use period parameter or use start and end) Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
        # interval: data interval (intraday data cannot extend last 60 days) Valid intervals are: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
        print("1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max")
        period = input("your period: ")
        comp_hist = company.history(period=period)
        comp_hist_df = pd.DataFrame(comp_hist).reset_index()
        print(comp_hist_df)
        print("<===================== Company Data Retrieved! ==========================>")
        return comp_hist_df
    else:
        # start: If not using period - Download start date string (YYYY-MM-DD) or datetime.
        start_date = date.fromisoformat(input("enter the start date (YYYY-MM-DD): "))
        # end: If not using period - Download end date string (YYYY-MM-DD) or datetime.
        end_date = date.fromisoformat(input("enter the end date (YYYY-MM-DD): "))
        comp_hist = company.history(start=start_date, end=end_date)
        comp_hist_df = pd.DataFrame(comp_hist).reset_index()
        print(comp_hist_df)
        print("<===================== Company Data Retrieved! ==========================>")
        return comp_hist_df


def retrieve_single_day():
    print("<==================== importing ===============================>")
    company_symbol = input("Select a company using their stock symbol: ")
    company = yf.Ticker(company_symbol)
    print("<==================== imported ==========================>")
    print("do you have a start and end date?")
    use_period = input('Y or N: ')
    if use_period.capitalize() == 'N':
        comp_hist = company.history(period='1d')
        comp_hist_df = pd.DataFrame(comp_hist).reset_index()
        print(comp_hist_df)
        print("<===================== Company Data Retrieved! ==========================>")
        return comp_hist_df
    else:
        return retrieve_by_date(company)


def retrieve_by_date(company):
    # start: If not using period - Download start date string (YYYY-MM-DD) or datetime.
    start_date = pd.to_datetime(input("enter the start date (YYYY-MM-DD): "))
    end_date = start_date + pd.Timedelta(days=1)
    comp_hist = company.history(start=start_date, end=end_date)
    comp_hist_df = pd.DataFrame(comp_hist).reset_index()
    print(comp_hist_df)
    print("<===================== Company Data Retrieved! ==========================>")
    return comp_hist_df


def advance_time(comp_hist_df):
    original_date = comp_hist_df["Date"]
    add_day = original_date + pd.Timedelta(days=1)
    print(add_day)
    return add_day

