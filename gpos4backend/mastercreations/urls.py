from django.urls import path
from .views import OwnerManageView, BusniessCreateViewApi

urlpatterns = [
    # path('', views.home, name='home'),
    path('owner-manage/', OwnerManageView.as_view(), name='owner-manage'),
    path('business-create/', BusniessCreateViewApi.as_view(), name='business-create'),

]