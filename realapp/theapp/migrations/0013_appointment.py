# Generated by Django 3.0.5 on 2022-11-30 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0012_auto_20221130_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.PositiveIntegerField(null=True)),
                ('doctor_id', models.PositiveIntegerField(null=True)),
                ('patientName', models.CharField(max_length=40, null=True)),
                ('doctorName', models.CharField(max_length=40, null=True)),
                ('appointmentDate', models.DateField(auto_now=True)),
                ('description', models.TextField(max_length=500)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]