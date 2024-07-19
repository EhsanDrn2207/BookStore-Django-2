from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
