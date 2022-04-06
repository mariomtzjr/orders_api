from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from .serializers import OperatorSerializer
from .models import Operator


# Create your views here.
class OperatorListView(generics.ListAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

    def get(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = OperatorSerializer(queryset, many=True)
        print("Serializer: ", serializer)
        return Response(serializer.data)


class OperatorCreateView(generics.CreateAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

    def post(self, request):
        serializer = OperatorSerializer(data=request.data)
        if serializer.is_valid():
            operator = serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)