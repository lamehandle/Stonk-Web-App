from django.http import HttpResponse
from django.shortcuts import render
from .forms import stock_form
from balance import Balance
from position import Position
from plot import Plot


def index(request):
    if request.method == 'POST':
        form = stock_form(request.POST)
        if form.is_valid():
            data = {
                'selected_stock': form.cleaned_data['select'],
                'selected_period': form.cleaned_data['period'],
                'start_date': form.cleaned_data['start'],
                'end_date': form.cleaned_data['end'],
                'stop_loss': form.cleaned_data['stop_loss_order'],
                'take_profit': form.cleaned_data['take_profit_order'],
                'bank_amt': form.cleaned_data['bank_amt'] | 10000.00,
                'invest_amt': form.cleaned_data['invest_amt'] | 2000.00,
                'stock_units': 0.0,
            }

            # todo I may need to

            # create instance of balance
            bank = Balance(data['bank_amt'])
            bank.invest(data['invest_amt'])
            # create instance of position
            usr_pos = Position(data['selected_stock'])

            # Create plot and pass the data to the renderer

            return render(request, "index.html", {'data': data})
    else:
        form = stock_form
        return render(request, "index.html", {'form': form})

