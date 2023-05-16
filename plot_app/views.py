from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'plot/index.html')  # call templates here


def about(request):
    return render(request, 'plot/about.html')


def plot(request):
    return render(request, 'plot_app/ploy.py')


def process_stock(request):
    return render(request, 'plot_app/process_stock.py')
