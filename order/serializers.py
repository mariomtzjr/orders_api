from rest_framework import serializers

from .models import Order
from .models import OrderItem
from product.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'order', 'qty', 'unit_price', 'total_price')


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'operador', 'comensal', 'order_items', 'grand_total', 'date')
    
    def create(self, validated_data):
        print("validated_data: ", validated_data)
        order_item_data = validated_data.pop('order_items')

        order = Order.objects.create(**validated_data)
        for order_item in order_item_data:
                OrderItem.objects.create(order=order, **order_item)
        return order


class OrderSerializerOutput(serializers.ModelSerializer):
    order_items = serializers.SlugRelatedField(many=True, read_only=True, slug_field='product')
    class Meta:
        model = Order
        fields = ('id', 'operador', 'comensal', 'order_items', 'grand_total', 'date')