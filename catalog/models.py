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


class Blog(models.Model):
    """Модель для данных о записях блога"""

    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blogs/', verbose_name='картинка', **NULLABLE)
    created_at = models.DateField(verbose_name='дата создания')
    is_published = models.BooleanField(verbose_name='признак публикации')
    count_views = models.IntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'запись блога'
        verbose_name_plural = 'записи блога'
