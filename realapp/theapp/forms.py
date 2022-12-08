from django import forms
from django.contrib.auth.models import User
from . import models





class AdminRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {'password': forms.PasswordInput()}



#for student related form
class DoctorForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class DoctorDetailForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['birthday','mobile','national_id','id_number','department','specialization_id','experience','profile_pic','category','price','degree_ed',
            'rating','address','status']






#for student related form
class PatientForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class PatientDetailForm(forms.ModelForm):
    class Meta:
        model=models.Patient
        fields=['birthday','national_id','id_number','blood_group','mobile_emergency','mobile','email_address',
                'address','marital_status','registration_date','symptoms','status']










class AppointmentForm(forms.ModelForm):
    class Meta:
        model=models.Appointment
        fields=['doctor','patient','appointmentTime','description','status']
