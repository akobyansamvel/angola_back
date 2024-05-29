# hospital/models.py
from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    registry_number = models.CharField(max_length=50)
    doctors = models.ManyToManyField('doctor.Doctor', related_name='hospitals')

    def __str__(self):
        return self.name
