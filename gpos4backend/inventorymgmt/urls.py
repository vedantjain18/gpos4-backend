from django.urls import path
from .views import home, StockRegisterAllApi, PhysicalStockTakingPendingApi, PriceTagsPrintingApi

urlpatterns = [
    path('', home, name='home'),
    path('stock-register-all/', StockRegisterAllApi.as_view(), name='stock-register-all'),
    path('physical-stock-taking-pending/', PhysicalStockTakingPendingApi.as_view(), name='physical-stock-taking-pending'),
    path('price-tags-printing/', PriceTagsPrintingApi.as_view(), name='price-tags-printing'),
]