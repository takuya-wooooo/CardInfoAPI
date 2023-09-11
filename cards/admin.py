from django.contrib import admin
from .models import CreditCard, CardCategory, CardReview

admin.site.register(CreditCard)
admin.site.register(CardCategory)
admin.site.register(CardReview)
