from rest_framework import serializers
from .models import StockRegister, PhysicalStockTakingPending, PriceTagsPrinting

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