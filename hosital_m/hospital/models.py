from django.db import models
from django.contrib.auth.models import User
from .utils import SpecialtyTypes

# Doctor table
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    supervisor = models.CharField(max_length=100)   
    specialty = models.IntegerField(choices=SpecialtyTypes.specialties(), default=SpecialtyTypes.DENTIST)
    created_by = models.ForeignKey(User, related_name='doctor_user', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
# Patient table    
class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    address = models.CharField(max_length=250)
    admitted_date = models.DateTimeField(auto_now_add=True)
    allergies = models.CharField(max_length=500)
    created_by = models.ForeignKey(User, related_name='patient_user', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

# Appointment table - bridge table
class Appointment(models.Model):
    appointed_id = models.CharField(max_length=10, unique=True) # unique
    blood_pressure = models.IntegerField(default=0)
    notes = models.CharField(max_length=250, blank=True)
    medicine = models.CharField(max_length=100, blank=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE) 
    created_by = models.ForeignKey(User, related_name='appointment_user', on_delete=models.CASCADE, null=True)
    
    