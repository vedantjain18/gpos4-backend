from rest_framework import serializers
from .models import StockRegister

class StockRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockRegister
        fields = '__all__'