from django.contrib import admin

# Register your models here.
from .models import ItemTaxMaster, ItemTaxContainer, ItemHSN, CentralDataHSN, CentralDataPincode, CentralDataCurrency, CentralDataIngredients, CentralDataLocationType, CentralDataNatureOfGroup, CentralDataAccountsGroup, CentralDataAccountsMaster, CentralDataVoucherType, CentralDataItemType
admin.site.register(ItemTaxMaster)
admin.site.register(ItemTaxContainer)
admin.site.register(ItemHSN)
admin.site.register(CentralDataHSN)
admin.site.register(CentralDataPincode)
admin.site.register(CentralDataCurrency)
admin.site.register(CentralDataIngredients)
admin.site.register(CentralDataLocationType)
admin.site.register(CentralDataNatureOfGroup)
admin.site.register(CentralDataAccountsGroup)
admin.site.register(CentralDataAccountsMaster)
admin.site.register(CentralDataVoucherType)
admin.site.register(CentralDataItemType)
