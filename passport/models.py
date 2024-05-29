# passport/models.py
from django.db import models
from django.conf import settings

class Passport(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='passport', default=1)  # Temporary default value
    last_name = models.CharField("Фамилия", max_length=100)
    first_name = models.CharField("Имя", max_length=100)
    middle_name = models.CharField("Отчество", max_length=100, null=True, blank=True)
    date_of_birth = models.DateField("Дата рождения")
    citizenship = models.CharField("Гражданство", max_length=100)
    series_number = models.CharField("Серия и номер", max_length=20)
    issued_by = models.CharField("Кем выдан", max_length=200)
    issued_date = models.DateField("Дата выдачи")
    expiry_date = models.DateField("Срок действия")

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.series_number}'
