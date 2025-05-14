from django.contrib import admin

# Register your models here.
from .models import SalesBillPending, SalesRegister, SalesRegisterDetails, SalesType, SalesReturnRegister, SalesReturnRegisterDetails, SalesOrderRegister, SalesOrderRegisterDetails, SalesOrderPending, SalesReturnRegisterMOP, SalesReturnBillPending, SalesRegisterSatusControl, SalesRegisterMOP, SalesQuotationPending, SalesQuotationRegister, SalesQuotationRegisterDetails
admin.site.register(SalesBillPending)
admin.site.register(SalesRegister)
admin.site.register(SalesRegisterDetails)
admin.site.register(SalesReturnRegister)
admin.site.register(SalesReturnRegisterDetails)
admin.site.register(SalesOrderRegister)
admin.site.register(SalesOrderRegisterDetails)
admin.site.register(SalesOrderPending)
admin.site.register(SalesReturnRegisterMOP)
admin.site.register(SalesReturnBillPending)
admin.site.register(SalesRegisterSatusControl)
admin.site.register(SalesRegisterMOP)
admin.site.register(SalesQuotationPending)
admin.site.register(SalesQuotationRegister)
admin.site.register(SalesQuotationRegisterDetails)
admin.site.register(SalesType)

