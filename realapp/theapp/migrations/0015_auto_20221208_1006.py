# Generated by Django 3.0.5 on 2022-12-08 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0014_auto_20221208_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointmentDate',
        ),
        migrations.AddField(
            model_name='appointment',
            name='appointmentTime',
            field=models.CharField(default='10.00', max_length=5),
        ),
    ]
