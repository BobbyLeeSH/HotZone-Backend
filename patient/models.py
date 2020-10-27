from django.db import models


# Create your models here.

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    national_id = models.CharField(max_length=20)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
