from rest_framework import generics
from .models import CreditCard, CardCategory
from .serializers import CreditCardSerializer, CardCategorySerializer
from .filters import CreditCardFilter


class CardCategoryListCreate(generics.ListCreateAPIView):
    queryset = CardCategory.objects.all()
    serializer_class = CardCategorySerializer

class CreditCardListCreate(generics.ListAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    filterset_class = CreditCardFilter
