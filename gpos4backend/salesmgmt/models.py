from django.db import models
from mastercreations.models import *
#from employeemgmt.models import *
from main.models import *
from inventorymgmt.models import *
from accounts.models import *
from customermgmt.models import *

# Create your models here.
class SalesBillPending(models.Model):
    business = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE, blank=False, null=False)
    location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE, blank=False, null=False)
    item_master = models.ForeignKey(ItemMaster, on_delete=models.CASCADE, blank=False, null=False) #discuss on_delete. data will be deleted from this table everytime a bill is saved. should we use foreign key? and if yes, should we remove the on_delete condition?
    item_barcode = models.CharField(blank=False, null=False, max_length=50)
    item_child_barcode = models.CharField(blank=False, null=False, max_length=50)
    item_name = models.CharField(blank=False, null=False, max_length=255)
    item_mrp = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_pur_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_sale_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_qty = models.IntegerField(blank=False, null=False)
    item_gst = models.IntegerField(blank=False, null=False)
    #item_gst2 = models.IntegerField(blank=False, null=False)
    item_row_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    employee_master = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=True) # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    #created_by = models.CharField(blank=False, null=False, max_length=50) # Have not used foreign key becase after every bill entry, it'll be required to delete this specific entry using empid
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_child_barcode
    
class SalesReturnBillPending(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    sales_bill_number = models.CharField(blank=False, null=False, max_length=50)
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE,  blank=False, null=False) #discuss on_delete. data will be deleted from this table everytime a bill is saved. should we use foreign key? and if yes, should we remove the on_delete condition?
    item_barcode = models.CharField(blank=False, null=False, max_length=50)
    item_child_barcode = models.CharField(blank=False, null=False, max_length=50)
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
        return self.item_child_barcode
    
class SalesRegister(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    sales_register_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz SalesRegister_id will not be serially assigned to every different business]
    location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    financial_year = models.CharField(blank=False, null=False, max_length=50)
    bill_num = models.CharField(blank=False, null=False, max_length=50, unique=True)
    customer_master_id = models.ForeignKey(CustomerMaster, on_delete=models.CASCADE,  blank=False, null=False)
    sale_date_time = models.DateTimeField(auto_now_add=True) # sale_date_time & created_at both are required in case of date changed bill creation
    bill_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2) # keeping this for now for fast calculations & to insert under 'payment modes'
    other_charges = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    other_discounts = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    #employee_master_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, related_name='std_employee_master_id') # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    comments = models.TextField(blank=True, null=True) # In case of any comments from the customer
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bill_num
    
class SalesRegisterDetails(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    sales_register_id = models.ForeignKey(SalesRegister, on_delete=models.CASCADE,  blank=False, null=False)
    # location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    # financial_year = models.CharField(blank=False, null=False, max_length=50)
    # bill_num = models.CharField(blank=False, null=False, max_length=50)
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE,  blank=False, null=False)
    item_barcode = models.CharField(blank=False, null=False, max_length=50)
    item_child_barcode = models.CharField(blank=False, null=False, max_length=50)
    # item_name = models.CharField(blank=False, null=False, max_length=255)
    item_mrp = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_pur_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_sale_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_qty = models.IntegerField(blank=False, null=False)
    item_gst_rate = models.IntegerField(blank=False, null=False)
    item_row_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2) # keeping this for now for fast calculations & to insert under 'payment modes'
    # sale_date_time = models.DateTimeField(auto_now_add=True) # sale_date_time & created_at both are required in case of date changed bill creation
    #employee_master_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_child_barcode
    
class SalesRegisterMOP(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    sales_register_id = models.ForeignKey(SalesRegister, on_delete=models.CASCADE,  blank=False, null=False)
    # location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False) #May be excluded, but keeping it will ease reporting like location wise mop or year wise mop trends
    # financial_year = models.CharField(blank=False, null=False, max_length=50) #May be excluded, but keeping it will ease reporting like location wise mop or year wise mop trends
    # bill_num = models.CharField(blank=False, null=False, max_length=50, unique=True)
    # total_amount = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    mop_id = models.ForeignKey(ModeOfPayment, on_delete=models.CASCADE,  blank=False, null=False) #One of the MOPs should be 'round-off' (Mandatory Field for every bill_num)
    mop_account_id = models.ForeignKey(AccountsMaster, on_delete=models.CASCADE,  blank=False, null=False) # This will be pulled via mop_id, but in case of credit bills, we need to input the respective customer's accounts_master_id
    mop_id_amount = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    mop_amount_reference_no = models.CharField(blank=False, null=True, max_length=50) # In Case of Credit Card/UPI etc
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bill_num
    
class SalesReturnRegister(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    sales_return_register_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz SalesReturnRegister_id will not be serially assigned to every different business]
    location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    financial_year = models.CharField(blank=False, null=False, max_length=50)
    bill_num = models.CharField(blank=False, null=True, max_length=50) #May be null, if in case the employee doesn't want to mention the bill number
    return_bill_num = models.CharField(blank=False, null=False, max_length=50)
    customer_master_id = models.ForeignKey(CustomerMaster, on_delete=models.CASCADE,  blank=False, null=False)
    sale_return_date_time = models.DateTimeField(auto_now_add=True) # sale_date_time & created_at both are required in case of date changed bill creation
    total_amount = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    mop_id = models.ForeignKey(ModeOfPayment, on_delete=models.CASCADE,  blank=False, null=False) # Need to make a 2d array to store multiple payment modes
    mop_acc_id = models.ForeignKey(AccountsMaster, on_delete=models.CASCADE,  blank=False, null=False) # Need to make a 2d array to store multiple payment modes' account id
    comments = models.TextField(blank=True, null=True) # In case of any comments from the customer
    #employee_master_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.return_bill_num
    
class SalesReturnRegisterDetails(models.Model): #Terms of return slip issue:return slip should be used in one single bill only. (or Cannot be used in multiple bills)
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    sales_return_register_id = models.ForeignKey(SalesReturnRegister, on_delete=models.CASCADE,  blank=False, null=False)
    # location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    # ret_bill_num = models.CharField(blank=False, null=False, max_length=50)
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE,  blank=False, null=False)
    item_barcode = models.CharField(blank=False, null=False, max_length=50)
    item_child_barcode = models.CharField(blank=False, null=False, max_length=50)
    # item_name = models.CharField(blank=False, null=False, max_length=255)
    item_mrp = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_pur_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_sale_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_qty = models.IntegerField(blank=False, null=False)
    item_gst_rate = models.IntegerField(blank=False, null=False)
    item_row_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2) # keeping this for now for fast calculations & to insert under 'payment modes'
    # sale_return_date_time = models.DateTimeField(auto_now_add=True) # sale_date_time & created_at both are required in case of date changed bill creation
    #employee_master_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_child_barcode
    
class SalesReturnRegisterMOP(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    sales_return_register_id = models.ForeignKey(SalesReturnRegister, on_delete=models.CASCADE,  blank=False, null=False)
    #location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False) #May be excluded, but keeping it will ease reporting like location wise mop or year wise mop trends
    #financial_year = models.CharField(blank=False, null=False, max_length=50) #May be excluded, but keeping it will ease reporting like location wise mop or year wise mop trends
    #return_bill_num = models.CharField(blank=False, null=False, max_length=50, unique=True)
    # total_amount = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    mop_id = models.ForeignKey(ModeOfPayment, on_delete=models.CASCADE,  blank=False, null=False) #One of the MOPs should be 'round-off' (Mandatory Field for every bill_num)
    mop_account_id = models.ForeignKey(AccountsMaster, on_delete=models.CASCADE,  blank=False, null=False) # This will be pulled via mop_id, but in case of credit bills, we need to input the respective customer's accounts_master_id
    mop_id_amount = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    mop_amount_reference_no = models.CharField(blank=False, null=True, max_length=50)
    is_redeemed = models.BooleanField(default=False)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bill_num

class SalesOrderPending(models.Model):
    business = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE, blank=False, null=False)
    location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE, blank=False, null=False)
    item_master = models.ForeignKey(ItemMaster, on_delete=models.CASCADE, blank=False, null=False) #discuss on_delete. data will be deleted from this table everytime a bill is saved. should we use foreign key? and if yes, should we remove the on_delete condition?
    item_barcode = models.CharField(blank=False, null=False, max_length=50)
    item_child_barcode = models.CharField(blank=False, null=False, max_length=50)
    item_name = models.CharField(blank=False, null=False, max_length=255)
    item_mrp = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_pur_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_sale_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_qty = models.IntegerField(blank=False, null=False)
    item_gst = models.IntegerField(blank=False, null=False)
    #item_gst2 = models.IntegerField(blank=False, null=False)
    item_row_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    employee_master = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=True) # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    #created_by = models.CharField(blank=False, null=False, max_length=50) # Have not used foreign key becase after every bill entry, it'll be required to delete this specific entry using empid
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_child_barcode
    
class SalesOrderRegister(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    sales_order_register_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz SalesOrderRegister_id will not be serially assigned to every different business]
    location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    financial_year = models.CharField(blank=False, null=False, max_length=50)
    order_num = models.CharField(blank=False, null=False, max_length=50, unique=True)
    customer_master_id = models.ForeignKey(CustomerMaster, on_delete=models.CASCADE,  blank=False, null=False)
    order_date_time = models.DateTimeField(auto_now_add=True) # sale_date_time & created_at both are required in case of date changed bill creation
    order_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2) # keeping this for now for fast calculations & to insert under 'payment modes'
    other_charges = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    other_discounts = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    comments = models.TextField(blank=True, null=True) # In case of any comments from the customer
    #employee_master_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, related_name='std_employee_master_id') # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_num
    
class SalesOrderRegisterDetails(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    sales_order_register_id = models.ForeignKey(SalesOrderRegister, on_delete=models.CASCADE,  blank=False, null=False)
    #location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    #financial_year = models.CharField(blank=False, null=False, max_length=50)
    #order_num = models.CharField(blank=False, null=False, max_length=50)
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE,  blank=False, null=False)
    item_barcode = models.CharField(blank=False, null=False, max_length=50)
    item_child_barcode = models.CharField(blank=False, null=False, max_length=50)
    # item_name = models.CharField(blank=False, null=False, max_length=255)
    item_mrp = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_pur_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_sale_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_qty = models.IntegerField(blank=False, null=False)
    item_gst_rate = models.IntegerField(blank=False, null=False)
    item_row_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2) # keeping this for now for fast calculations & to insert under 'payment modes'
    #order_date_time = models.DateTimeField(auto_now_add=True) # sale_date_time & created_at both are required in case of date changed bill creation
    #employee_master_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_child_barcode
    
class SalesQuotationPending(models.Model):
    business = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE, blank=False, null=False)
    location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE, blank=False, null=False)
    item_master = models.ForeignKey(ItemMaster, on_delete=models.CASCADE, blank=False, null=False) #discuss on_delete. data will be deleted from this table everytime a bill is saved. should we use foreign key? and if yes, should we remove the on_delete condition?
    item_barcode = models.CharField(blank=False, null=False, max_length=50)
    item_child_barcode = models.CharField(blank=False, null=False, max_length=50)
    item_name = models.CharField(blank=False, null=False, max_length=255)
    item_mrp = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_pur_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_sale_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_qty = models.IntegerField(blank=False, null=False)
    item_gst = models.IntegerField(blank=False, null=False)
    #item_gst2 = models.IntegerField(blank=False, null=False)
    item_row_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    employee_master = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=True) # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    #created_by = models.CharField(blank=False, null=False, max_length=50) # Have not used foreign key becase after every bill entry, it'll be required to delete this specific entry using empid
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_child_barcode

class SalesQuotationRegister(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    sales_quotation_register_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz SalesQuotationRegister_id will not be serially assigned to every different business]
    location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    financial_year = models.CharField(blank=False, null=False, max_length=50)
    quotation_num = models.CharField(blank=False, null=False, max_length=50, unique=True)
    customer_master_id = models.ForeignKey(CustomerMaster, on_delete=models.CASCADE,  blank=False, null=False)
    quotation_date_time = models.DateTimeField(auto_now_add=True) # sale_date_time & created_at both are required in case of date changed bill creation
    quotation_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2) # keeping this for now for fast calculations & to insert under 'payment modes'
    other_charges = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    other_discounts = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    #employee_master_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, related_name='std_employee_master_id') # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quotation_num
    
class SalesQuotationRegisterDetails(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False)
    sales_quotation_register_id = models.ForeignKey(SalesQuotationRegister, on_delete=models.CASCADE,  blank=False, null=False)
    # location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    # financial_year = models.CharField(blank=False, null=False, max_length=50)
    # quotation_num = models.CharField(blank=False, null=False, max_length=50)
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE, blank=False, null=False)
    item_barcode = models.CharField(blank=False, null=False, max_length=50)
    item_child_barcode = models.CharField(blank=False, null=False, max_length=50)
    # item_name = models.CharField(blank=False, null=False, max_length=255)
    item_mrp = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_pur_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_sale_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_qty = models.IntegerField(blank=False, null=False)
    item_gst_rate = models.IntegerField(blank=False, null=False)
    item_row_total = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2) # keeping this for now for fast calculations & to insert under 'payment modes'
    # quotation_date_time = models.DateTimeField(auto_now_add=True) # sale_date_time & created_at both are required in case of date changed bill creation
    #employee_master_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # emp_id and created_by both are required in case the manager is creating a bill on behalf of an eployee
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_child_barcode
    
