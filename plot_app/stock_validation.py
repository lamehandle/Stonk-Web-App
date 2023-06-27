from django.shortcuts import render
from .forms import stock_form
import yfinance as yf
import plotly.graph_objects as go


# todo refactor to use dash
def stock_validation(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = stock_form(request.POST)
        # check whether it's valid:
        print(form.cleaned_data)

        if form.is_valid():
            # Dict to pass this data into the template
            if not form.cleaned_data['symbol'].empty:
                symbol = form.cleaned_data['symbol']
            else:
                symbol = form.cleaned_data['select']

            data = {
                'symbol':  form.cleaned_data['select'],
                'period': form.cleaned_data['period'],
                'start': form.cleaned_data['start'],
                'end': form.cleaned_data['end'],
                'stop_loss_order': form.cleaned_data['stop_loss_order'],
                'take_profit_order': form.cleaned_data['take_profit_order'],
            }

            chart = yf.Ticker(data['symbol'])

            if not data['period']:
                chart.history(start=data['start'], end=data['end'])
            else:
                chart.history(period=data['period'])

            chart = chart.reset_index()

            x_axis = chart['Date']
            y_axis = chart['Volume']
            chart = go.Figure(data=[go.Candlestick(title=chart['symbol'], x=chart.index,
                                                   open=chart['Open'],
                                                   high=chart['High'],
                                                   low=chart['Low'],
                                                   close=chart['Close'],
                                                   )])

            chart.update_layout(title=chart['symbol'] + " Stock data",
                                y_axis_title='Price',

                                )

            chart.show()
    else:
        form = stock_form()
        return render(request, 'plot/index.html', {'form': form})