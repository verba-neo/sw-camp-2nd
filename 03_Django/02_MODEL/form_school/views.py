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
        # 새로운 빈 form
        form = StudentForm()

    elif request.method == 'POST':
        # 사용자 입력데이터를 담은 form
        form = StudentForm(request.POST)
        # 검증
        if form.is_valid():
            # 성공 => 저장
            student = form.save()
            return redirect('school:detail', student.pk)
            # 실패 => 아래 코드 실행
    return render(request, 'school/form.html', {
        'form': form,
    })


def index(request):
    # 단순 전부 => id 오름차순
    # students = Student.objects.all()
    # 나이 오름차순
    # students = Student.objects.order_by('age')
    # id(pk) 내림차순
    students = Student.objects.order_by('-pk')
    return render(request, 'school/index.html', {
        'students': students,
    })


def detail(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    return render(request, 'school/detail.html', {
        'student': student,
    })


"""
def update(request, student_pk):
    student = Student.objects.get(pk=student_pk)

    if request.method == 'GET':
        # 기존 레코드의 내용을 담은 form
        form = StudentForm(instance=student)
        # 사용자에게 렌더
        return render(request, 'school/edit.html', {
            'form': form,
        })

    elif request.method == 'POST':
        # 기존 레코드와 사용자가 넘긴 정보를 함께 담은 form
        form = StudentForm(request.POST, instance=student)
        # form 이(사용자 입력 데이터가) 유효하다면,
        if form.is_valid():
            # 레코드 갱신 저장
            student = form.save()
            return redirect('school:detail', student.pk)
        # 사용자 입력 데이터가 유효하지 않다면,
        else:
            return render(request, 'school/edit.html', {
                'form': form,
            })
"""
def update(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    if request.method == 'GET':
        form = StudentForm(instance=student)
        
    elif request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('school:detail', student.pk)
        
    return render(request, 'school/form.html', {
        'form': form,
    })


def delete(request, student_pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=student_pk)
        student.delete()
    return redirect('school:index')