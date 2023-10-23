from django.contrib import admin
from django.urls import path
from . import views

app_name = 'plot'

urlpatterns = [
    path('', views.index, name='plot-home'),
    path('plot-chart', views.chart_view, name='plot-chart'),
    path('about/', views.about, name='plot-about'),
    path('process_stock/', views.process_stock_view, name='plot-process-form'),

]

#  The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.

