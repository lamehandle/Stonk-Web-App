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

    def update_position(self):
        if self.fig is not None:
            if self.pos is not None:
                print("<======== Position data! =========>")
                self.fig.add_trace(go.Scatter(self.pos, x=self.pos["Date"], y=self.pos["Open"]))
                self.fig.update_traces(marker=dict(size=12,
                                                   line=dict(width=2,
                                                             color="DarkSlateGrey")),
                                       selector=dict(mode="markers"))
                self.fig.show()
        else:
            return print("<======== No Position data! =========>")

            # Low level example of a figure which is a dict
            # fig = dict({
            #     "data": [{"type": "bar",
            #               "x": [1, 2, 3],
            #               "y": [1, 3, 2]}],
            #     "layout": {"title": {"text": "A Figure Specified By Python Dictionary"}}
            # })
            #
            # # To display the figure defined by this dict, use the low-level plotly.io.show function
            # import plotly.io as pio
            #
            # pio.show(fig)
