from datetime import datetime
from django import forms


class stock_form(forms.Form):
    symbols = [
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
    select = forms.ChoiceField(label='Symbol', choices=symbols)  # takes lists of tuples as value/label pairs.
    symbol = forms.CharField(label='Symbol', required=True, max_length=20, initial="CADUSD=X")
    period = forms.CharField(label='Symbol', required=False, max_length=5)   # 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    start = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'startDate'}),
        label='Start Date', required=False)
    end = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'endDate'}),
        label='End Date', required=False)



