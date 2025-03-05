from django.db import models
from accounts.models import *
from mastercreations.models import *

# Create your models here.
class CustomerMaster(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False,)
    # accid = models.IntegerField(null=False, blank=False) [Will be automatically added by Django]
    customer_name = models.CharField(null=False, blank=False, max_length=120)
    customer_account_id = models.ForeignKey(AccountsMaster, on_delete=models.CASCADE,  blank=False, null=False)
    customer_phone = models.IntegerField(null=True, blank=True)
    customer_whatsapp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) # Set default to 0
    customer_add1 = models.CharField(max_length=220, null=True, blank=True)
    customer_add2 = models.CharField(max_length=30, null=True, blank=True)
    customer_city = models.CharField(max_length=30, null=True, blank=True)
    customer_pincode = models.IntegerField(null=True, blank=True)
    customer_glos_lat = models.DecimalField(max_digits=100, decimal_places=100, null=True, blank=True)
    customer_glos_lang = models.DecimalField(max_digits=100, decimal_places=100, null=True, blank=True)
    customer_email = models.CharField(max_length=120, null=True, blank=True)
    customer_type = models.CharField(max_length=120, null=True, blank=True) # B2C B2b Whoelsale Retail
    customer_allow_credit = models.BooleanField(default=False)
    customer_credit_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    customer_birthdate = models.DateField(null=True, blank=True)
    customer_anniversary = models.DateField(null=True, blank=True)
    customer_location_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.acc_name)