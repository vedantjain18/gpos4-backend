from django.contrib import admin

# Register your models here.
from .models import SalesBillPending, SalesRegister, SalesTransactionDetails, SalesReturnRegister, SalesReturnsTransactionDetails
admin.site.register(SalesBillPending)
admin.site.register(SalesRegister)
admin.site.register(SalesTransactionDetails)
admin.site.register(SalesReturnRegister)
admin.site.register(SalesReturnsTransactionDetails)
