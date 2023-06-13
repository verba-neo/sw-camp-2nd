# util/urls.py
from django.urls import path
from . import views


urlpatterns = [
    # util/lotto/
    path('lotto/', views.lotto),
    # util/kospi/
    path('kospi/', views.kospi),
]