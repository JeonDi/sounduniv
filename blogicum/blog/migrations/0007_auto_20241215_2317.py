# Generated by Django 3.2.16 on 2024-12-15 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20241215_2307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='slug_1',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='genre',
            old_name='slug_3',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='performer',
            old_name='slug_2',
            new_name='slug',
        ),
    ]
