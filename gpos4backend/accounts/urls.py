from django.urls import path
from .views import AccountsLedgerPendingApi, AccountsMasterApi

urlpatterns = [
    # path('', views.home, name='home'),
    path('accounts-ledger-pending/', AccountsLedgerPendingApi.as_view(), name='accounts-ledger-pending'),
    path('accounts-master/', AccountsMasterApi.as_view(), name='accounts-master'),

]