from django.urls import path
from .views import AccountsLedgerPendingApi

urlpatterns = [
    # path('', views.home, name='home'),
    path('accounts-ledger-pending/', AccountsLedgerPendingApi.as_view(), name='accounts-ledger-pending'),

]