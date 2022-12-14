
from django.shortcuts import render,redirect,reverse
from . import models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings
from django.db.models import Q

from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

from . import forms,models


from django.core.paginator import Paginator #import Paginator

# load pages:
def cardiology(request):
    doctors=models.Doctor.objects.all()
    return render(request=request, template_name="theapp/cardiology.html", context = {'doctors':doctors})

def children(request):
    doctors=models.Doctor.objects.all()
    return render(request=request, template_name="theapp/children.html", context = {'doctors':doctors})

def dentistry(request):
    doctors=models.Doctor.objects.all()
    return render(request=request, template_name="theapp/dentistry.html", context = {'doctors':doctors})

def mri(request):
    doctors=models.Doctor.objects.all()
    return render(request=request, template_name="theapp/mri.html", context = {'doctors':doctors})

def neurology(request):
    doctors=models.Doctor.objects.all()
    return render(request=request, template_name="theapp/neurology.html", context = {'doctors':doctors})

def pulmonology(request):
    doctors=models.Doctor.objects.all()
    return render(request=request, template_name="theapp/pulmonology.html", context = {'doctors':doctors})

def surgery(request):
    doctors=models.Doctor.objects.all()
    return render(request=request, template_name="theapp/surgery.html", context = {'doctors':doctors})

def lab(request):
    doctors=models.Doctor.objects.all()
    return render(request=request, template_name="theapp/lab.html", context = {'doctors':doctors})







# Create your views here:

def homepage(request):
    # form = AuthenticationForm(request, data=request.POST)
    context = {}
    doctors = models.Doctor.objects.all()
    context['doctors'] = doctors
    print(f"AHSADJLASDJSAD {doctors}")

    return render(request=request, template_name="theapp/index.html", context=context)


def home_back(request):
    return homepage(request)




def register(request):
    #form = AuthenticationForm(request, data=request.POST)

    return render(request=request, template_name="theapp/register.html")




# Create your models here.
def register_admin(request):
    if request.method=='POST':
        form=forms.AdminRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()

            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
            login(request, user)

            messages.success(request, "Registration successful." )
            return HttpResponseRedirect('home_back')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form=forms.AdminRegisterForm()
    return render(request=request,template_name = 'theapp/register_admin.html',context = {'form':form})

def register_doctor(request):
    userForm=forms.DoctorForm()
    doctorForm=forms.DoctorDetailForm()
    form={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorForm(request.POST)
        doctorForm=forms.DoctorDetailForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor.status = False
            doctor=doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)

            return HttpResponseRedirect('login')
    return render(request=request,template_name='theapp/register_doctor.html',context=form)


def register_patient(request):
    userForm=forms.PatientForm()
    patientForm=forms.PatientDetailForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientForm(request.POST)
        patientForm=forms.PatientDetailForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.user=user
            patient.status = False
            patient=patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
            login(request, user)
        return HttpResponseRedirect("login")
    return render(request,'theapp/register_patient.html',context=mydict)



def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("theapp:afterlogin")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="theapp/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("theapp:home_back")







def afterlogin(request):
    if admin_verify(request.user):
        return redirect('theapp:admin_page')
    elif doctor_verify(request.user):
        accountapproval=models.Doctor.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('theapp:doctor_page')
        else:
            return render(request,'theapp/doctor_no_approval.html')
    elif patient_verify(request.user):
        accountapproval=models.Patient.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('theapp:patient_page')
        else:
            return render(request,'theapp/patient_no_approval.html')


















# ADMIN STAFF:

def admin_verify(user):
    if user.groups.filter(name='ADMIN').exists() or user.is_superuser:
        return True
    else:
        return False
def doctor_verify(user):
    return user.groups.filter(name='DOCTOR').exists()
def patient_verify(user):
    return user.groups.filter(name='PATIENT').exists()



@login_required(login_url='login')
@user_passes_test(admin_verify)
def admin_page(request):
    return render(request,'theapp/admin_page.html')

@login_required(login_url='login')
@user_passes_test(doctor_verify)
def doctor_page(request):
    appointments=models.Appointment.objects.filter(doctor_id = request.user.doctor.id, status = True)
    return render(request,'theapp/doctor_page.html', context = {'appointments':appointments})







@login_required(login_url='login')
@user_passes_test(patient_verify)
def patient_page(request):
    appointments=models.Appointment.objects.filter(patient_id = request.user.patient.id)
    return render(request,'theapp/patient_page.html', context = {'appointments':appointments})






### ADMIN AND DOCTOR:

@login_required(login_url='login')
@user_passes_test(admin_verify)
def admin_doctor(request):
    doctors=models.Doctor.objects.all().filter(status=True)
    return render(request,'theapp/admin_doctor.html',{'doctors':doctors})


@login_required(login_url='login')
@user_passes_test(admin_verify)
def add_doctor(request):
    userForm=forms.DoctorForm()
    doctorForm=forms.DoctorDetailForm()
    form={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorForm(request.POST)
        doctorForm=forms.DoctorDetailForm(request.POST,request.FILES)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            doctor=doctorForm.save(commit=False)
            doctor.user=user
            doctor.status = True
            doctor=doctor.save()
            my_doctor_group = Group.objects.get_or_create(name='DOCTOR')
            my_doctor_group[0].user_set.add(user)

            return HttpResponseRedirect('admin_doctor')
    return render(request=request,template_name='theapp/add_doctor.html',context=form)







@login_required(login_url='login')
@user_passes_test(admin_verify)
def approve_doctor(request):
    doctors=models.Doctor.objects.all().filter(status=False)
    return render(request,'theapp/approve_doctor.html',{'doctors':doctors})

@login_required(login_url='login')
@user_passes_test(admin_verify)
def accept_doctor(request,doctor_id):
    doctor=models.Doctor.objects.get(id=doctor_id)
    doctor.status=True
    doctor.save()
    return redirect(reverse('theapp:approve_doctor'))


@login_required(login_url='login')
@user_passes_test(admin_verify)
def delete_doctor(request,doctor_id):
    doctor=models.Doctor.objects.get(id=doctor_id)
    user=models.User.objects.get(id=doctor.user_id)
    user.delete()
    doctor.delete()

    return redirect('theapp:admin_doctor')



@login_required(login_url='login')
@user_passes_test(admin_verify)
def update_doctor(request,doctor_id):
    doctor=models.Doctor.objects.get(id=doctor_id)
    user=models.User.objects.get(id=doctor.user_id)

    userForm=forms.DoctorForm(instance=user)
    doctorForm=forms.DoctorDetailForm(request.FILES,instance=doctor)
    form={'userForm':userForm,'doctorForm':doctorForm}
    if request.method=='POST':
        userForm=forms.DoctorForm(request.POST,instance=user)
        doctorForm=forms.DoctorDetailForm(request.POST,request.FILES,instance=doctor)
        if userForm.is_valid() and doctorForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            doctor=doctorForm.save(commit=False)

            doctor.save()
            return redirect('theapp:admin_doctor')
    return render(request,'theapp/update_doctor.html',context=form)

















### ADMIN AND PATIENT:

@login_required(login_url='login')
@user_passes_test(admin_verify)
def approve_patient(request):
    patients=models.Patient.objects.all().filter(status=False)
    return render(request,'theapp/approve_patient.html',{'patients':patients})

@login_required(login_url='login')
@user_passes_test(admin_verify)
def accept_patient(request,patient_id):
    patient=models.Patient.objects.get(id=patient_id)
    patient.status=True
    patient.save()
    return redirect(reverse('theapp:approve_patient'))







@login_required(login_url='login')
@user_passes_test(admin_verify)
def admin_patient(request):
    patients=models.Patient.objects.all().all().filter(status=True)
    return render(request,'theapp/admin_patient.html',{'patients':patients})



@login_required(login_url='login')
@user_passes_test(admin_verify)
def add_patient(request):
    userForm=forms.PatientForm()
    patientForm=forms.PatientDetailForm()
    form={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientForm(request.POST)
        patientForm=forms.PatientDetailForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()

            patient=patientForm.save(commit=False)
            patient.user=user
            patient.status = True
            patient=patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)

            return HttpResponseRedirect('admin_patient')
    return render(request=request,template_name='theapp/add_patient.html',context=form)




@login_required(login_url='login')
@user_passes_test(admin_verify)
def update_patient(request,patient_id):
    patient=models.Patient.objects.get(id=patient_id)
    user=models.User.objects.get(id=patient.user_id)

    userForm=forms.PatientForm(instance=user)
    patientForm=forms.PatientDetailForm(request.FILES,instance=patient)
    form={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientForm(request.POST,instance=user)
        patientForm=forms.PatientDetailForm(request.POST,request.FILES,instance=patient)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.status=True
            patient.save()
            return redirect('theapp:admin_patient')
    return render(request,'theapp/update_patient.html',context=form)



@user_passes_test(admin_verify)
def delete_patient(request,patient_id):
    patient=models.Patient.objects.get(pk=patient_id)
    user=models.User.objects.get(pk=patient.user_id)
    user.delete()
    patient.delete()

    return redirect('theapp:admin_patient')















# PATIENT AND APPOINTMENTS
@login_required(login_url='login')
@user_passes_test(patient_verify)
def patient_request_appointment(request):

    appointmentForm=forms.AppointmentForm(request.POST)
    form={'appointmentForm':appointmentForm}
    if request.method=='POST':
        appointmentForm=forms.AppointmentForm(request.POST)
        if appointmentForm.is_valid():

            appointment=appointmentForm.save(commit=False)
            appointment.patient = request.user.patient

            appointment.status=False
            appointment.save()
            return redirect('theapp:patient_page')
    return render(request,'theapp/patient_request_appointment.html',context=form)
















#  DOCTOR AND APPOINTMENTS
@login_required(login_url='login')
@user_passes_test(doctor_verify)
def doctor_add_appointment(request):

    appointmentForm=forms.AppointmentForm(request.POST)
    form={'appointmentForm':appointmentForm}
    if request.method=='POST':
        appointmentForm=forms.AppointmentForm(request.POST)
        if appointmentForm.is_valid():

            appointment=appointmentForm.save(commit=False)
            appointment.doctor = request.user.doctor

            appointment.status=True
            appointment.save()
            return redirect('theapp:doctor_page')
    return render(request,'theapp/doctor_add_appointment.html',context=form)






@user_passes_test(doctor_verify)
def doctor_delete_appointment(request,appointment_id):
    appointment=models.Appointment.objects.get(pk=appointment_id)


    appointment.delete()

    return redirect('theapp:doctor_page')




@login_required(login_url='login')
@user_passes_test(doctor_verify)
def doctor_unapproved_appointments(request):
    appointments=models.Appointment.objects.filter(doctor_id = request.user.doctor.id, status = False)
    return render(request,'theapp/doctor_unapproved_appointments.html', context = {'appointments':appointments})

@login_required(login_url='login')
@user_passes_test(doctor_verify)
def doctor_approve_appointment(request,appointment_id):
    appointment=models.Appointment.objects.get(pk=appointment_id)
    appointment.status=True
    appointment.save()
    return redirect(reverse('theapp:doctor_page'))








@login_required(login_url='login')
@user_passes_test(doctor_verify)
def doctor_update_appointment(request,appointment_id):
    appointment=models.Appointment.objects.get(id=appointment_id)
    appointmentForm = forms.AppointmentForm(instance = appointment)

    form={'appointmentForm':appointmentForm}


    if request.method=='POST':
        appointmentForm = forms.AppointmentForm(request.POST, instance = appointment)
        if appointmentForm.is_valid():

            appointment=appointmentForm.save(commit=False)
            appointment.status=True
            appointment.save()
            return redirect('theapp:doctor_page')
    return render(request,'theapp/doctor_update_appointment.html',context=form)




def update_patient(request,patient_id):
    patient=models.Patient.objects.get(id=patient_id)
    user=models.User.objects.get(id=patient.user_id)

    userForm=forms.PatientForm(instance=user)
    patientForm=forms.PatientDetailForm(request.FILES,instance=patient)
    form={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientForm(request.POST,instance=user)
        patientForm=forms.PatientDetailForm(request.POST,request.FILES,instance=patient)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.status=True
            patient.save()
            return redirect('theapp:admin_patient')
    return render(request,'theapp/update_patient.html',context=form)






# SEARCH FUNCTIONALITY
def doctor_info(request, oid):
    doctor = models.Doctor.objects.get(id=oid)
    context = {"doctor_name": doctor.get_name,
               "doctor_department": doctor.department,
               "doctor_rating": doctor.rating,
               "doctor_phone": doctor.mobile,
               "doctor_img": doctor.profile_pic,
               }

    return render(request, 'theapp/doctor_info.html', context=context)
