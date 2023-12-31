from django.urls import path
from .views import CreditCardListCreate, CardCategoryListCreate, CardReviewListCreate, CardCompare

urlpatterns = [
    path('', CreditCardListCreate.as_view()),
    path('/category', CardCategoryListCreate.as_view()),
    path('/categories/<int:category_id>/cards/', CardCategoryListCreate.as_view()),
    path('/review', CardReviewListCreate.as_view()),
    path('/compare', CardCompare.as_view()),
]
