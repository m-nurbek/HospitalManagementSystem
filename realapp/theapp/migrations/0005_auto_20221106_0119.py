# Generated by Django 3.0.5 on 2022-11-05 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0004_doctor_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='category',
            field=models.CharField(choices=[('Highest', 'Highest'), ('First', 'First'), ('Second', 'Second')], default='Highest', max_length=9),
        ),
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.CharField(default='00', max_length=2),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialization_id',
            field=models.CharField(default='000000000', max_length=9),
        ),
    ]
