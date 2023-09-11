from rest_framework import generics
from .models import CreditCard, CardCategory, CardReview
from .serializers import CreditCardSerializer, CardCategorySerializer, CardReviewSerializer
from .filters import CreditCardFilter


class CardCategoryListCreate(generics.ListCreateAPIView):
    queryset = CardCategory.objects.all()
    serializer_class = CardCategorySerializer

class CreditCardListCreate(generics.ListAPIView):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    filterset_class = CreditCardFilter

class CardReviewListCreate(generics.ListAPIView):
    queryset = CardReview.objects.all()
    serializer_class = CardReviewSerializer
