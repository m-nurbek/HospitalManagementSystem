# Generated by Django 3.0.5 on 2022-12-08 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0017_auto_20221208_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='slots',
        ),
    ]
