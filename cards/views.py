from rest_framework import generics
from .models import CreditCard
from .serializers import CreditCardSerializer
from .filters import CreditCardFilter


class CreditCardListCreate(generics.ListAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    filterset_class = CreditCardFilter
