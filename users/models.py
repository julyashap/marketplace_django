from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(verbose_name='аватар')
    phone = models.CharField(max_length=50, verbose_name='номер')
    country = models.CharField(max_length=100, verbose_name='страна')

    code = models.CharField(max_length=4, verbose_name='email-код', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
