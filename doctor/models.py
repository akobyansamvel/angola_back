# doctor/models.py
from django.db import models

class Doctor(models.Model):
    full_name = models.CharField(max_length=100, null=True, blank=True)  # Allowing null and blank values
    profession = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.full_name if self.full_name else 'Unnamed Doctor'
