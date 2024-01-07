from datetime import datetime
from django import forms
from .stock_symbols import stock_symbols


class stock_form(forms.Form):
    companies = stock_symbols
    periods = [('', 'None'),
               ('1-day', '1d'),
               ('5-day', '5d'),
               ('30-day', '1mo'),
               ('90-day', '3mo'),
               ('6-months', '6mo'),
               ('1-year', '1y'),
               ('2-years', '2y'),
               ('5-years', '5y'),
               ('10-years', '10y'),
               ('year-to-date', 'ytd'),
               ('Max', 'max'),
               ]
    select = forms.ChoiceField(label='Stock Select:', choices=companies)  # takes lists of tuples as value/label pairs.
    # symbol = forms.CharField(label='Symbol:', required=False, max_length=20, widget=forms.TextInput(
    #     {'placeholder': 'Enter a Stock Symbol'}))
    period = forms.ChoiceField(label='Select Period:', choices=periods, required=False, initial=periods[11])
    start = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'startDate', }),
        label='Start Date', required=False)
    end = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'endDate', 'type': 'date'}),
        label='End Date', required=False)
    stop_loss_order = forms.DecimalField(label='Stop Loss Order:', required=False, min_value=0.0,
                                         widget=forms.NumberInput(
                                             {'placeholder': 'Enter a Stop Loss Order Trigger value'}))
    take_profit_order = forms.DecimalField(label='Take Profit Order:', required=False, min_value=0.0,
                                           widget=forms.NumberInput({'placeholder': 'Enter a Take loss Trigger value'}))
