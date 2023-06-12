from django.shortcuts import render

import random
import requests
from bs4 import BeautifulSoup

def lotto(request):
    # 로또 번호 6개 뽑기
    lucky_numbers = random.sample(range(1, 46), 6)

    return render(request, 'lotto.html', {
        'lucky_numbers': lucky_numbers,
    })


def kospi(request):
    URL = 'https://finance.naver.com/sise'
    res = requests.get(URL)
    html = BeautifulSoup(res.text, 'html.parser')
    KOSPI = html.select_one('#KOSPI_now').text
    
    return render(request, 'kospi.html', {
        'KOSPI': KOSPI,
    })