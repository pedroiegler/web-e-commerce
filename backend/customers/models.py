from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
        
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    
class User(AbstractUser):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    email = models.EmailField(max_length=254, unique=True, error_messages={'unique': "O email cadastrado já existe."})
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_set')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')
    
    USERNAME_FIELD = 'email'