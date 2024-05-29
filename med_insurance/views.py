# med_insurance/views.py

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import MedInsurance
from .serializers import MedInsuranceSerializer

@login_required
def med_insurance_detail(request):
    med_insurance = get_object_or_404(MedInsurance, user=request.user)
    return render(request, 'med_insurance/med_insurance_detail.html', {'med_insurance': med_insurance})

@login_required
def med_insurance_update(request):
    med_insurance = get_object_or_404(MedInsurance, user=request.user)
    if request.method == 'POST':
        form = MedInsuranceForm(request.POST, instance=med_insurance)
        if form.is_valid():
            form.save()
            return redirect('med_insurance_detail')
    else:
        form = MedInsuranceForm(instance=med_insurance)
    return render(request, 'med_insurance/med_insurance_form.html', {'form': form})

class MedInsuranceViewSet(viewsets.ModelViewSet):
    queryset = MedInsurance.objects.all()
    serializer_class = MedInsuranceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MedInsurance.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
