import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import datetime as datetime
from position import Position as pos


class Plot:
    # dataframe for plotting
    hist = None
    pos = None
    open = None
    close = None
    low = None
    high = None

    def __init__(self, position):
        self.hist = position.history
        self.pos = position.position_time_series

        self.open = self.hist['Open']
        self.close = self.hist['Close']
        self.low = self.hist['Low']
        self.high = self.hist['High']

    def plot_history(self):
        if self.hist is not None:
            print("<======== data! =========>")
            fig = go.Figure(data=[go.Candlestick(x=self.hist['Date'],
                                                 open=self.open,
                                                 high=self.high,
                                                 low=self.low,
                                                 close=self.close)])

            return fig.show()
        else:
            return print("<======== No data! =========>")

    def plot_position(self):
        if self.pos is not None:
            print("<======== Position data! =========>")
            fig = go.Figure(data=[go.Candlestick(x=self.pos['Date'],
                                                 open=self.pos['Open'],
                                                 high=self.pos['High'],
                                                 low=self.pos['Low'],
                                                 close=self.pos['Close'])])

            return fig.show()
        else:
            return print("<======== No Position data! =========>")