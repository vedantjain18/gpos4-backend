from django.db import models

# Create your models here.
class OwnerMaster(models.Model):
    firstname = models.CharField(max_length=80, blank=False, null=False)
    lastname = models.CharField(max_length=80, blank=False, null=False)
    username = models.CharField(max_length=50, blank=False, null=False, unique=True)
    password = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    mobile = models.BigIntegerField(blank=False, null=False)
    whatsapp = models.BigIntegerField( blank=True, null=True)
    address1 = models.TextField(blank=False, null=False)
    address2 = models.TextField(blank=False, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    pin = models.BigIntegerField(blank=False, null=False)
    district = models.CharField(max_length=255, blank=False, null=False)
    state = models.CharField(max_length=255, blank=False, null=False)
    country = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return self.firstname + " " + self.lastname
    
class BusinessMaster(models.Model):
    owner_id = models.ForeignKey(OwnerMaster, on_delete=models.CASCADE)
    businessname = models.CharField(max_length=15, blank=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    address1 = models.TextField(blank=False, null=False)
    address2 = models.TextField(blank=False, null=False)
    gstin = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=False, null=False)
    pin = models.CharField(max_length=10, blank=False, null=False)
    district = models.CharField(max_length=10, blank=False, null=False)
    state = models.CharField(max_length=255, blank=False, null=False)
    currency_name = models.CharField(max_length=255, blank=False, null=False)
    currency_symbol = models.CharField(max_length=255, blank=False, null=False)
    currency_country = models.CharField(max_length=255, blank=False, null=False)
    currency_code = models.CharField(max_length=255, blank=False, null=False)
    country = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return self.businessname
    
class LocationMaster(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE, blank=False, null=False)  # Assuming you have a Business model
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=False, null=False)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    pin = models.CharField(max_length=10, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)
    country = models.CharField(max_length=100, blank=False, null=False)
    pan = models.CharField(max_length=20, blank=True, null=True)
    gstin = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)

    def __str__(self):
        return self.name
    

