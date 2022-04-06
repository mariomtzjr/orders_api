from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from .serializers import OperatorSerializer, ComensalSerializer
from .models import Operator, Comensal


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


class OperatorDetailView(generics.RetrieveAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

    def get(self, request, pk):
        operator = self.get_object()
        serializer = OperatorSerializer(operator)
        return Response(serializer.data)


class ComensalDetailView(generics.RetrieveAPIView):
    queryset = Comensal.objects.all()
    serializer_class = OperatorSerializer

    def get(self, request, pk):
        comensal = self.get_object()
        serializer = ComensalSerializer(comensal)
        return Response(serializer.data)