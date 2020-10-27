from django.db import models


# Create your models here.
from case.models import Case


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    x_coord = models.CharField(max_length=10)
    y_coord = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name) + ' / ' + str(self.address) + ' / ' + str(self.x_coord) + ' / ' + str(self.y_coord)

    class Meta:
        unique_together =(("x_coord", "y_coord"),)
        ordering = ['id']


class CaseLocation(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    category = models.CharField(max_length=10)

    def __str__(self):
        return str(self.case) + ' / ' + str(self.location) + ' / ' + str(self.category)

    class Meta:
        ordering = ['id']
