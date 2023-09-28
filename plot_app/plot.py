import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import datetime as datetime
from position import Position as pos


class Plot:
    # Plot
    fig = None
    index = None
    
    def __init__(self, position):
        self.index = position.index

    def plot_history(self, position):
        if position is not None:
            print("<======== data! =========>")
            self.fig = go.Figure(data=[go.Candlestick(x=position.history['Date'],
                                                      open=position.history['Open'],
                                                      high=position.history['High'],
                                                      low=position.history['Low'],
                                                      close=position.history['Close'])])

            self.fig.update_layout(xaxis_rangeslider_visible=False)
            return self.fig.show()
        else:
            return print("<======== No data! =========>")

    def update_position(self, position):
        if self.fig is not None:
            if position.history is not None:
                print("<======== Position data! =========>")
                self.fig.add_trace(
                    go.Scatter(x=position.history["Date"], y=position.history["Open"],))
                self.fig.show()
        else:
            return print("<======== No Position data! =========>")
