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
    
    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Confirme a senha"
    )
    
    is_staff = serializers.BooleanField(
        label="Membro da Equipe",
        help_text="Indica que usuário consegue acessar o site de administração."
    )
    
    is_superuser = serializers.BooleanField(
        label="SuperUsuário",
        help_text="Indica que este usuário tem todas as permissões sem atribuí-las explicitamente."
    )
    
    class Meta:
        model = User
        fields = ('username','email','password','password_confirm','is_staff','is_superuser')
        extra_kwargs = {'password':{'write_only': True}}
        
    def save(self):
        conta = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            is_staff=self.validated_data['is_staff'],
            is_superuser=self.validated_data['is_superuser']
        )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']
        
        if password != password_confirm:
            raise serializers.ValidationError({'password': 'As senhas não são iguais.'})
        conta.set_password(password)
        conta.save()
        return conta
        
        
        
        
        
        