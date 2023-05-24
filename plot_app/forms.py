from datetime import datetime
from django import forms
import yfinance as yf


class stock_form(forms.Form):
    symbol = forms.CharField(required=True, max_length=10, initial="CADUSD=X")
    period = forms.CharField(required=False, max_length=5)   # 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    start = forms.DateTimeField(required=False, initial=datetime.date.today)
    end = forms.DateTimeField(required=False)
    stock_symbols = [
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
    stonk_select = forms.ChoiceField(stock_symbols)  # takes lists of tuples as value/label pairs.
