# first_app/urls.py
from django.urls import path
from . import views

# 반드시 아래 이름의 list 필요
urlpatterns = [
    path('hello/', views.hello),
    path('home/', views.home),
]