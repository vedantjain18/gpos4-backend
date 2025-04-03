from django.urls import path
from .views import CentralDataLocationTypeView

urlpatterns = [
    # path('', views.home, name='home'),
    path('central-location-type/', CentralDataLocationTypeView.as_view(), name='central-location-type'),
]