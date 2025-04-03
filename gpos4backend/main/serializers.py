from rest_framework import serializers
from .models import CentralDataLocationType

class CentralDataLocationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentralDataLocationType
        fields = '__all__'