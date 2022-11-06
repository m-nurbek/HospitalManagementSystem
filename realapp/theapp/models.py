from django.db import models
from django.contrib.auth.models import User
from django import forms
import datetime
from django.core import validators

departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

categories = [('Highest','Highest'), ('First','First'), ('Second','Second')]

degrees = [('Doctor of Medicine', 'Doctor of Medicine'), ('Ph.D. in Medicine', 'Ph.D. in Medicine'),
            ('MD in Medicine', 'MD in Medicine')]


class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    birthday = models.DateTimeField(default=datetime.date.today, blank=True)
    mobile = models.CharField(max_length=20)
    national_id = models.CharField(max_length = 12)
    id_number = models.CharField(max_length = 9)

    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')

    #department_id = model.CharField(maxlength = 9)
    specialization_id = models.CharField(max_length = 9, default='000000000')
    experience = models.CharField(max_length = 2, default='00')
    profile_pic= models.ImageField(upload_to='images/doctor_pics',null=True,blank=True)
    category = models.CharField(max_length=9, choices=categories, default='Highest')

    price = models.CharField(max_length = 4, default='0000')


    degree_ed = models.CharField(max_length=25, choices=degrees, default='MD in Medicine')

    rating = models.CharField(max_length = 2, default = '00')

    address = models.CharField(max_length=40, default = 'Your current address')


    status=models.BooleanField(default=False)



    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)






blood_groups = [('A RhD positive (A+)','A RhD positive (A+)'),('A RhD negative (A-)','A RhD negative (A-)'),
                ('B RhD positive (B+)','B RhD positive (B+)'),('B RhD negative (B-)','B RhD negative (B-)'),
                ('O RhD positive (O+)', 'O RhD positive (O+)'),('O RhD negative (O-)', 'O RhD negative (O-)'),
                ('AB RhD positive (AB+)','AB RhD positive (AB+)'),('AB RhD negative (AB-)','AB RhD negative (AB-)')]

marital_statuses = [('single','single'),('married','married'),('divorced','divorced')]


class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    birthday = models.DateTimeField(default=datetime.date.today, blank=True)
    profile_pic= models.ImageField(upload_to='images/patient_pics',null=True,blank=True)
    national_id = models.CharField(max_length = 12, default = '000000000000')
    id_number = models.CharField(max_length = 9,default = '000000000')
    blood_group = models.CharField(max_length=50,choices=blood_groups,default='Single')
    mobile_emergency = models.CharField(max_length=20,default = '000')
    mobile = models.CharField(max_length=20,default = '000')
    email_address = models.EmailField(max_length = 254)
    address = models.CharField(max_length=40, default = 'Some address')
    marital_status= models.CharField(max_length=50,choices=marital_statuses,default='Single')
    registration_date = models.DateTimeField(default=datetime.date.today, blank=True)
    symptoms = models.CharField(max_length=100, default= 'Flu')
    status=models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"
