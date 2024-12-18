# Generated by Django 3.2.16 on 2024-12-16 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20241215_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='music',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение'),
        ),
        migrations.AddField(
            model_name='performer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]
