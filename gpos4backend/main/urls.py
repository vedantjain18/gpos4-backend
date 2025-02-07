from django.urls import path
from .views import home, StockRegisterAllApi

urlpatterns = [
    path('', home, name='home'),
    path('api/stock-register-all/', StockRegisterAllApi.as_view(), name='stocks'),
]