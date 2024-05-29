# med_insurance/views.py
from rest_framework import viewsets
from .models import MedInsurance
from .serializers import MedInsuranceSerializer

class MedInsuranceViewSet(viewsets.ModelViewSet):
    queryset = MedInsurance.objects.all()
    serializer_class = MedInsuranceSerializer
