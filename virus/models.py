from django.db import models

# Create your models here.
from django.db import models


# Create your models here.

class Virus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    common_name = models.CharField(max_length=30)
    maximum_period_of_infection = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
