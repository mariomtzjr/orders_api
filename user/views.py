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
        
        return Response(serializer.data)


class OperatorCreateView(generics.CreateAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

    def post(self, request):
        serializer = OperatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class OperatorDetailView(generics.RetrieveAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

    def get(self, request, pk):
        try:
            operator = Operator.objects.get(pk=pk)
            if not operator:
                return Response({"error": f"Operator with id={pk} not found"}, status=404)
        except:
            operator = Operator.objects.get(employee_number=pk)
            if not operator:
                return Response({"error": f"Operator with employee_number={pk} not found"}, status=404)

        serializer = OperatorSerializer(operator)
        return Response(serializer.data)



class ComensalCreateView(generics.CreateAPIView):
    queryset = Comensal.objects.all()
    serializer_class = ComensalSerializer

    def post(self, request):
        serializer = ComensalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ComensalDetailView(generics.RetrieveAPIView):
    queryset = Comensal.objects.all()
    serializer_class = OperatorSerializer

    def get(self, request, pk):
        try:
            comensal = Comensal.objects.get(pk=pk)
            if not comensal:
                return Response({"error": f"Comensal with id={pk} not found"}, status=404)
        except:
            return Response({"error": f"Comensal not found"}, status=404)
            
        serializer = ComensalSerializer(comensal)
        return Response(serializer.data)