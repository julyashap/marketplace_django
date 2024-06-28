# Generated by Django 5.0.6 on 2024-06-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='client',
        ),
        migrations.AddField(
            model_name='newsletter',
            name='clients',
            field=models.ManyToManyField(to='mailing.client', verbose_name='клиенты'),
        ),
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(verbose_name='тело сообщения'),
        ),
    ]
