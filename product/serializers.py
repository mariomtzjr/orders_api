from rest_framework import serializers

from drf_spectacular.utils import extend_schema_serializer, OpenApiExample

from .models import Product


@extend_schema_serializer(
    exclude_fields=(), # schema ignore these fields
    examples = [
         OpenApiExample(
            'Valid example por Product creation',
            summary='Creation of a Product',
            description='Creation of a Product',
            value={
                "name": "Coca-Cola 240 ml",
                "description": "Refresco Coca-Cola 240 ml",
                "quantity": 10,
                "value": 32.00
            },
            request_only=True, # signal that example only applies to requests
            response_only=False, # signal that example only applies to responses
        ),
    ]
)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'quantity', 'unit_price')
