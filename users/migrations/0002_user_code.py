# Generated by Django 4.2 on 2024-07-15 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='email-код'),
        ),
    ]
