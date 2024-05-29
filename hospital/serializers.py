# hospital/serializers.py
from rest_framework import serializers
from doctor.serializers import DoctorSerializer
from .models import Hospital

class HospitalSerializer(serializers.ModelSerializer):
    doctors = DoctorSerializer(many=True, read_only=True)

    class Meta:
        model = Hospital
        fields = ['id', 'name', 'address', 'phone_number', 'registry_number', 'doctors']
