from django.db import models
from django.contrib.auth.models import User


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

class CardReview(models.Model):
    name = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField
    comment = models.TextField()
