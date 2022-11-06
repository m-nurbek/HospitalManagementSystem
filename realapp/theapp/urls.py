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


    path("admin_page", views.admin_page, name="admin_page"),
    path("add_doctor", views.add_doctor, name="add_doctor"),
    path("admin_doctor_choices", views.admin_doctor_choices, name="admin_doctor_choices"),
    path("delete_doctor_view", views.delete_doctor_view, name="delete_doctor_view"),


    path("add_patient", views.add_patient, name="add_patient"),
    path("admin_patient_choices", views.admin_patient_choices, name="admin_patient_choices"),
    path("delete_patient_view", views.delete_patient_view, name="delete_patient_view"),









    path("login", views.login_request, name="login"),



]
