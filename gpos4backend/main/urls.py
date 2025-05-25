from django.urls import path
from .views import CentralDataLocationTypeView, ItemTaxMasterApi

urlpatterns = [
    # path('', views.home, name='home'),
    path('central-location-type/', CentralDataLocationTypeView.as_view(), name='central-location-type'),
    path('item-tax-master/', ItemTaxMasterApi.as_view(), name='item-tax-master'),
]