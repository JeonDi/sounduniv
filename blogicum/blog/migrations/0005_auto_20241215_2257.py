# Generated by Django 3.2.16 on 2024-12-15 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_genre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='slug',
            new_name='slug_1',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='slug',
            new_name='slug_3',
        ),
        migrations.RenameField(
            model_name='performer',
            old_name='slug',
            new_name='slug_2',
        ),
    ]
