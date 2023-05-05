import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yfinance as yf


period = "1mo"  # Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max:

amzn = yf.Ticker("AMZN").history(period)
amzn = amzn.reset_index()

dow = yf.Ticker("^DJI").history(period)
dow = dow.reset_index()  # reset_index returns a new dataframe

us_cad = yf.Ticker('CADUSD=X').history(period)
us_cad = us_cad.reset_index()

# # Plot a candle stick plot with plotly
fig = make_subplots(rows=1, cols=2)
fig.add_trace(
    go.Candlestick(x=dow['Date'],
        open=dow['Open'],
        high=dow['High'],
        low=dow['Low'],
        close=dow['Close'],
    ), row=1, col=1)

fig.add_trace(
    go.Candlestick(x=amzn['Date'],
        open=amzn['Open'],
        high=amzn['High'],
        low=amzn['Low'],
        close=amzn['Close'],
    ), row=1, col=2)

fig.show()

fig2 = go.Figure(data=[go.Candlestick(x=us_cad['Date'],
        open=us_cad['Open'],
        high=us_cad['High'],
        low=us_cad['Low'],
        close=us_cad['Close'],
    )])
fig2.show()
