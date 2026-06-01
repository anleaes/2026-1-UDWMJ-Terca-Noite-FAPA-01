from rest_framework import serializers
from .models import Cid

class CidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cid
        fields = '__all__'
