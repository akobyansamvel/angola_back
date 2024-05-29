# med_insurance/serializers.py

from rest_framework import serializers
from .models import MedInsurance

class MedInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedInsurance
        fields = '__all__'
