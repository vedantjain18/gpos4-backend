from django.urls import path
from .views import home, StockRegisterAllApi, PhysicalStockTakingPendingApi, PriceTagsPrintingApi

urlpatterns = [
    path('', home, name='home'),
    path('api/stock-register-all/', StockRegisterAllApi.as_view(), name='stock-register-all'),
    path('api/physical-stock-taking-pending/', PhysicalStockTakingPendingApi.as_view(), name='physical-stock-taking-pending'),
    path('api/price-tags-printing/', PriceTagsPrintingApi.as_view(), name='price-tags-printing'),
]