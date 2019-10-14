from django.db import models
from datetime import datetime


class Customer(models.Model):
    name = models.CharField(max_length=51)
    phone = models.CharField(max_length=16)
    created_at = models.DateTimeField(default=datetime.now)


class Spot(models.Model):
    number = models.IntegerField()


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, related_name='reservations',
                                 on_delete=models.CASCADE, blank=True)
    spot = models.ForeignKey(Spot, related_name='reservations',
                             on_delete=models.CASCADE, blank=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    created_at = models.DateTimeField(default=datetime.now)
