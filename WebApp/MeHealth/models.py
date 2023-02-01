from django.db import models

# Create your models here.
class Doctors(models.Model):
    name = models.CharField(max_length=300)
    specialty = models.CharField(max_length=100)
    about = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to="doctor_profile/", null=False)
    
    def __str__(self):
        return self.name