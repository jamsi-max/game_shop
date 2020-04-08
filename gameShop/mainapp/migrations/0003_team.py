# Generated by Django 2.2.10 on 2020-04-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20200408_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='имя')),
                ('post', models.CharField(max_length=32, verbose_name='должность')),
                ('image', models.ImageField(upload_to='products_images')),
            ],
        ),
    ]
