from django.contrib import admin

# Register your models here.
from .models import Owner, Business
admin.site.register(Owner)
admin.site.register(Business)