# Generated by Django 3.0.5 on 2022-11-06 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0009_auto_20221106_0358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='assignedDoctorId',
        ),
    ]