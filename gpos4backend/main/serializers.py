from rest_framework import serializers
from .models import ItemTaxMaster, ItemTaxContainer, ItemHSN, CentralDataHSN, CentralDataPincode, CentralDataCurrency, CentralDataIngredients, CentralDataLocationType, CentralDataNatureOfGroup, CentralDataAccountsGroup, CentralDataAccountsMaster, CentralDataVoucherType, CentralDataItemType

class CentralDataLocationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralDataLocationType
        fields = '__all__'

class ItemTaxMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTaxMaster
        fields = '__all__'

class ItemTaxContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTaxContainer
        fields = '__all__'

class ItemHSNSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemHSN
        fields = '__all__'

class CentralDataHSNSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralDataHSN
        fields = '__all__'

class CentralDataPincodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralDataPincode
        fields = '__all__'

class CentralDataCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralDataCurrency
        fields = '__all__'

class CentralDataIngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralDataIngredients
        fields = '__all__'

class CentralDataNatureOfGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralDataNatureOfGroup
        fields = '__all__'

class CentralDataAccountsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralDataAccountsGroup
        fields = '__all__'

class CentralDataAccountsMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralDataAccountsMaster
        fields = '__all__'
    
class CentralDataVoucherTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralDataVoucherType
        fields = '__all__'

class CentralDataItemTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralDataItemType
        fields = '__all__'
















