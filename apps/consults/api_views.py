from rest_framework import viewsets
from .models import Consult
from .serializers import ConsultSerializer

class ConsultViewSet(viewsets.ModelViewSet):
    queryset = Consult.objects.all()
    serializer_class = ConsultSerializer
