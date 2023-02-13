from django.urls import path, re_path
from .views import index, GetDoctors, Consult, VideoCall
from . import views

app_name = "med"

urlpatterns = [
    path("home/", views.index, name="index"),
    # re_path(r"^doctors/$",views.doctors, name="doctors"),
    re_path(r"^data/$", views.data, name="medical_data"),
    re_path(r'^doctors/$', GetDoctors.as_view(), name="get_doctors"),
    re_path(r'^consult/$', Consult.as_view(), name="consult"),
    re_path(r'meeting/$', views.VideoCall, name="video_call")
    
]
