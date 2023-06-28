# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    stars = models.ManyToManyField('self', symmetrical=False, related_name='fans')
    # followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
