from django.urls import path
from .views import OwnerMasterApi, BusniessMasterViewApi

urlpatterns = [
    # path('', views.home, name='home'),
    path('owner-master/', OwnerMasterApi.as_view(), name='owner-master'),
    path('business-master/', BusniessMasterViewApi.as_view(), name='business-master'),

]