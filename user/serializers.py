from rest_framework import serializers


from .models import Operator, Comensal


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ('id', 'employee_number', 'first_name', 'last_name', 'email')


class ComensalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comensal
        fields = ('id', 'table_number', 'first_name', 'last_name')


