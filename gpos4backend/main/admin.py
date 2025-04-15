from django.contrib import admin

# Register your models here.
from .models import ItemTaxMaster, ItemTaxContainer, ItemHSN, CentralDataHSN, CentralDataPincode, CentralDataCurrency, CentralDataIngredients, CentralDataLocationType
admin.site.register(ItemTaxMaster)
admin.site.register(ItemTaxContainer)
admin.site.register(ItemHSN)
admin.site.register(CentralDataHSN)
admin.site.register(CentralDataPincode)
admin.site.register(CentralDataCurrency)
admin.site.register(CentralDataIngredients)
admin.site.register(CentralDataLocationType)
