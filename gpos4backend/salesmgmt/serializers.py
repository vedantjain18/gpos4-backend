from rest_framework import serializers
from .models import SalesBillPending, SalesReturnBillPending, SalesRegister, SalesTransactionDetails, SalesQuotationPending, SalesOrderPending, SalesReturnsTransactionDetails, OrderTransactionDetails, QuotationTransactionDetails, OrderRegister, QuotationRegister
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

class SalesTransactionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesTransactionDetails
        fields = '__all__'

class SalesQuotationPendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesQuotationPending
        fields = '__all__'

class SalesOrderPendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderPending
        fields = '__all__'

class SalesReturnsTransactionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesReturnsTransactionDetails
        fields = '__all__'

class CashHandoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashHandover
        fields = '__all__'

class OrderRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderRegister
        fields = '__all__'

class QuotationRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationRegister
        fields = '__all__'

class QuotationTransactionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuotationTransactionDetails
        fields = '__all__'

class OrderTransactionDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTransactionDetails
        fields = '__all__'

class ItemBarcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemBarcode
        fields = '__all__'
