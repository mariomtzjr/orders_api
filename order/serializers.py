from rest_framework import serializers

from drf_spectacular.utils import extend_schema_serializer, OpenApiExample

from .models import Order
from .models import OrderItem
from product.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'order', 'qty', 'unit_price', 'total_price')


@extend_schema_serializer(
    exclude_fields=(), # schema ignore these fields
    examples = [
         OpenApiExample(
            'Valid example por Order creation',
            summary='Creation of an Order',
            description='Creation of an Order',
            value={
                "operador": {
                "employee_number": 10011,
                "first_name": "Mario",
                "last_name": "Martinez"
            },
            "comensal": {
                "table_number": 3,
                "first_name": "Alfonso",
                "last_name": "Pedraza"
            },
            "order_items": [
                {
                    "qty": 2,
                    "name": "Coca-Cola 240 ml",
                    "unit_price": 25.00
                },
                {
                    "qty": 2,
                    "name": "Gintonic Blueberry 240 ml",
                    "unit_price": 45.00
                }
            ]
            },
            request_only=True, # signal that example only applies to requests
            response_only=False, # signal that example only applies to responses
        ),
    ]
)
class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'operador', 'comensal', 'order_items', 'grand_total', 'date')
    
    def create(self, validated_data):
        print("validated_data: ", validated_data)
        order_item_data = validated_data.pop('order_items')
        print("order_item_data: ", order_item_data)
        order = Order.objects.create(**validated_data)
        for order_item in order_item_data:
                OrderItem.objects.create(order=order, **order_item)
        return order


class OrderSerializerOutput(serializers.ModelSerializer):
    order_items = serializers.SlugRelatedField(many=True, read_only=True, slug_field='product')
    class Meta:
        model = Order
        fields = ('id', 'operador', 'comensal', 'order_items', 'grand_total', 'date')