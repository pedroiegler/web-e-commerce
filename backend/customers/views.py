from django.shortcuts import render
from rest_framework import mixins, generics, permissions, viewsets

from .models import Customer, User
from .serializers import CustomerSerializer, UserSerializer

class CustomerListAPIView(generics.ListAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        return Customer.objects.all()

class CustomerCreateAPIView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]
    
    
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ListUsers(generics.ListAPIView):
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    serializer_class = UserSerializer
    