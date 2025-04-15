from rest_framework import serializers
from .models import OwnerMaster, BusinessMaster, LocationMaster, EmployeeMaster, LocationType

class OwnerMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerMaster
        fields = '__all__'

class BusinessMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessMaster
        fields = '__all__'

class LocationMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationMaster
        fields = '__all__'

class EmployeeMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeMaster
        fields = '__all__'

class LocationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationType
        fields = '__all__'