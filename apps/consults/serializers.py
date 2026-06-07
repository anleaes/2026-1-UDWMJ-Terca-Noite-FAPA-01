from rest_framework import serializers
from .models import Consult

class ConsultSerializer(serializers.ModelSerializer):
    patient_name = serializers.StringRelatedField(source='patient', read_only=True)
    doctor_name  = serializers.StringRelatedField(source='doctor',  read_only=True)

    class Meta:
        model  = Consult
        fields = '__all__'
