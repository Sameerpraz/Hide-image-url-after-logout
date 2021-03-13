from django.shortcuts import render
from .serializers import CustomerSerializer
from rest_framework import viewsets
from .models import Customer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from django.shortcuts import get_object_or_404

from rest_framework.response import Response

# Create your views here.
from .permissions import CustomDjangoModelPermissions
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (CustomDjangoModelPermissions, )


    # def retrieve(self, request, pk=None):
    #     queryset = Customer.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = CustomerSerializer(Customer)
    #     return Response(serializer.data)


