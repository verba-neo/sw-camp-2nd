from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'#{self.id}: {self.name}'
        

class Patient(models.Model):
    name = models.CharField(max_length=100)
    # Patient 객체 => doctors 로 접근
    doctors = models.ManyToManyField(
        Doctor,
        through='Reservation',
        through_fields=('patient', 'doctor'),
        # Doctor 객체 => 역참조 기본값 _set => 수정
        related_name = 'patients',
    )

    def __str__(self):
        return f'#{self.id}: {self.name}'
    

class Reservation(models.Model):
    #                          Doctor 입장에서 Reservation 역참조 => d.reservations.all()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='reservations')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reservations')
    date = models.DateField()


if __name__ == '__main__':
    d1 = Doctor.objects.create(name='김외과')
    d2 = Doctor.objects.create(name='이내과')
    d3 = Doctor.objects.create(name='박피부과')

    p1 = Patient.objects.create(name='최환자')
    p2 = Patient.objects.create(name='정환자')
    p3 = Patient.objects.create(name='강환자')
    p4 = Patient.objects.create(name='유환자')

    Reservation.objects.create(doctor=d1, patient=p1, date='2023-06-26')
    Reservation.objects.create(doctor=d1, patient=p2, date='2023-06-27')
    Reservation.objects.create(doctor=d1, patient=p3, date='2023-06-28')
    Reservation.objects.create(doctor=d1, patient=p4, date='2023-06-29')

    Reservation.objects.create(doctor=d2, patient=p1, date='2023-06-26')
    Reservation.objects.create(doctor=d3, patient=p1, date='2023-06-26')
    
    # 1번 환자의 모든 예약 의사
    p1.doctors.all() 
    # 1번 환자의 모든 예약
    p1.reservations.all()

    # 1번 의사의 모든 예약 환자
    d1.patients.all()
    # 1번 의사의 모든 예약
    d1.reservations.all()


    # related_name 옵션 사용하는 이유
    class User(models.Model):
        name = models.CharField(max_length=100)


    class Article(models.Model):
        title = models.CharField(max_length=100)
        content = models.TextField()

        # 작가
        author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='write_articles')
        # 편집자
        editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='edit_articles')
        # 번역가
        translator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='translate_articles')
        # 검수
        inspector = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inspect_articles')

    u = User.objects.first()
    
    # 작성한 글
    u.write_articles.all()
    # 편집한 글
    u.edit_articles.all()
    # 번역한 글
    u.translate_articles.all()
    # 검수한 글
    u.inspect_articles.all()
