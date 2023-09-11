from rest_framework import serializers
from .models import CreditCard, CardCategory, CardReview


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ['id', 'name', 'point_rate', 'annual_fee']

class CardCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CardCategory
        fields = ['id', 'name']

class CardReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardReview
        fields = ['id', 'name', 'rate', 'comment']
