# hospital/admin.py
from django.contrib import admin
from .models import Hospital
from doctor.models import Doctor

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number', 'registry_number')
    filter_horizontal = ('doctors',)  # Используем виджет с чекбоксами

admin.site.register(Hospital, HospitalAdmin)
