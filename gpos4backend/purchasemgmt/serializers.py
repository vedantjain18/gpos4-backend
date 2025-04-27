from rest_framework import serializers
from .models import PurchaseInvoiceRegister, PurchaseInvoicePending, PurchaseOrderRegister, PurchaseChallanRegister, PurchaseInvoiceRegisterDetails

class PurchaseInvoiceRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoiceRegister
        fields = '__all__'

class PurchaseInvoicePendingSerializer(serializers.ModelSerializer):
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