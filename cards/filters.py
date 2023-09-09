import django_filters
from .models import CreditCard


class CreditCardFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CreditCard
        fields = ['name']
