# input/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # input/home/
    path('home/', views.home),
    # input/greeting/neo/
    path('greeting/<str:name>/', views.greeting),
    # input/lotto/100/
    path('lotto/<int:draw_no>/', views.lotto),

    # input/ping/
    path('ping/', views.ping),
    # input/pong/
    path('pong/', views.pong),
]
