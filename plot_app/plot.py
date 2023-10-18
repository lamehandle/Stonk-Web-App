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
                                                      close=position.history['Close'],
                                                      name=position.symbol + " Stock Price")])

            self.fig.update_layout(xaxis_rangeslider_visible=False,
                                   title="Historical stock data for " + position.symbol,
                                   yaxis_title=position.symbol + "stock price",
                                   xaxis_title="Date")

        else:
            return print("<======== No data! =========>")

    def update_position(self, position):
        self.plot_history(position)
        if self.fig is not None:
            if position.history is not None:
                print("<======== Position data! =========>")
                self.fig.add_trace(
                    go.Scatter(x=position.history["Date"], y=position.history["Open"], mode="lines+markers",
                               name=position.symbol + " Open Position"))

                self.fig.add_trace(
                    go.Scatter(x=position.history["Date"], y=position.history["Close"], mode="lines+markers",
                               name=position.symbol + " Close Position"))

                # todo refactor to provide the rows that match the value.
            if position.take_prof_slice is not None:
                self.fig.add_hline(y=position.take_profit_value, line_dash="dash", opacity=0.5, line_color="blue",
                                   annotation_text="Take Profit Order",
                                   annotation_position="top left",
                                   annotation_font_size=12,
                                   annotation_font_color="blue")

                self.fig.add_trace(
                    go.Scatter(x=position.history["Date"],
                               y=[position.take_prof_slice["Close"]],
                               name="Take Profit (Close)",
                               text="Take Profit",
                               mode="markers+text",
                               ))

            # if position.stop_loss_slice is not None:
                self.fig.add_hline(y=position.stop_loss_value, line_dash="dash", opacity=0.5, line_color="blue",
                                   annotation_text="Stop Loss Order",
                                   annotation_position="top left",
                                   annotation_font_size=12,
                                   annotation_font_color="blue")

                self.fig.add_trace(
                    go.Scatter(x=position.stop_loss_slice["Date"],
                               y=[position.stop_loss_slice["Close"]],
                               name="Stop Loss (Close)",
                               text="Stop Loss",
                               mode="markers+text",
                               ))
                self.fig.show()
        else:
            return print("<======== No Position data! =========>")
