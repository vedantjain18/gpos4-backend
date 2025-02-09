from django.urls import path
from .views import OwnerManageView

urlpatterns = [
    # path('', views.home, name='home'),
    path('api/owner-manage/', OwnerManageView.as_view(), name='owner-manage'),
]