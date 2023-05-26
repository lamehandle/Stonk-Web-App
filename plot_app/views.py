from django.shortcuts import render
from .forms import stock_form


# Create your views here.
def index(request):
    return render(request, 'plot/index.html')  # call templates here


def about(request):
    return render(request, 'plot/about.html')


def process_stock_view(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = stock_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.cleaned_data()
            # process the data in form.cleaned_data as required
            symbol = form.cleaned_data['symbol']
            period = form.cleaned_data['period']
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']
            # make a dict to pass this data into the template
            data = {
                'symbol': symbol,
                'period': period,
                'start': start,
                'end': end,
            }

            # todo wire this up in the template then worry about these advances settings.
            # history = yf.Ticker(symbol).history(period)
            # history_flat = history.reset_index()
            # date = history_flat['Date']
            # open = history['Open']
            # high = history['High']
            # low = history['Low']
            # close = history['Close']
            # volume = history['volume']
            # dividends = history['dividends']
            # splits = history['splits']

            # redirect to a new URL:
            return render(request, "process_stock.html", {'data': data})
            # replace this third argument with a
            # dictionary ('key': 'value' pairs) to create the context for the template.

        # if a GET (or any other method) we'll create a blank form
        else:
            form = stock_form()
            return render(request, '"process_stock.html', {'form': form})
