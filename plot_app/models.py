from datetime import datetime
from django.db import models
import yfinance as yf


# Create your models here.
class stock(models.Model):
    symbol = models.CharField(max_length=10, initial="CADUSD=X")
    period = models.CharField(max_length=5)   # 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    start = models.DateTimeField(required=False, initial=datetime.date.today)
    end = models.DateTimeField(required=False)
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
    stonk_select = models.Choices(stock_symbols)  # takes lists of tuples as value/label pairs.
    history = ''

    def __str__(self):
        return f"{self.symbol} {self.period} {self.start}{self.end}"

    def stock_history(self):
        if self.period != '':
            self.history = yf.Ticker(self.symbol).history(period=self.period)
        else:
            self.history = yf.Ticker(self.symbol).history(start=self.start, end=self.end)


class user(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_pass = models.CharField(max_length=200)
    stock = models.ForeignKey(stock, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_name} {self.user_email} {self.user_pass} {self.stock}"
