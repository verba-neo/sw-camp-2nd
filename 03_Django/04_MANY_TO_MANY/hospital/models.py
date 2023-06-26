from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'#{self.id}: {self.name}'
        

class Patient(models.Model):
    name = models.CharField(max_length=100)
    doctors = models.ManyToManyField(
        Doctor,
        through='Reservation',
        through_fields=('patient', 'doctor',)
    )

    def __str__(self):
        return f'#{self.id}: {self.name}'
    

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
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
    p1.reservation_set.all()

    # 1번 의사의 모든 예약 환자
    d1.patient_set.all()
    # 1번 의사의 모든 예약
    d1.reservation_set.all()
