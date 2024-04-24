from django.contrib import admin

from .models import Doctor, Patient, Appointment

# Register Doctor model
class DoctorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name"]}), 
        ("Phone", {"fields": ["phone"]}),
        ("Email", {"fields": ["email"]}),
        ("Supervisor", {"fields": ["supervisor"]}), 
        ("Specialty", {"fields": ["specialty"]}),
        ("Created Date", {"fields": ["created_at"]}),
        ] 
    
    list_display = ["name", "phone", "email", "supervisor", "specialty", "created_at"]    
    list_filter = ["created_at", "specialty"]
    search_fields = ["name"]
    

class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["id"]}),
        ("Patient Name", {"fields": ["name"]}),
        ("Patient Email", {"fields": ["email"]}),
        ("Allergies", {"fields": ["allergies"]}),
        ("Admitted Date", {"fields": ["admitted_date"]}),
    ]
    
    list_display = ["id", "name", "email", "address", "admitted_date", "allergies"]   
    list_filter = ["admitted_date", "address"]
    search_fields = ["name"]
    
    
class AppointmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["id"]}),
        ("Appointed ID", {"fields": ["appointed_id"]}),
        ("Blood Pressure", {"fields": ["blood_pressure"]}),
        ("Appointment Note", {"fields": ["notes"]}),
        ("Medicines", {"fields": ["medicine"]}),
        ("Doctor", {"fields": ["doctor_id"]}),        
        ("Patient", {"fields": ["patient_id"]}),
        
    ]
    list_display = ["id", "appointed_id", "blood_pressure", "notes", "medicine", "doctor_id", "patient_id"]
    list_filter = ["doctor_id", "medicine"]
    search_fields = ["patient_id"]
    
    
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Appointment, AppointmentAdmin)
