# Generated by Django 3.1.3 on 2020-11-22 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='lenguage',
            new_name='language',
        ),
    ]
