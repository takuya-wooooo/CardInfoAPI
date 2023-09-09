from django.urls import path
from .views import CreditCardListCreate

urlpatterns = [
    path('', CreditCardListCreate.as_view())
]
