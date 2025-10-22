from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('guest', 'Гость'),
        ('user', 'Пользователь'),
        ('business', 'Владелец бизнеса'),
        ('moderator', 'Модератор'),
        ('admin', 'Администратор'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='guest')
    phone = models.CharField(max_length=20, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)

class Location(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()