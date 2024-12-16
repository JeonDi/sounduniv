# Generated by Django 3.2.16 on 2024-12-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_performer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('performer', models.CharField(max_length=256, verbose_name='Исполнитель')),
                ('year', models.PositiveIntegerField(verbose_name='Год')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('slug', models.SlugField(unique=True, verbose_name='Идентификатор')),
            ],
            options={
                'verbose_name': 'альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
    ]