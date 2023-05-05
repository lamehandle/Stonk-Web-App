from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='plot_app-home'),
    path('about', views.about, name='plots-about'),
    path('plot_app/', views.plot, name='plots-plot_app'),
]
