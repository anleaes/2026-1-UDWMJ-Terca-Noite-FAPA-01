from rest_framework import serializers
from .models import Prescription

class PrescriptionSerializer(serializers.ModelSerializer):
    patient_name = serializers.StringRelatedField(source='patient', read_only=True)
    doctor_name  = serializers.StringRelatedField(source='doctor',  read_only=True)

    class Meta:
        model  = Prescription
        fields = '__all__'
