from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderSerializerOutput
from user.models import Comensal, Operator
from product.models import Product
from .filters import OrderFilter


# Create your views here.
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderFilter

    def get(self, request):
        query_params = self.request.query_params
        queryset = self.get_queryset()
        serializer = OrderSerializer(queryset, many=True)
        
        return Response(serializer.data)


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request):
        serializer = OrderSerializer(data=request.data)

        operador = serializer.initial_data['operador']
        operador, created_ = Operator.objects.get_or_create(employee_number=operador)

        comensal_data = serializer.initial_data.get("comensal")
        comensal, created = Comensal.objects.get_or_create(**comensal_data)

        serializer.initial_data["comensal"] = comensal.id
        products = serializer.initial_data.get("order_items")

        for product in products:
            product_found = Product.objects.filter(name__exact=product.get('name')).first()
            if not product_found:
                obj = Product.objects.create(
                    name=product.get('name'),
                    unit_price=product.get('unit_price'),
                    quantity=product.get('qty')
                )
                product['product'] = obj.id
            else:
                prod = Product.objects.filter(name__exact=product.get('name')).first()
                product['product'] = prod.id

        if serializer.is_valid():
            order =  serializer.save()
            
            print("Order: ", order)
            print("Order id: ", order.id)
            print("Order items: ", order.order_items.all())
            data_response = OrderSerializerOutput(order).data
            print("data_response: ", data_response)
            order_items_processed = [{
                'id': item.id,
                'product': item.product.name,
                'unit_price': item.unit_price,
                'quantity': item.qty,
                'total': item.total_price
            } for item in order.order_items.all()]
            data_response['order_items'] = order_items_processed

            return Response(data_response, status=201)
        return Response(serializer.errors, status=400)