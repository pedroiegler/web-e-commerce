from django.urls import path, include
from rest_framework import routers
from django.contrib import admin

from . import views

app_name = 'customers'

router = routers.DefaultRouter()
router.register('cadastrar_usuario', views.UsersViewSet, basename='Cadastrar Usuário')

urlpatterns = [
    path('customers/', views.CustomerListAPIView.as_view(), name='customer-list'),
    path('customers/create/', views.CustomerCreateAPIView.as_view(), name='customer-create'),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cadastrar_usuario/', views.ListUsers.as_view())
]
