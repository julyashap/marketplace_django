from django.db import models


class Product(models.Model):
    """Модель для данных о продаваемых продуктах"""

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    """Модель для данных о представленных категориях"""

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
