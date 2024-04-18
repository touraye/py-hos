from django.db import models

# Doctor table
class Doctor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    supervisor = models.CharField(max_length=100)
    specialty = models.CharField(max_length=200) ## Doctors will have their unique specification, this be checked when fixing an appointing for a Patient. A Patient with a teeth issue will have an appointment with a Doctor with a specification of dentist: [some constraints]
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
    
    def __str__(self):
        return self.name
    

# Appointment table - bridge table
class Appointment(models.Model):
    appointed_id = models.CharField(max_length=10, unique=True) # unique
    blood_pressure = models.IntegerField(default=0)
    notes = models.CharField(max_length=250, blank=True)
    medicine = models.CharField(max_length=100)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE) 
