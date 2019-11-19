from django.db import models


class Shipment(models.Model):
    tracking = models.CharField(max_length=20)
    date = models.DateField()
    origin = models.CharField(max_length=250)
    destination = models.CharField(max_length=250)
    statusCode = models.IntegerField()

    def __str__(self):
        return self.tracking
