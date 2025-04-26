from django.db import models
from mastercreations.models import *
# from employeemgmt.models import *
# from inventorymgmt.models import *

# Create your models here.
class ItemTaxRates(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    item_tax_symbol = models.CharField(max_length=255)
    item_tax_rate = models.DecimalField(max_digits=100, decimal_places=2, blank=False, null=False)
    about = models.CharField(max_length=355, null=True)
    isActive = models.BooleanField(default=True) # True or False
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ItemTaxMaster(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=255) #GST 5%, GST 12%, GST 18%, GST40%
    item_tax_symbol = models.CharField(max_length=255)
    about = models.CharField(max_length=355, null=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ItemTaxContainer(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=255) #5% -> 2.5 CGST + 2.5 SCGST
    item_tax_symbol = models.CharField(max_length=255)
    item_tax_rates_id = models.ForeignKey(ItemTaxRates, on_delete=models.CASCADE) # how do i make this 2D? so that it may contain multiple tax masters like CGST2.5% + SGST2.5% UNDER GST 5%
    item_tax_master_id = models.ForeignKey(ItemTaxMaster, on_delete=models.CASCADE)
    about = models.CharField(max_length=355, null=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ItemHSN(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    item_hsn = models.CharField(max_length=255)
    item_hsn_desc = models.CharField(max_length=255)
    item_hsn_type = models.CharField(max_length=255) # HSN Or SAC
    item_hsn_category = models.CharField(max_length=255) # 2 Digit / 4 Digit / 8 Digit HSN Code [0 For SAC]
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_hsn}"
    
class CentralDataNatureOfGroup(models.Model):
    # business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE,  blank=False, null=False)
    nog_name = models.CharField(max_length=100, blank=False, null=False) # Assets, Expenses, Liabilities & Income
    nog_symbol = models.CharField(max_length=100, blank=False, null=False)
    nog_operator = models.CharField(max_length=100, blank=False, null=False) # (+) or (-)
    # created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      return self.nog_name

class CentralDataAccountsGroup(models.Model):
    #business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE,  blank=False, null=False)
    acc_grp_name = models.CharField(max_length=100, blank=False, null=False) # Salary, Fixed Assets, Current Assets, Current Liabilities, Sundry Creditors, Sundry Debtors, etc
    nature_of_group_id = models.ForeignKey(CentralDataNatureOfGroup, on_delete=models.CASCADE,  blank=False, null=False)
    # created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      return self.acc_grp_name
    
class CentralDataAccountsMaster(models.Model):
    # business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False,)
    # accid = models.IntegerField(null=False, blank=False) [Will be automatically added by Django]
    acc_name = models.CharField(null=False, blank=False, max_length=120)
    accounts_group_id = models.ForeignKey(CentralDataAccountsGroup, on_delete=models.CASCADE,  blank=False, null=False)
    acc_bill_wise = models.BooleanField(null=True, blank=False)
    acc_cred_period = models.IntegerField(null=True, blank=True)
    acc_cred_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) # Set default to 0
    acc_add1 = models.CharField(max_length=220, null=True, blank=True)
    acc_add2 = models.CharField(max_length=30, null=True, blank=True)
    acc_city = models.CharField(max_length=30, null=True, blank=True)
    acc_pincode = models.IntegerField(null=True, blank=True)
    acc_gstin = models.CharField(max_length=15, null=True, blank=True)
    acc_g_loc_lat = models.DecimalField(max_digits=100, decimal_places=100, null=True, blank=True)
    acc_g_loc_lang = models.DecimalField(max_digits=100, decimal_places=100, null=True, blank=True)
    acc_mob = models.PositiveIntegerField(unique=True, null=False, blank=False)
    acc_phone = models.CharField(max_length=10, null=True, blank=True)
    acc_email = models.CharField(max_length=120, null=True, blank=True)
    acc_opp_bal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False) # Set default to 0
    # created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.acc_name)
    
class CentralDataVoucherType(models.Model):
    # business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE,  blank=False, null=False)
    location_master_id =  models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    vchr_name = models.CharField(max_length=100, blank=False, null=False) # Sales, SR, Purchase, PR, Receipt, Payment, Journal, Contra
    voucher_symbol = models.CharField(max_length=255)
    # created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE , null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      return self.vchr_name
    
class CentralDataItemTaxMaster(models.Model):
    # business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    item_tax_symbol = models.CharField(max_length=255) # like 2.5% CGST, 2.5% SGST, 6%, 14%, etc
    item_tax_rate = models.DecimalField(max_digits=100, decimal_places=2, blank=False, null=False) # like 2.5, 6, 14, etc
    about = models.CharField(max_length=355, null=True)
    # created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class CentralDataItemType(models.Model): # Refer to UQC Codes from tally screenshots & redefine this class
    # business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=255) # Pieces, Loose, Hybrid, etc
    item_type_symbol = models.CharField(max_length=255) # Like Loose (LSE), Pieces (PCS), Hybrid (HYD), etc.
    about = models.CharField(max_length=355, null=True) # Hybrid is a combination of both pieces and loose, when used, application will deduct stock from the loose (master) product only. Pieces' quantity will remain '0' thoughout.
    # created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CentralDataHSN(models.Model):
    # business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE) # [can keep it as '0']
    item_hsn = models.CharField(max_length=255, unique=True)
    item_hsn_desc = models.CharField(max_length=255)
    item_hsn_type = models.CharField(max_length=255) # HSN Or SAC
    item_hsn_category = models.CharField(max_length=255) # 2 Digit / 4 Digit / 8 Digit HSN Code [0 For SAC]
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.itemhsn

class CentralDataPincode(models.Model):
    # business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE) # [can keep it as '0']
    pincode = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pincode
    
class CentralDataCurrency(models.Model):
    # business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE, blank=False, null=False) # [can keep it as '0' for Central Data]
    currency_name = models.CharField(max_length=255, blank=False, null=False)
    currency_symbol = models.CharField(max_length=255, blank=False, null=False)
    currency_country = models.CharField(max_length=255, blank=False, null=False)
    currency_code = models.CharField(max_length=255, blank=False, null=False)
    currency_iso2_name = models.CharField(max_length=255, blank=False, null=False)
    currency_country_phone_code = models.DecimalField(max_digits=100, decimal_places=2, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.currency_code

class CentralDataIngredients(models.Model):
    # business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=500, blank=False, null=False)
    ingredient_description = models.CharField(blank=False, null=False, max_length=500)
    ingredient_is_red_dot = models.CharField(blank=False, null=False, max_length=500)
    ingredient_health_hazard_level = models.CharField(blank=False, null=False, max_length=500) # On a scale of 1-5; 5 being the worst for health
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.ingredient_name

class CentralDataLocationType(models.Model):
    # business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    location_type_name = models.CharField(max_length=255, blank=False, null=False) #Defaults -> Warehouse/Godown, SalePoint, Store, Office, Manufacturing Facility, Temporary Storage, etc
    purpose = models.CharField(max_length=750, blank=False, null=False)
    is_sale_permitted = models.BooleanField(default=False)
    is_purchase_permitted = models.BooleanField(default=False)
    is_stock_permitted = models.BooleanField(default=False)
    is_production_permitted = models.BooleanField(default=False)
    employee_limit = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)# On a scale of 1-5; 5 being the worst for health
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.location_type_name
    
class CentralDataModeOfPayment(models.Model):
    #business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE,  blank=False, null=False)
    mop_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz ModeOfPayment_id will not be serially assigned to every different business]
    mop_name = models.CharField(max_length=100, blank=False, null=False) #Cash, Credit Card, Debit Card, UPI, Cheque, Pending, etc
    mop_account_id = models.CharField(max_length=100, blank=False, null=True) #One of the MOPs should be 'round-off'. & 'Credit Notes'
    mop_commission_rate = models.DecimalField(max_digits=100, decimal_places=3, blank=False, null=True) # Commission charged by the bank/paymemnt aggregrator like 1.5%
    mop_commission_ledger = models.CharField(max_length=100, blank=False, null=True)
    # HandoverDateTime = models.DateTimeField(auto_now_add=True)
    #created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE , null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      return self.CentralDataModeOfPayment_id
    
class CentralDataSalesType(models.Model):
    #business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE, blank=False, null=False)
    sales_type_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz SalesType_id will not be serially assigned to every different business]
    sales_type_name = models.CharField(max_length=255, blank=False, null=False) #Defaults -> Counter, Delivery, Takeaway/Pickup, D2C etc
    sales_type_symbol = models.CharField(max_length=255, blank=False, null=False) #Defaults -> CTR, DLV, TAW/PCK, D2C, etc
    purpose = models.CharField(max_length=750, blank=False, null=False)

    def __str__(self):
        return self.sales_type_name
    
class CentralDataSalesReturnType(models.Model):
    #business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE, blank=False, null=False)
    sales_return_type_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz SalesReturnType_id will not be serially assigned to every different business]
    sales_return_type_name = models.CharField(max_length=255, blank=False, null=False) #Defaults -> Counter, Delivery, Takeaway/Pickup, D2C etc
    sales_return_type_symbol = models.CharField(max_length=255, blank=False, null=False) #Defaults -> CTR, DLV, TAW/PCK, D2C, etc
    purpose = models.CharField(max_length=750, blank=False, null=False)

    def __str__(self):
        return self.sales_return_type_name