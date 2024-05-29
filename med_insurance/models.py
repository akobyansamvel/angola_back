# med_insurance/models.py
from django.db import models

class MedInsurance(models.Model):
    policy_number = models.CharField("Номер полиса", max_length=50)
    expiry_date = models.DateField("Срок действия")
    insurer_id = models.CharField("Идентификатор страховой", max_length=50)
    insurer_name = models.CharField("Название страховой", max_length=100)
    issued_by = models.CharField("Где выдан", max_length=200)

    def __str__(self):
        return f'{self.policy_number} - {self.insurer_name}'
