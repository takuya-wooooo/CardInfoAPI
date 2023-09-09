from django.urls import path
from .views import CreditCardListCreate

urlpatterns = [
    path('cards/', CreditCardListCreate.as_view())
]
