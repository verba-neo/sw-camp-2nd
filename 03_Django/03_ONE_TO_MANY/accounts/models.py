# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # MBTI_CHOICES = [
    #     # (db 저장할 값, 사용자에게 보여줄 text)
    #     ('estp', 'ESTP'),
    #     ('estj', 'ESTJ'),
    #     ('esfp', 'ESFP'),
    #     ('esfj', 'ESFJ'),
    # ]

    # mbti = models.CharField(max_length=4, choices=MBTI_CHOICES)

    def __str__(self):
        return f'#{self.pk}: {self.username}'