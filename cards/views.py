from rest_framework import generics, status
from rest_framework.response import Response
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

class CardCompare(generics.ListAPIView):
    serializer_class = CreditCardSerializer

    def get_queryset(self):
        ids = self.request.query_params.get('ids', '')
        ids = [int(id) for id in ids.split(',') if id.isdigit()]
        return CreditCard.objects.filter(id__in=ids)

    def get(self, request, *args, **kwargs):
        ids = request.query_params.get('ids', '')
        ids = [int(id) for id in ids.split(',') if id.isdigit()]

        cards = CreditCard.objects.filter(id__in=ids)
        if len(cards) != len(ids):
            return Response(
                {
                    "message": "クレジットカードが見つかりませんでした"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(cards, many=True)
        return Response(serializer.data)
