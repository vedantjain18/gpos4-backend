from django.urls import path
from .views import OwnerManageView, BusniessCreateViewApi

urlpatterns = [
    # path('', views.home, name='home'),
    path('api/owner-manage/', OwnerManageView.as_view(), name='owner-manage'),
    path('api/business-create/', BusniessCreateViewApi.as_view(), name='business-create'),

]