from rest_framework import serializers
from .models import PurchaseInvoiceRegister, PurchaseInvoicePending, PurchaseOrderRegister, PurchaseChallanRegister, PurchaseInvoiceRegisterDetails
from main.serializers import ItemTaxMasterSerializer

class PurchaseInvoiceRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoiceRegister
        fields = '__all__'

class PurchaseInvoicePendingSerializer(serializers.ModelSerializer):
    item_tax_id = ItemTaxMasterSerializer(read_only=True)
    class Meta:
        model = PurchaseInvoicePending
        fields = '__all__'

class PurchaseOrderRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderRegister
        fields = '__all__'

class PurchaseChallanRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseChallanRegister
        fields = '__all__'

class PurchaseInvoiceRegisterDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoiceRegisterDetails
        fields = '__all__'