# Master urls.py
from django.contrib import admin
from django.urls import path, include


def home(request):
    from django.shortcuts import redirect
    # 홈 화면 변경시 redirect 대상만 변경
    return redirect('board:article_index')  


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')),
    path('accounts/', include('accounts.urls')),
]
