from hospital.models import Doctor, Patient, Appointment
from rest_framework import viewsets, permissions
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer

# Doctor Viewset
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DoctorSerializer
    
    
# Patient Viewset
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PatientSerializer  
    
    
# Appointment Viewset
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AppointmentSerializer      