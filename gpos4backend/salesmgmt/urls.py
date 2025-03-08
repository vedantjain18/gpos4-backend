from django.contrib import admin
from django.urls import path, include
from .views import ItemMasterSearchByNameApi, SalesBillPendingApi, SalesReturnBillPendingApi

urlpatterns = [
    # path('', home, name='home'),
    path('api/item-master-search-by-name/', ItemMasterSearchByNameApi.as_view(), name='item-master-search-by-name'),
    path('api/sales-bill-pending/', SalesBillPendingApi.as_view(), name='sales-bill-pending'),
    path('api/sales-return-bill-pending/', SalesReturnBillPendingApi.as_view(), name='sales-return-bill-pending'),

]