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


    path("admin_page", views.admin_page, name="admin_page"),


    path("add_doctor", views.add_doctor, name="add_doctor"),
    path("admin_doctor", views.admin_doctor, name="admin_doctor"),
    path('update_doctor/<doctor_id>', views.update_doctor,name='update_doctor'),
    path("delete_doctor/<doctor_id>", views.delete_doctor, name="delete_doctor"),


    path("add_patient", views.add_patient, name="add_patient"),
    path("admin_patient", views.admin_patient, name="admin_patient"),
    path('update_patient/<patient_id>', views.update_patient,name='update_patient'),
    path("delete_patient/<patient_id>", views.delete_patient, name="delete_patient"),













]
