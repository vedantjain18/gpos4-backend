from django.contrib import admin

# Register your models here.
from .models import NatureOfGroup, AccountsGroup, AccountsMaster, VoucherType, AccountsVoucherEntry, CashHandover, ModeOfPayment, AccountsLedgerPending, OpeningAccounts
admin.site.register(NatureOfGroup)
admin.site.register(AccountsGroup)
admin.site.register(AccountsMaster)
admin.site.register(VoucherType)
admin.site.register(AccountsVoucherEntry)
admin.site.register(CashHandover)
admin.site.register(ModeOfPayment)
admin.site.register(AccountsLedgerPending)
admin.site.register(OpeningAccounts)
