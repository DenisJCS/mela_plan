"""Defines URL ptterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'ml_plan'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
]