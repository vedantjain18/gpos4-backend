from rest_framework import serializers
from .models import AccountsLedgerPendingg

class AccountsLedgerPendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsLedgerPending
        fields = '__all__'
