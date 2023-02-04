from django.urls import path, re_path
from .views import index
from . import views

app_name = "med"

urlpatterns = [
    path("home/", views.index, name="index"),
    re_path(r"^doctors/$",views.doctors, name="doctors"),
    re_path("data", views.data, name="medical_data")
     
]
