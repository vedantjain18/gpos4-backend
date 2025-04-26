from django.urls import path
from .views import OwnerMasterApi, BusniessMasterViewApi, LocationMasterApi, EmployeeMasterApi, LocationTypeApi

urlpatterns = [
    # path('', views.home, name='home'),
    path('owner-master/', OwnerMasterApi.as_view(), name='owner-master'),
    path('business-master/', BusniessMasterViewApi.as_view(), name='business-master'),
    path('location-master/', LocationMasterApi.as_view(), name='location-master'),
    path('employee-master/', EmployeeMasterApi.as_view(), name='employee-master'),
    path('location-type/', LocationTypeApi.as_view(), name='location-type'),

]