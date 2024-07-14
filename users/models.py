from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(verbose_name='аватар')
    phone = models.CharField(max_length=50, verbose_name='номер')
    country = models.CharField(max_length=100, verbose_name='страна')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
