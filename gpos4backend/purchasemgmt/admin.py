from django.contrib import admin

# Register your models here.
from .models import PurchaseInvoiceRegister, PurchaseInvoiceRegisterDetails, PurchaseInvoicePending
admin.site.register(PurchaseInvoiceRegister)
admin.site.register(PurchaseInvoiceRegisterDetails)
admin.site.register(PurchaseInvoicePending)
