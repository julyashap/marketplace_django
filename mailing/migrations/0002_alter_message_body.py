# Generated by Django 5.0.6 on 2024-06-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(verbose_name='тело сообщения'),
        ),
    ]
