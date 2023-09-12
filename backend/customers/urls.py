from django.urls import path

from . import views

app_name = 'customers'

urlpatterns = [
    path('customers/', views.CustomerListAPIView.as_view(), name='customer-list'),
    path('customers/create/', views.CustomerCreateAPIView.as_view(), name='customer-create'),
]
