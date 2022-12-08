from django.urls import path
from . import views

app_name = "theapp"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("home_back",  views.home_back, name = "home_back"),
    path("register", views.register, name="register"),
    path("register_admin", views.register_admin, name="register_admin"),
    path("register_doctor", views.register_doctor, name="register_doctor"),
    path("register_patient", views.register_patient, name="register_patient"),



    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),

    path("afterlogin", views.afterlogin, name= "afterlogin"),
    path("admin_page", views.admin_page, name="admin_page"),
    path("admin_page", views.admin_page, name="admin_page"),




    path("doctor_page", views.doctor_page, name="doctor_page"),
    path("doctor_add_appointment", views.doctor_add_appointment, name="doctor_add_appointment"),
    path("doctor_delete_appointment/<appointment_id>", views.doctor_delete_appointment, name="doctor_delete_appointment"),
    path("doctor_update_appointment/<appointment_id>", views.doctor_update_appointment, name="doctor_update_appointment"),
    path("doctor_approve_appointment/<appointment_id>", views.doctor_approve_appointment, name="doctor_approve_appointment"),
    path("doctor_unapproved_appointments", views.doctor_unapproved_appointments, name="doctor_unapproved_appointments"),








    path("patient_page", views.patient_page, name="patient_page"),

    path("patient_request_appointment", views.patient_request_appointment, name="patient_request_appointment"),




    path("add_doctor", views.add_doctor, name="add_doctor"),
    path("admin_doctor", views.admin_doctor, name="admin_doctor"),
    path("approve_doctor", views.approve_doctor, name="approve_doctor"),
    path("accept_doctor/<doctor_id>", views.accept_doctor, name="accept_doctor"),
    path('update_doctor/<doctor_id>', views.update_doctor,name='update_doctor'),
    path("delete_doctor/<doctor_id>", views.delete_doctor, name="delete_doctor"),


    path("add_patient", views.add_patient, name="add_patient"),
    path("admin_patient", views.admin_patient, name="admin_patient"),
    path("approve_patient", views.approve_patient, name="approve_patient"),
    path("accept_patient/<patient_id>", views.accept_patient, name="accept_patient"),
    path('update_patient/<patient_id>', views.update_patient,name='update_patient'),
    path("delete_patient/<patient_id>", views.delete_patient, name="delete_patient"),


    path("doctor_info/<oid>", views.doctor_info, name="doctor_info"),


    #pages:
    path("cardiology", views.cardiology, name="cardiology"),
    path("children", views.children, name="children"),
    path("dentistry", views.dentistry, name="dentistry"),
    path("lab", views.lab, name="lab"),
    path("mri", views.mri, name="mri"),
    path("neurology", views.neurology, name="neurology"),
    path("pulmonology", views.pulmonology, name="pulmonology"),
    path("surgery", views.surgery, name="surgery"),















]
