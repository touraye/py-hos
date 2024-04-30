from hospital.models import Doctor, Patient, Appointment
from rest_framework import viewsets, permissions
from .serializers import DoctorSerializer, PatientSerializer, AppointmentSerializer

# Doctor Viewset
class DoctorViewSet(viewsets.ModelViewSet):
     # queryset = Doctor.objects.all()
    permission_classes = [
        permissions.IsAuthenticated # adding authentication
    ]
    
    serializer_class = DoctorSerializer
    
    def get_queryset(self):        
        return Doctor.objects.all()
    
    
# Patient Viewset
class PatientViewSet(viewsets.ModelViewSet):
    # queryset = Patient.objects.all()
    permission_classes = [
        permissions.IsAuthenticated # adding authentication
    ]
    
    serializer_class = PatientSerializer  
    
    def get_queryset(self):
        return self.Patient.objects.all()
    
    
# Appointment Viewset
class AppointmentViewSet(viewsets.ModelViewSet):
    # queryset = Appointment.objects.all()
    permission_classes = [
        permissions.IsAuthenticated # add authentication
    ]
    
    serializer_class = AppointmentSerializer   
    
    def get_queryset(self):
        return self.Appointment.objects.all()