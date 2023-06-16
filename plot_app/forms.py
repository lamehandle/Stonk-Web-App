from datetime import datetime
from django import forms


class stock_form(forms.Form):
    symbols = [
        ('Enter a Stock','Select a Stock'),
        ('CADUSD=X', 'USD / CAD'),
        ('XIU.TO', 'iShares S&P/TSX 60 Index ETF'),
        ('GC=F', 'Gold Futures'),
        ('^GSPTSE', 'S&P/TSX Composite index'),
        ('^GSPC', '	S&P 500'),
        ('^DJI', 'Dow Jones Industrial Average'),
        ('^IXIC', 'NASDAQ Composite'),
        ('^NYA', 'NYSE COMPOSITE (DJ)'),
        ('^XAX', 'NYSE AMEX COMPOSITE INDEX'),
        ('^RUT', 'Russell 2000'),
        ('^VIX', '	CBOE Volatility Index'),
        ('^FTSE', 'FTSE 100'),
        ('^GDAXI', 'DAX PERFORMANCE-INDEX'),
        ('^FCHI', 'CAC 40'),
    ]
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
    select = forms.ChoiceField(label='Stock Select:', choices=symbols)  # takes lists of tuples as value/label pairs.
    symbol = forms.CharField(label='Symbol:', required=False, max_length=20, widget=forms.TextInput(
        {'placeholder': 'Enter a Stock Symbol'}))
    period = forms.ChoiceField(label='Select Period:', choices=periods, required=False, initial=periods[11])
    start = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'class': 'startDate', }),
        label='Start Date', required=False)
    end = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'endDate', 'type': 'date'}),
        label='End Date', required=False)


def __init__(self, *args, **kwargs):
    super().__init__( *args, **kwargs)
    self.fields['symbol'] = self.fields['select']

