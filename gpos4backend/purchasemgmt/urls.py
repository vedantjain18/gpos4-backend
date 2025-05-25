from django.urls import path
from .views import home, PurchaseInvoiceRegisterApi, PurchaseInvoicePendingApi, PurchaseOrderRegisterApi, PurchaseChallanRegisterApi, PurchaseInvoiceRegisterDetailsApi

urlpatterns = [
    path('', home, name='home'),
    path('purchase-invoice-register/', PurchaseInvoiceRegisterApi.as_view(), name='purchase-invoice-register'),
    path('purchase-invoice-pending/', PurchaseInvoicePendingApi.as_view(), name='purchase-invoice-pending'),
    path('purchase-order-register/', PurchaseOrderRegisterApi.as_view(), name='purchase-order-register'),
    path('purchase-challan-register/', PurchaseChallanRegisterApi.as_view(), name='purchase-challan-register'),
    path('purchase-invoice-register-details/', PurchaseInvoiceRegisterDetailsApi.as_view(), name='purchase-invoice-register-details'),


]