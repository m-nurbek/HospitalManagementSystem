# Generated by Django 3.0.5 on 2022-11-04 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='category',
            field=models.CharField(choices=[('Highest', 'Highest'), ('First', 'First'), ('Second', 'Second')], default='Highest', max_length=9),
        ),
        migrations.AddField(
            model_name='doctor',
            name='degree_ed',
            field=models.CharField(choices=[('Doctor of Medicine', 'Doctor of Medicine'), ('Ph.D. in Medicine', 'Ph.D. in Medicine'), ('MD in Medicine', 'MD in Medicine')], default='MD in Medicine', max_length=25),
        ),
        migrations.AddField(
            model_name='doctor',
            name='experience',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='id_number',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='national_id',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='price',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='rating',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='specialization_id',
            field=models.CharField(max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(null=True)),
                ('national_id', models.CharField(max_length=12, null=True)),
                ('id_number', models.CharField(max_length=9, null=True)),
                ('blood_group', models.CharField(choices=[('A RhD positive (A+)', 'A RhD positive (A+)'), ('A RhD negative (A-)', 'A RhD negative (A-)'), ('B RhD positive (B+)', 'B RhD positive (B+)'), ('B RhD negative (B-)', 'B RhD negative (B-)'), ('O RhD positive (O+)', 'O RhD positive (O+)'), ('O RhD negative (O-)', 'O RhD negative (O-)'), ('AB RhD positive (AB+)', 'AB RhD positive (AB+)'), ('AB RhD negative (AB-)', 'AB RhD negative (AB-)')], default='Single', max_length=50)),
                ('mobile_emergency', models.CharField(max_length=20, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('email_address', models.EmailField(max_length=150)),
                ('address', models.CharField(max_length=40)),
                ('marital_status', models.CharField(choices=[('single', 'single'), ('married', 'married'), ('divorced', 'divorced')], default='Cardiologist', max_length=50)),
                ('registration_date', models.DateField(null=True)),
                ('symptoms', models.CharField(max_length=100)),
                ('assignedDoctorId', models.PositiveIntegerField(null=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]