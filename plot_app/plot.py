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

    def __init__(self, position):
        self.hist = position.history
        self.pos = position.position_history

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

            fig.update_layout(xaxis_rangeslider_visible=False)
            fig.add_scatter()

            # fig.add_candlestick(x=self.pos['Date'],
            #                     open=self.pos['Open'],
            #                     high=self.pos['High'],
            #                     low=self.pos['Low'],
            #                     close=self.pos['Close'])
            # fig.add_trace()
            return fig.show()
        else:
            return print("<======== No data! =========>")

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

    def plot_position(self):
        if self.pos is not None:
            print("<======== Position data! =========>")
            fig = go.Figure(data=[go.Candlestick(x=self.pos['Date'],
                                                 open=self.pos['Open'],
                                                 high=self.pos['High'],
                                                 low=self.pos['Low'],
                                                 close=self.pos['Close'])])
            fig.update_layout(xaxis_rangeslider_visible=False)
            return fig.show()
        else:
            return print("<======== No Position data! =========>")
