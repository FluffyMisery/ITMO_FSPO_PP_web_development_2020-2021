# Generated by Django 3.1.6 on 2021-03-09 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0002_auto_20210309_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carowner',
            name='date_of_birth',
        ),
    ]
