from rest_framework import serializers

from drf_spectacular.utils import extend_schema_serializer, OpenApiExample

from .models import Operator, Comensal


@extend_schema_serializer(
    exclude_fields=(), # schema ignore these fields
    examples = [
         OpenApiExample(
            'Valid example por Operator creation',
            summary='Creation of an Operator',
            description='Creation of an Operator',
            value={
                "employee_number": 10012,
                "first_name": "Eduardo",
                "last_name": "Martinez",
                "email": ""
            },
            request_only=True, # signal that example only applies to requests
            response_only=False, # signal that example only applies to responses
        ),
    ]
)
class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ('id', 'employee_number', 'first_name', 'last_name', 'email')


@extend_schema_serializer(
    exclude_fields=(), # schema ignore these fields
    examples = [
         OpenApiExample(
            'Valid example por Comensal creation',
            summary='Creation of a Comensal',
            description='Creation of a Comensal',
            value={
                "table_number": 1,
                "first_name": "Juan",
                "last_name": "Alvarez"
            },
            request_only=True, # signal that example only applies to requests
            response_only=False, # signal that example only applies to responses
        ),
    ]
)
class ComensalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comensal
        fields = ('id', 'table_number', 'first_name', 'last_name', )


