# Generated by Django 3.0.5 on 2022-11-05 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actor', '0003_auto_20221106_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50),
        ),
    ]