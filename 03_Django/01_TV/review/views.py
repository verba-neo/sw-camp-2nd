# review/views.py
from django.shortcuts import render


def home(request):
    
    return render(request, 'review/home.html')


def about(request):
    
    return render(request, 'review/about.html')
