from rest_framework import routers
from .api import DoctorViewSet, PatientViewSet, AppointmentViewSet

router = routers.DefaultRouter()
router.register('api/doctors', DoctorViewSet, 'doctors')
router.register('api/patients', PatientViewSet, 'patients')
router.register('api/appointments', AppointmentViewSet, 'appointments')

urlpatterns = router.urls