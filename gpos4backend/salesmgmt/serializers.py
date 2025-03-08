from rest_framework import serializers
from .models import ItemMaster, SalesBillPending, SalesReturnBillPending

class ItemMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMaster
        fields = '__all__'

class SalesBillPendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesBillPending
        fields = '__all__'

class SalesReturnBillPendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReturnBillPending
        fields = '__all__'