from django.db import models


class CreditCard(models.Model):
    name = models.CharField(max_length=255)
    point_rate = models.FloatField()
    annual_fee = models.IntegerField()
