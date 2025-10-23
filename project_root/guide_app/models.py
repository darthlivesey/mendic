from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class CustomUser(AbstractUser):
    """Кастомная модель пользователя с дополнительными полями"""
    
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(
        max_length=20, 
        blank=True, 
        null=True,
        verbose_name='Телефон'
    )
    
    birth_date = models.DateField(
        blank=True, 
        null=True,
        verbose_name='Дата рождения'
    )
    
    COUNTRY_CHOICES = [
        ('ru', 'Россия'),
        ('by', 'Беларусь'),
        ('kz', 'Казахстан'),
        ('ua', 'Украина'),
        ('other', 'Другая'),
    ]
    
    country = models.CharField(
        max_length=10,
        choices=COUNTRY_CHOICES,
        blank=True,
        null=True,
        verbose_name='Страна'
    )
    
    city = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Город'
    )
    
    # Согласия
    agreed_to_terms = models.BooleanField(
        default=False,
        verbose_name='Согласие с условиями'
    )
    
    newsletter_subscription = models.BooleanField(
        default=False,
        verbose_name='Подписка на рассылку'
    )
    
    # Даты
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.username

class RegistrationLog(models.Model):
    """Модель для логирования регистраций"""
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    ip_address = models.GenericIPAddressField(verbose_name='IP адрес')
    user_agent = models.TextField(verbose_name='User Agent')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    
    class Meta:
        verbose_name = 'Лог регистрации'
        verbose_name_plural = 'Логи регистраций'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Регистрация {self.user.username} - {self.created_at}"