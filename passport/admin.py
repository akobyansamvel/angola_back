# passport/admin.py
from django.contrib import admin
from .models import Passport

class PassportAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'series_number', 'issued_by', 'issued_date', 'date_of_birth', 'citizenship', 'expiry_date')
    search_fields = ('last_name', 'first_name', 'series_number')

admin.site.register(Passport, PassportAdmin)
