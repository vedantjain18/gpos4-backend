from django.contrib import admin

# Register your models here.
from .models import OwnerMaster, BusinessMaster
admin.site.register(OwnerMaster)
admin.site.register(BusinessMaster)