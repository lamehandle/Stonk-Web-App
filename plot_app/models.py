from django.db import models


# Create your models here.
class stock(models.Model):
    symbol = models.CharField(max_length=10)
    period = models.CharField(max_length=5)   # 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return f"{self.symbol} {self.period} {self.start}{self.end}"


class user(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_pass = models.CharField(max_length=200)
    stock = models.ForeignKey(stock, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_name} {self.user_email} {self.user_pass} {self.stock}"
