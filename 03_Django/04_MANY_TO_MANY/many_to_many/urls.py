# Master URL
from django.contrib import admin
from django.urls import path, include


def home(request):
    from django.shortcuts import redirect
    return redirect('board:feed_index')


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('board/', include('board.urls')),
]
