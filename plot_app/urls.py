from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='plot_app-home'),
    path('about', views.about, name='plots-about'),
    path('plot_app/', views.plot, name='plots-plot_app'),
]

#  The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.
#  At this point, it’s worth reviewing what these arguments are for.
