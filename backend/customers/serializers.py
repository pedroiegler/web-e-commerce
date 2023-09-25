from rest_framework import serializers

from .models import Customer, User

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'date_of_birth',)
        read_only_fields = ('id',)
        
class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Senha"
    )