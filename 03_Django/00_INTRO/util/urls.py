# util/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('lotto/', views.lotto),
    path('kospi/', views.kospi),
]