from django.contrib import admin
from django.urls import path, include
from .views import ItemMasterSearchByNameApi, SalesBillPendingApi, SalesReturnBillPendingApi, SalesRegisterApi, SalesReturnRegisterApi, SalesOrderPendingApi, SalesQuotationPendingApi, SalesOrderRegisterApi, SalesQuotationRegisterApi

urlpatterns = [
    # path('', home, name='home'),
    path('item-master-search-by-name/', ItemMasterSearchByNameApi.as_view(), name='item-master-search-by-name'),
    path('sales-bill-pending/', SalesBillPendingApi.as_view(), name='sales-bill-pending'),
    path('sales-return-bill-pending/', SalesReturnBillPendingApi.as_view(), name='sales-return-bill-pending'),
    path('sales-register/', SalesRegisterApi.as_view(), name='sales-register'),
    path('sales-return-register/', SalesReturnRegisterApi.as_view(), name='sales-return-register'),
    path('sales-order-register/', SalesOrderRegisterApi.as_view(), name='sales-order-register'),
    path('sales-order-pending/', SalesOrderPendingApi.as_view(), name='sales-order-pending'),
    path('sales-quotation-pending/', SalesQuotationPendingApi.as_view(), name='sales-quotation-pending'),
    path('sales-quotation-register/', SalesQuotationRegisterApi.as_view(), name='sales-quotation-register'),
]