from rest_framework import generics
from .models import CreditCard
from .serializers import CreditCardSerializer


class CreditCardListCreate(generics.ListAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
