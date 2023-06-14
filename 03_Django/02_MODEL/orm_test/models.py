from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    major = models.CharField(max_length=100)
    mbti = models.CharField(max_length=4)


"""
1. 스키마 구상 (DB 모델링)
2. models.py 에 Model class 작성
3. python manage.py makemigrations <app-name>
4. python manage.py migrate <app-name>
5. 테이블 생성 완료
"""

if __name__ == '__main__':
    # Create
    s = Student()
    s.name = '유태영'
    s.age = 40
    s.major = '컴공'
    s.mbti = 'ESTP'
    s.save()

    s = Student.objects.create(name='오창희', age=39, major='SW', mbti='ENTJ')

    # Read
    # 전체 조회
    students = Student.objects.all()
    # 단일 조회 (pk == id)
    student = Student.objects.get(pk=1)
    student.id, student.pk
    student.name
    student.age
    
    # Update
    student = Student.objects.get(pk=1)
    student.mbti = 'INFJ'
    student.age = 35
    student.save()

    # Delete
    student = Student.objects.get(pk=2)
    student.delete()
