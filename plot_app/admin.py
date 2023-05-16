from django.contrib import admin

# Register your models here.
from .models import stock
from .models import user

admin.site.register(stock)
admin.site.register(user)
