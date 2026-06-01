from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('cids/', include('cids.urls', namespace='cids')),
    path('medications/', include('medications.urls', namespace='medications')),
    path('historicos/', include('medicalhistories.urls', namespace='medicalhistories')),
    path('pacientes/', include('patients.urls', namespace='patients')),
    path('medicos/', include('doctors.urls', namespace='doctors')),
    path('consultas/', include('consults.urls', namespace='consults')),
    path('exames/', include('exams.urls', namespace='exams')),
    path('receitas/', include('prescriptions.urls', namespace='prescriptions')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)