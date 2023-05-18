import plotly.graph_objects as go
import yfinance as yf

# todo I think I need to turn this into a Django model
class Stock:
    symbol = ''  # string representation of stock ticker symbol
    data = ''  # A Ticker object using the symbol passed.
    history = ''
    # interval = ''  # data interval (intraday data cannot extend last 60 days)
    # Valid intervals are: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo.
    period = ''  # data period to download (Either Use period parameter or use start and end)
    # Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max.
    # start = ''  # If not using period - Download start date string (YYYY-MM-DD) or datetime.
    # end = ''  # If not using period - Download end date string (YYYY-MM-DD) or datetime.

    def __init__(self, symbol, period='', start='', end=''):
        self.symbol = symbol
        self.data = yf.Ticker(symbol)
        self.history = self.history()

    def history(self, period='', start='', end=''):
        if period != '':
            self.history = self.data.history(period=self.period)
        else:
            self.history = self.data.history(start=start, end=end)

    def stock_info(self):
        return self.data.info


class Plotter:
    Stock

    def __int__(self, stock):
        self.stock = stock.reset_index()

    def plot(self):
        fig = go.Figure(data=[go.Candlestick(x=self.stock['Date'],
                                         open=self.stock['Open'],
                                         high=self.stock['High'],
                                         low=self.stock['Low'],
                                         close=self.stock['Close'],
        )])
        fig.show()
