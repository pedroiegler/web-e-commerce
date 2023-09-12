from django.shortcuts import render
from rest_framework import mixins, generics, permissions

from .models import Customer
from .serializers import CustomerSerializer

class CustomerListAPIView(generics.ListAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        return Customer.objects.all()

class CustomerCreateAPIView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]