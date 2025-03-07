from django.db import models
from mastercreations.models import *
#from employeemgmt.models import *
from main.models import *
from inventorymgmt.models import *
from accounts.models import *
from customermgmt.models import *

# Create your models here.
class SalesBillPending(models.Model):
    business = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    loc_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    item_master = models.ForeignKey(ItemMaster, on_delete=models.CASCADE,  blank=False, null=False) #discuss on_delete. data will be deleted from this table everytime a bill is saved. should we use foreign key? and if yes, should we remove the on_delete condition?
    item_barcode = models.CharField(blank=False, null=False, max_length=50)
    child_barcode = models.CharField(blank=False, null=False, max_length=50)
    item_name = models.CharField(blank=False, null=False, max_length=255)
    item_mrp = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_pur_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_sale_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_qty = models.IntegerField(blank=False, null=False)
    item_gst = models.IntegerField(blank=False, null=False)
    item_gst2 = models.IntegerField(blank=False, null=False)
    item_row_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    employee_master = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=True) # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    #created_by = models.CharField(blank=False, null=False, max_length=50) # Have not used foreign key becase after every bill entry, it'll be required to delete this specific entry using empid
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.child_barcode
    
class SalesReturnBillPending(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    loc_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    sales_bill_number = models.CharField(blank=False, null=False, max_length=50)
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE,  blank=False, null=False) #discuss on_delete. data will be deleted from this table everytime a bill is saved. should we use foreign key? and if yes, should we remove the on_delete condition?
    item_barcode = models.CharField(blank=False, null=False, max_length=50)
    child_barcode = models.CharField(blank=False, null=False, max_length=50)
    item_name = models.CharField(blank=False, null=False, max_length=255)
    item_mrp = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_pur_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_sale_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_qty = models.IntegerField(blank=False, null=False)
    item_gst = models.IntegerField(blank=False, null=False)
    item_row_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    employee_master = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=True)
    created_by = models.CharField(blank=False, null=False, max_length=50) # Have not used foreign key becase after every bill entry, it'll be required to delete this specific entry using empid
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.child_barcode
    
class SalesRegister(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    loc_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    bill_num = models.CharField(blank=False, null=False, max_length=50)
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE,  blank=False, null=False)
    item_barcode = models.CharField(blank=False, null=False, max_length=50)
    child_barcode = models.CharField(blank=False, null=False, max_length=50)
    # item_name = models.CharField(blank=False, null=False, max_length=255)
    item_mrp = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_pur_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_sale_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_qty = models.IntegerField(blank=False, null=False)
    item_gst_rate = models.IntegerField(blank=False, null=False)
    item_row_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2) # keeping this for now for fast calculations & to insert under 'payment modes'
    sale_date_time = models.DateTimeField(auto_now_add=True) # sale_date_time & created_at both are required in case of date changed bill creation
    #employee_master_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.child_barcode
    
class SalesTransactionDetails(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    loc_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    bill_num = models.CharField(blank=False, null=False, max_length=50)
    financial_year = models.CharField(blank=False, null=False, max_length=50)
    cust_id = models.ForeignKey(CustomerMaster, on_delete=models.CASCADE,  blank=False, null=False)
    sale_date_time = models.DateTimeField(auto_now_add=True) # sale_date_time & created_at both are required in case of date changed bill creation
    bill_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2) # keeping this for now for fast calculations & to insert under 'payment modes'
    other_charges = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    other_discounts = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    mop_id = models.ForeignKey(ModeOfPayment, on_delete=models.CASCADE,  blank=False, null=False) # Need to make a 2d array to store multiple payment modes
    mop_acc_id = models.ForeignKey(AccountsMaster, on_delete=models.CASCADE,  blank=False, null=False) # Need to make a ForeignKey(ModeOfPayment, on_delete=models.CASCADE,  blank=False, null=False)
    mop_id_amount = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    #employee_master_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, related_name='std_employee_master_id') # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, related_name='std_created_by') # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.child_barcode
    
class SalesReturnRegister(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    loc_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    bill_num = models.CharField(blank=False, null=False, max_length=50)
    ret_bill_num = models.CharField(blank=False, null=False, max_length=50)
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE,  blank=False, null=False)
    item_barcode = models.CharField(blank=False, null=False, max_length=50)
    child_barcode = models.CharField(blank=False, null=False, max_length=50)
    # item_name = models.CharField(blank=False, null=False, max_length=255)
    item_mrp = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_pur_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_sale_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_qty = models.IntegerField(blank=False, null=False)
    item_gst_rate = models.IntegerField(blank=False, null=False)
    item_row_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2) # keeping this for now for fast calculations & to insert under 'payment modes'
    sale_ret_date_time = models.DateTimeField(auto_now_add=True) # sale_date_time & created_at both are required in case of date changed bill creation
    #employee_master_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.child_barcode
    
class SalesReturnsTransactionDetails(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    loc_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    ret_bill_num = models.CharField(blank=False, null=False, max_length=50)
    cust_id = models.ForeignKey(CustomerMaster, on_delete=models.CASCADE,  blank=False, null=False)
    sale_ret_date_time = models.DateTimeField(auto_now_add=True) # sale_date_time & created_at both are required in case of date changed bill creation
    total_amount = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    mop_id = models.ForeignKey(ModeOfPayment, on_delete=models.CASCADE,  blank=False, null=False) # Need to make a 2d array to store multiple payment modes
    mop_acc_id = models.ForeignKey(AccountsMaster, on_delete=models.CASCADE,  blank=False, null=False) # Need to make a 2d array to store multiple payment modes' account id
    #employee_master_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.child_barcode
    
