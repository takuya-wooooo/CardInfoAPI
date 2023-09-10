from rest_framework import serializers
from .models import CreditCard, CardCategory


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ['id', 'name', 'point_rate', 'annual_fee']

class CardCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CardCategory
        fields = ['id', 'name']
