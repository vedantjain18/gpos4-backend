from django.db import models
from mastercreations.models import *
#from employeemgmt.models import *
from main.models import *
from inventorymgmt.models import *
from accounts.models import *

# Create your models here.
class PurchaseRegister(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    loc_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE)
    purchase_bill_no = models.CharField(max_length=50)
    purchase_bill_date = models.DateTimeField(auto_now_add=True)
    account_id = models.ForeignKey('AccountsMaster', on_delete=models.CASCADE)
    # purchase_entry_date_time = models.DateTimeField(auto_now_add=True)
    bill_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    other_charges = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    other_discounts = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    freight = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    net_amount = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    emp_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.purchase_bill_no

class PurchaseDetails(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    # loc_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE)
    # purchase_date_time = models.DateTimeField(auto_now_add=True)
    # purchase_bill_no = models.CharField(max_length=50)
    purchase_id = models.ForeignKey(PurchaseRegister, on_delete=models.CASCADE)
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE)
    item_barcode = models.CharField(max_length=50)
    item_child_barcode = models.CharField(max_length=50)
    item_child_purchase_rate = models.DecimalField(max_digits=10, decimal_places=2)
    item_child_mrp = models.DecimalField(max_digits=10, decimal_places=2)
    item_child_sales_qty = models.DecimalField(max_digits=10, decimal_places=2) # Should be made a 2D array for "Quantity based pricing"
    item_child_sales_rate = models.DecimalField(max_digits=10, decimal_places=2) # Should be made a 2D array for "Quantity based pricing"
    item_tax_id = models.ForeignKey(ItemTaxMaster, on_delete=models.CASCADE)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_master_id
    
class PurchasePending(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    loc_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE)
    emp_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE)
    purchase_bill_no = models.CharField(max_length=50)
    purchase_bill_date = models.DateTimeField(auto_now_add=True)
    account_id = models.ForeignKey(AccountsMaster, on_delete=models.CASCADE)
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    item_barcode = models.CharField(max_length=50)
    item_child_barcode = models.CharField(max_length=50)
    item_child_purchase_rate = models.DecimalField(max_digits=10, decimal_places=2)
    item_child_mrp = models.DecimalField(max_digits=10, decimal_places=2)
    item_child_sales_qty = models.DecimalField(max_digits=10, decimal_places=2) # Should be made a 2D array for "Quantity based pricing"
    item_child_sales_rate = models.DecimalField(max_digits=10, decimal_places=2) # Should be made a 2D array for "Quantity based pricing"
    item_tax_id = models.ForeignKey(ItemTaxMaster, on_delete=models.CASCADE)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_master_id

