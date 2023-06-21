from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .forms import CustomUserCreationForm


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'GET':
        form = CustomUserCreationForm()
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('board:article_index')
    
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


def login(request):
    pass


def logout(request):
    pass
