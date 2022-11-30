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
        fields=['birthday','profile_pic','national_id','id_number','blood_group','mobile_emergency','mobile','email_address',
                'address','marital_status','registration_date','symptoms','status']










class AppointmentForm(forms.ModelForm):
    doctor_id=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    patient_id=forms.ModelChoiceField(queryset=models.Patient.objects.all().filter(status=True),empty_label="Patient Name and Symptoms", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']


class PatientAppointmentForm(forms.ModelForm):
    doctorId=forms.ModelChoiceField(queryset=models.Doctor.objects.all().filter(status=True),empty_label="Doctor Name and Department", to_field_name="user_id")
    class Meta:
        model=models.Appointment
        fields=['description','status']
