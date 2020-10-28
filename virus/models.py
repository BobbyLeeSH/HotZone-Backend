from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Virus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    common_name = models.CharField(max_length=30)
    max_infection_period = models.IntegerField()

    def __str__(self):
        return self.namec

    class Meta:
        ordering = ['id']
