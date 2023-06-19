from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def new(request):
    form = StudentForm()
    
    return render(request, 'school/new.html', {
        'form': form,
    })


def create(request):
    
    return redirect('school:new')