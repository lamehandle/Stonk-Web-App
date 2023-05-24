from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import stock_form
import yfinance as yf


# Create your views here.
def index(request):
    return render(request, 'plot/index.bak.html')  # call templates here


def about(request):
    return render(request, 'plot/about.html')


def plot(request):
    return render(request, 'plot_app/ploy.py')


def process_stock_view(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = stock_form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.cleaned_data()
            # process the data in form.cleaned_data as required
            symbol = form.fields['symbol']
            period = form.fields['period']
            start = form.fields['start']
            end = form.fields['end']

            history = yf.Ticker(symbol).history(period)
            history_flat = history.reset_index()
            date = history_flat['Date']
            open = history['Open']
            high = history['High']
            low = history['Low']
            close = history['Close']
            volume = history['volume']
            dividends = history['dividends']
            splits = history['splits']

            # redirect to a new URL:
            return render(request, "process_stock.html", {'form': form})

        # if a GET (or any other method) we'll create a blank form
        else:
            form = stock_form()
            return render(request, 'plot_app/process_stock.py', {'form': form})



