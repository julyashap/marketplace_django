from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    """Модель для данных о представленных категориях"""

    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """Модель для данных о продаваемых продуктах"""

    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='картинка', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена', **NULLABLE)
    created_at = models.DateField(verbose_name='дата создания')
    updated_at = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contact(models.Model):
    """Модель для хранения контактных данных"""

    country = models.CharField(max_length=100, verbose_name='страна')
    tin = models.CharField(max_length=10, verbose_name='ИНН')
    address = models.CharField(max_length=100, verbose_name='адрес')

    def __str__(self):
        return f"{self.country} {self.tin}"

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'
