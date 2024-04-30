from rest_framework import serializers
from hospital.models import Doctor, Patient, Appointment
from django.contrib.auth.models import User


# create a user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'

# create a doctor serializer
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        
        
# create a patient serializer
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'        
        
        
# create a appointment serializer
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'        