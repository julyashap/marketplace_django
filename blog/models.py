from django.db import models

NULLABLE = {'null': True, 'blank': True}


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
