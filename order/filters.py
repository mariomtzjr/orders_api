
from django_filters import rest_framework as filters

from order.models import Order


class OrderFilter(filters.FilterSet):
    operador = filters.CharFilter(field_name='operador__first_name', lookup_expr='icontains')
    start_date = filters.DateFilter(lookup_expr='gte')
    end_date = filters.DateFilter(lookup_expr='lte')

    class Meta:
        model = Order
        fields = ['operador', 'start_date', 'end_date']