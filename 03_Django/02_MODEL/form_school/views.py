from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
"""
# GET /school/new/
def new(request):
    # 새로운 HTML 생성용 빈 form
    form = StudentForm()
    return render(request, 'school/new.html', {
        'form': form,
    })


# POST /school/create/
def create(request):
    # 사용자 제출한 데이터 검증용 Form
    form = StudentForm(request.POST)

    # 사용자 제출 데이터가 유효하다면,
    if form.is_valid():
        # DB에 저장
        form.save()
        # redirect
        return redirect('school:new')
    # 데이터가 하나라도 유효하지 않다면,
    else:
        # 다시 입력 HTML 제공
        return render(request, 'school/new.html', {
            'form': form,
        })
    
"""
def create(request):
    if request.method == 'GET':
        form = StudentForm()

    elif request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('school:detail', student.pk)
    
    return render(request, 'school/new.html', {
        'form': form,
    })


def index(request):
    pass


def detail():
    pass


def delete():
    pass