# med_insurance/admin.py
from django.contrib import admin
from .models import MedInsurance

class MedInsuranceAdmin(admin.ModelAdmin):
    list_display = ('policy_number', 'expiry_date', 'insurer_id', 'insurer_name', 'issued_by')
    search_fields = ('policy_number', 'insurer_name')

admin.site.register(MedInsurance, MedInsuranceAdmin)
