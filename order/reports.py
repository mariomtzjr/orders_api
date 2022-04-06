
from django.db.models import Sum

from order.models import Order

def order_report():
    data = []

    queryset = Order.objects.values('order_items').annotate(total=Sum('order_items__price'))