# Generated by Django 2.2.10 on 2020-04-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата добавления новости'),
        ),
    ]
