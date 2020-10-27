from django.db import models


# Create your models here.
from patient.models import Patient
from virus.models import Virus


class Case(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    virus = models.ForeignKey(Virus, on_delete=models.CASCADE)
    confirmed_date = models.DateField()
    origin = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id) + ' / ' + str(self.patient) + ' / ' + str(self.virus)

    class Meta:
        ordering = ['id']
