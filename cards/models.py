from django.db import models


class CardCategory(models.Model):
    name = models.CharField(max_length=255)

class CreditCard(models.Model):
    name = models.CharField(max_length=255)
    point_rate = models.FloatField()
    annual_fee = models.IntegerField()
    category = models.ForeignKey(
        CardCategory,
        on_delete=models.CASCADE,
        related_name="cards",
        null=True,
        blank=True
    )
