from django.contrib import admin

# Register your models here.
from .models import SalesBillPending, SalesRegister, SalesRegisterDetails, SalesReturnRegister, SalesReturnRegisterDetails
admin.site.register(SalesBillPending)
admin.site.register(SalesRegister)
admin.site.register(SalesRegisterDetails)
admin.site.register(SalesReturnRegister)
admin.site.register(SalesReturnRegisterDetails)
