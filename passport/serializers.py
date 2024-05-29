# passport/serializers.py
from rest_framework import serializers
from .models import Passport

class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = ['id', 'last_name', 'first_name', 'middle_name', 'series_number', 'issued_by', 'issued_date', 'date_of_birth', 'citizenship', 'expiry_date']
