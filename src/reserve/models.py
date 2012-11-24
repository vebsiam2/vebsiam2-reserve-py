from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    quantity = models.IntegerField()

class Reservation(models.Model):
    reserved_to = models.CharField(max_length=256)
    reserved_by = models.CharField(max_length=256)
    reserved_date = models.DateTimeField()
    reserved_on = models.DateTimeField()

