from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    """Модель для данных о представленных категориях"""

    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f"{self.pk}. {self.name}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """Модель для данных о продаваемых продуктах"""

    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='products/', verbose_name='картинка', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    created_at = models.DateField(verbose_name='дата создания')
    updated_at = models.DateField(verbose_name='дата последнего изменения')
    manufactured_at = models.DateField(verbose_name='дата производства продукта')

    def __str__(self):
        return f"{self.pk}. {self.name}"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
