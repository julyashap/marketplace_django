# Generated by Django 5.0.6 on 2024-06-10 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='цена'),
        ),
    ]