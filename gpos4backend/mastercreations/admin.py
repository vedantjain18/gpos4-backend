from django.contrib import admin

# Register your models here.
from .models import OwnerMaster, BusinessMaster, LocationMaster, EmployeeMaster
admin.site.register(OwnerMaster)
admin.site.register(BusinessMaster)
admin.site.register(LocationMaster)
admin.site.register(EmployeeMaster)