# Generated by Django 3.0.5 on 2022-12-08 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0016_appointment_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='doctor',
            name='slots',
            field=models.ManyToManyField(through='theapp.Appointment', to='theapp.Patient'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointmentTime',
            field=models.CharField(choices=[('9.00', '9.00'), ('9.20', '9.20'), ('9.40', '9.40'), ('10.00', '10.00'), ('10.20', '10.20'), ('10.40', '10.40'), ('11.00', '11.00'), ('11.20', '11.20'), ('11.40', '11.40'), ('12.00', '12.00'), ('12.20', '12.20'), ('12.40', '12.40'), ('14.00', '14.00'), ('14.20', '14.20'), ('14.40', '14.40'), ('15.00', '15.00'), ('15.20', '15.20'), ('15.40', '15.40'), ('16.00', '16.00'), ('16.20', '16.20'), ('16.40', '16.40'), ('17.00', '17.00'), ('17.20', '17.20'), ('17.40', '17.40')], default='9.00', max_length=50),
        ),
    ]
