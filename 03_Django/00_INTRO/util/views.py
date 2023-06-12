from django.shortcuts import render


def lotto(request):
    
    return render(request, 'lotto.html')


def kospi(request):
    
    return render(request, 'kospi.html')