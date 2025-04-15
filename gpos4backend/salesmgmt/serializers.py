from rest_framework import serializers
from .models import SalesBillPending, SalesReturnBillPending, SalesRegister, SalesQuotationPending, SalesOrderPending, SalesReturnRegister, SalesOrderRegisterDetails, SalesQuotationRegisterDetails, SalesOrderRegister, SalesQuotationRegister
from inventorymgmt.models import ItemMaster, ItemBarcode
from accounts.models import CashHandover

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

class SalesRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesRegister
        fields = '__all__'

class SalesRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesRegister
        fields = '__all__'

class SalesQuotationPendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesQuotationPending
        fields = '__all__'

class SalesOrderPendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderPending
        fields = '__all__'

class SalesReturnRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReturnRegister
        fields = '__all__'

class CashHandoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashHandover
        fields = '__all__'

class SalesOrderRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderRegister
        fields = '__all__'

class SalesQuotationRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesQuotationRegister
        fields = '__all__'

class SalesQuotationRegisterDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesQuotationRegisterDetails
        fields = '__all__'

class SalesOrderRegisterDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderRegisterDetails
        fields = '__all__'

class ItemBarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemBarcode
        fields = '__all__'
