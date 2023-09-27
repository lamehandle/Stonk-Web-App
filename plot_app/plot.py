import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import datetime as datetime
from position import Position as pos


class Plot:
    # Plot

    hist = None
    pos = None
    open = None
    close = None
    low = None
    high = None
    fig = None

    def __init__(self, position):
        self.hist = position.history
        self.pos = position.initial_record

        self.open = self.hist['Open']
        self.close = self.hist['Close']
        self.low = self.hist['Low']
        self.high = self.hist['High']

    def plot_history(self):
        if self.hist is not None:
            print("<======== data! =========>")
            self.fig = go.Figure(data=[go.Candlestick(x=self.hist['Date'],
                                                      open=self.open,
                                                      high=self.high,
                                                      low=self.low,
                                                      close=self.close)])

            self.fig.update_layout(xaxis_rangeslider_visible=False)
            self.fig.add_scatter()

            return self.fig.show()
        else:
            return print("<======== No data! =========>")

    def update_position(self, position):
        data = position.history[0, position.index]
        if self.fig is not None:
            if self.pos is not None:
                print("<======== Position data! =========>")
                self.fig.add_trace(go.Scatter(self.pos, x=data["Date"], y=data["Open"]))

            self.fig.show()
        else:
            return print("<======== No Position data! =========>")
