from django.urls import path
from .views import home, PurchaseRegisterApi

urlpatterns = [
    path('', home, name='home'),
    path('api/purchase-register-all/', PurchaseRegisterApi.as_view(), name='purchase-register-all'),

]