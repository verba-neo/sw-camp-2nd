# input/views.py
from django.shortcuts import render


def home(request):
    return render(request, 'input/home.html')


# Variable Routing
def greeting(request, name):
    return render(request, 'input/greeting.html', {
        'name': name,
    })


def lotto(request, draw_no):
    # draw_no(회차) 정보로 원하는 데이터를 뽑아서
    # 사용자에게 lotto.html 에 보여주기

    return render(request, 'input/lotto.html', {
    })


# <form> & <input>
def ping(request):
    # 사용자에게 데이터 입력용 <form> 제공
    return render(request, 'input/ping.html')


def pong(request):
    # 사용자가 제출(submit)한 데이터를 받음
    username = request.POST['username']
    password = request.POST['password']

    return render(request, 'input/pong.html', {
        'username': username,
        'password': password[:2] + '****',
    })
