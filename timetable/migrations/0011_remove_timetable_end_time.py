# Generated by Django 4.1.5 on 2023-01-31 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0010_alter_timetable_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timetable',
            name='end_time',
        ),
    ]
