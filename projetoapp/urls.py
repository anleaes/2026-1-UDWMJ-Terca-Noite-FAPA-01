from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

from cids.api_views import CidViewSet
from medications.api_views import MedicationViewSet
from medicalhistories.api_views import MedicalHistoryViewSet
from patients.api_views import PatientViewSet
from doctors.api_views import DoctorViewSet
from consults.api_views import ConsultViewSet
from exams.api_views import ExamViewSet
from prescriptions.api_views import PrescriptionViewSet
from prescriptionitems.api_views import PrescriptionItemViewSet

router = DefaultRouter()
router.register(r'cids', CidViewSet)
router.register(r'medications', MedicationViewSet)
router.register(r'medicalhistories', MedicalHistoryViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'consults', ConsultViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'prescriptionitems', PrescriptionItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('core.urls', namespace='core')),
    path('cids/', include('cids.urls', namespace='cids')),
    path('medications/', include('medications.urls', namespace='medications')),
    path('historicos/', include('medicalhistories.urls', namespace='medicalhistories')),
    path('pacientes/', include('patients.urls', namespace='patients')),
    path('medicos/', include('doctors.urls', namespace='doctors')),
    path('consultas/', include('consults.urls', namespace='consults')),
    path('exames/', include('exams.urls', namespace='exams')),
    path('receitas/', include('prescriptions.urls', namespace='prescriptions')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)