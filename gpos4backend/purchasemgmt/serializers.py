from rest_framework import serializers
from .models import PurchaseRegister

class PurchaseRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRegister
        fields = '__all__'
