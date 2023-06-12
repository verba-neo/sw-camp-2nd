from django.shortcuts import render


def hello(request):
    from django.http import HttpResponse
    return HttpResponse('Hello Django')


def home(request):
    return render(request, 'home.html')
    