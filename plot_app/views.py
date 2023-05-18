from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NameForm  # todo rename NameForm to my forms name
from .models import stock
# Create your views here.
def index(request):
    return render(request, 'plot/index.html')  # call templates here


def about(request):
    return render(request, 'plot/about.html')


def plot(request):
    return render(request, 'plot_app/ploy.py')


def process_stock(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        form = stock(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")
        # if a GET (or any other method) we'll create a blank form
        else:
        form = NameForm()


return render(request, "name.html", {"form": form})
    return render(request, 'plot_app/process_stock.py', raw_post_data)
