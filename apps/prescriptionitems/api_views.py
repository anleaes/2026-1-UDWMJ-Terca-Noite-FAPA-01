from rest_framework import viewsets
from .models import PrescriptionItem
from .serializers import PrescriptionItemSerializer

class PrescriptionItemViewSet(viewsets.ModelViewSet):
    queryset = PrescriptionItem.objects.all()
    serializer_class = PrescriptionItemSerializer
