from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from .models import Doctors

# Create your views here.
def index(request):
    return render(request,"index.html")

# def doctors(request):
#     return render(request,"doctors.html")

def data(request):
    return render(request, "data.html")

class GetDoctors(ListView):
    model = Doctors
    template_name = "doctors_detail.html"
    context_object_name = "doctors"
    
class Consult(ListView):
    model = Doctors
    template_name="departments.html"
    context_object_name = "consultants"