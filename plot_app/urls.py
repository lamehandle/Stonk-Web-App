from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='plot_app-home'),
    path('about', views.about, name='plots-about'),
    path('process_stock/', views.process_stock_view, name='plot-process-form'),
]

#  The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.

