# med_insurance/models.py
from django.db import models
from django.conf import settings

class MedInsurance(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='med_insurance', default=1)  # Temporary default value
    policy_number = models.CharField("Номер полиса", max_length=50)
    expiry_date = models.DateField("Срок действия")
    insurer_id = models.CharField("Идентификатор страховой", max_length=50)
    insurer_name = models.CharField("Название страховой", max_length=100)
    issued_by = models.CharField("Где выдан", max_length=200)

    def __str__(self):
        return f'{self.policy_number} - {self.insurer_name}'
