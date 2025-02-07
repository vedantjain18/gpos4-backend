from django.db import models

# Create your models here.
class StockRegister(models.Model):
    Business_id = models.CharField(max_length=5)
    # osid = models.CharField(blank=True, null=True, max_length=10)
    itemname = models.CharField(max_length=255)
    itemid = models.BigIntegerField(blank=True, null=True,)
    itemqty = models.IntegerField(blank=True, null=False, default=0)  # Set default value to 0
    itempurrate = models.DecimalField(blank=True, null=False, max_digits=10, decimal_places=2, default=0)  # Set default value to 0
    itemmrp = models.DecimalField(blank=True, null=False, max_digits=10, decimal_places=2, default=0)  # Set default value to 0
    itemsalerate = models.DecimalField(blank=True, null=False, max_digits=10, decimal_places=2, default=0)  # Set default value to 0
    itembarcode = models.BigIntegerField(blank=True, null=True,)  # Set default value to 0
    childbarcode = models.BigIntegerField(blank=True, null=True,)
    locid = models.CharField(blank=True, null=True, max_length=10)

    def __str__(self):
        return self.itemname
    
