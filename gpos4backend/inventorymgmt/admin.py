from django.contrib import admin

# Register your models here.
from .models import StockRegister, ItemType, ItemUnit, Company, ItemBrand, ItemCategory, ItemGroup, ItemSubGroup, ItemMaster, OpeningStock, ItemIngredientsMaster, PhysicalStockTakingPending, StockManipulationType, StockManipulation, PriceTagsPrinting, ItemBarcode
admin.site.register(StockRegister)
admin.site.register(ItemType)
admin.site.register(ItemUnit)
admin.site.register(Company)
admin.site.register(ItemBrand)
admin.site.register(ItemCategory)
admin.site.register(ItemGroup)
admin.site.register(ItemSubGroup)
admin.site.register(ItemMaster)
admin.site.register(OpeningStock)
admin.site.register(ItemIngredientsMaster)
admin.site.register(PhysicalStockTakingPending)
admin.site.register(StockManipulationType)
admin.site.register(StockManipulation)
admin.site.register(PriceTagsPrinting)
admin.site.register(ItemBarcode)
