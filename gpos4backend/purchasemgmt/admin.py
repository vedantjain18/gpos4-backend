from django.contrib import admin

# Register your models here.
from .models import PurchaseRegister, PurchaseDetails, PurchasePending
admin.site.register(PurchaseRegister)
admin.site.register(PurchaseDetails)
admin.site.register(PurchasePending)
