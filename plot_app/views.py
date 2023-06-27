from django.shortcuts import render
from .forms import stock_form
import yfinance as yf
import plotly.graph_objects as go


def index(request):
    form = stock_form()
    return render(request, 'plot/index.html', {'form': form})  #


def about(request):
    return render(request, 'plot/about.html')


def process_stock_view(request):

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = stock_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # Dict to pass this data into the template
            if not form.cleaned_data['select']:
                symbol = form.cleaned_data['symbol']
            else:
                symbol = form.cleaned_data['select']

        data = {
                'symbol': symbol,
                'period': form.cleaned_data['period'],
                'start': form.cleaned_data['start'],
                'end': form.cleaned_data['end'],
        }

        if not data['period']:
            chart_data = yf.download(tickers=data['symbol'], start=['start'], end=data['end'])
        else:
            chart_data = yf.download(data['symbol'], period=data['period'])

        chart_data = chart_data.reset_index()
        x_axis = chart_data['Date']
        y_axis = chart_data['Volume']
        chart = go.Figure(data=[go.Candlestick(x=chart_data.index,
            open=chart_data['Open'],
            high=chart_data['High'],
            low=chart_data['Low'],
            close=chart_data['Close'],
                ),
            ]
        )

        chart.show()

        return render(request, "plot/index.html", {'data': data})
        # replace this third argument with the Dict above
        # ('key': 'value' pairs) to create the context for the template.
        # In this case reference {{data}} in the template

        # if a GET (or any other method) we'll create a blank form
    else:
        form = stock_form()
        return render(request, 'plot/index.html', {'form': form})

