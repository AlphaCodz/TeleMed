from django.urls import path, re_path
from .views import index
from . import views

urlpatterns = [
    re_path("index", views.index, name="index"),
    re_path("doctors",views.doctors, name="doctors"),
    re_path("data", views.data, name="medical_data")
     
]
