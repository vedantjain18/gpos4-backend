from django.contrib import admin
from django.urls import path, include
from .views import ItemMasterSearchByNameApi, SalesBillPendingApi, SalesReturnBillPendingApi, SalesRegisterApi, SalesOrderPendingApi, SalesQuotationPendingApi, OrderRegisterApi, QuotationRegisterApi

urlpatterns = [
    # path('', home, name='home'),
    path('item-master-search-by-name/', ItemMasterSearchByNameApi.as_view(), name='item-master-search-by-name'),
    path('sales-bill-pending/', SalesBillPendingApi.as_view(), name='sales-bill-pending'),
    path('sales-return-bill-pending/', SalesReturnBillPendingApi.as_view(), name='sales-return-bill-pending'),
    path('sales-register/', SalesRegisterApi.as_view(), name='sales-register'),
    path('sales-order-pending/', SalesOrderPendingApi.as_view(), name='sales-order-pending'),
    path('sales-quotation-pending/', SalesQuotationPendingApi.as_view(), name='sales-quotation-pending'),
    path('quotation-register/', QuotationRegisterApi.as_view(), name='quotation-register'),
    path('order-register/', OrderRegisterApi.as_view(), name='order-register'),

]