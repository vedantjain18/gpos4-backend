from rest_framework import serializers
from .models import StockRegister, PhysicalStockTakingPending, PriceTagsPrinting, ItemType, ItemUnit, ItemMaster, Company, ItemBrand, ItemCategory, ItemGroup, ItemSubGroup, OpeningStock, ItemIngredientsMaster, StockManipulationType, StockManipulation, ItemBarcode

class StockRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockRegister
        fields = '__all__'

class PhysicalStockTakingPendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalStockTakingPending
        fields = '__all__'

class PriceTagsPrintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceTagsPrinting
        fields = '__all__'

class ItemMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMaster
        fields = '__all__'

class ItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemType
        fields = '__all__'

class ItemUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemUnit
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ItemBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemBrand
        fields = '__all__'

class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCategory
        fields = '__all__'

class ItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemGroup
        fields = '__all__'

class ItemSubGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSubGroup
        fields = '__all__'

class OpeningStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningStock
        fields = '__all__'

class ItemIngredientsMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemIngredientsMaster
        fields = '__all__'

class StockManipulationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockManipulationType
        fields = '__all__'

class StockManipulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockManipulation
        fields = '__all__'

class ItemBarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemBarcode
        fields = '__all__'