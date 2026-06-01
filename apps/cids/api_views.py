from rest_framework import viewsets
from .models import Cid
from .serializers import CidSerializer

class CidViewSet(viewsets.ModelViewSet):
    queryset = Cid.objects.all()
    serializer_class = CidSerializer
