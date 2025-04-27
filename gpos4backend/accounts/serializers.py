from rest_framework import serializers
from .models import AccountsLedgerPending, AccountsMaster

class AccountsLedgerPendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsLedgerPending
        fields = '__all__'

class AccountsMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsMaster
        fields = '__all__'
