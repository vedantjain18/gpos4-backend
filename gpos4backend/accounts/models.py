from django.db import models
from mastercreations.models import *
# from employeemgmt.models import *
from main.models import *

# Create your models here.

class NatureOfGroup(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE,  blank=False, null=False)
    nog_name = models.CharField(max_length=100, blank=False, null=False) # Assets, Expenses, Liabilities & Income
    nog_symbol = models.CharField(max_length=100, blank=False, null=False)
    nog_operator = models.CharField(max_length=100, blank=False, null=False) # (+) or (-)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      return self.nog_name

class AccountsGroup(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE,  blank=False, null=False)
    acc_grp_name = models.CharField(max_length=100, blank=False, null=False) # Assets, Expenses, Liabilities & Income
    nature_of_group_id = models.ForeignKey(NatureOfGroup, on_delete=models.CASCADE,  blank=False, null=False)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      return self.acc_grp_name
    
class AccountsMaster(models.Model):
    business_id = models.ForeignKey(BusinessMaster,on_delete=models.CASCADE,blank=False, null=False,)
    # accid = models.IntegerField(null=False, blank=False) [Will be automatically added by Django]
    acc_name = models.CharField(null=False, blank=False, max_length=120)
    accounts_group_id = models.ForeignKey(AccountsGroup, on_delete=models.CASCADE,  blank=False, null=False)
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
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.acc_name)
    
class VoucherType(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE,  blank=False, null=False)
    loc_id =  models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    vchr_name = models.CharField(max_length=100, blank=False, null=False) # Sales, SR, Purchase, PR, Receipt, Payment, Journal, Contra
    voucher_symbol = models.CharField(max_length=255)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE , null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      return self.vchr_name
    
class AccountsVoucherEntry(models.Model):
    business_id= models.ForeignKey(BusinessMaster, on_delete=models.CASCADE,  blank=False, null=False)
    loc_id =  models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    vchr_number = models.CharField(max_length=100,  blank=True, null=True) # only put numbers here. voucher type will be determined by VoucherType_id
    voucher_type_id = models.ForeignKey(VoucherType, on_delete=models.CASCADE , null=False, blank=False)
    vchr_entry_date = models.DateField(max_length=100,  blank=False, null=False)
    vchr_entry_time = models.TimeField(max_length=100,  blank=False, null=False)
    vchr_narration = models.CharField(max_length=100,  blank=True, null=True)
    from_acc_id = models.ForeignKey(AccountsMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in AccountsMaster_id here?
    to_acc_id = models.ForeignKey(AccountsMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in AccountsMaster_id here?
    crd_amt = models.IntegerField( blank=False, null=False)
    dbt_amt = models.IntegerField( blank=False, null=False) # this & fromaccid, toaccid & crdamt should be made a 2d array (for multiple entries)
    # balance = models.IntegerField( blank=True, null=True) # Will not be required as it can be calculated from crdamt & dbtamt
    vchr_ref = models.CharField(max_length=100, blank=True, null=True)
    # vchtype = models.ForeignKey('Vouchertype', on_delete=models.CASCADE,  blank=False, null=False)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE , null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return str(self.vchrnumber)

class CashHandover(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE,  blank=False, null=False)
    handover_date_time = models.DateTimeField(auto_now_add=True)
    emp_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE , null=False, blank=False) # separate from created_by coz, a manager might do an entry of cash hanndover on behalf of an employee
    loc_id =  models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False)
    N1 = models.DecimalField(max_digits=100, decimal_places=2, blank=False)
    N2 = models.DecimalField(max_digits=100, decimal_places=2, blank=False)
    N5 = models.DecimalField(max_digits=100, decimal_places=2, blank=False)
    N10 = models.DecimalField(max_digits=100, decimal_places=2, blank=False)
    N20 = models.DecimalField(max_digits=100, decimal_places=2, blank=False)
    N50 = models.DecimalField(max_digits=100, decimal_places=2, blank=False)
    N100 = models.DecimalField(max_digits=100, decimal_places=2, blank=False)
    N200 = models.DecimalField(max_digits=100, decimal_places=2, blank=False)
    N500 = models.DecimalField(max_digits=100, decimal_places=2, blank=False)
    N2000 = models.DecimalField(max_digits=100, decimal_places=2, blank=False)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE , null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      return self.CashHandover_id
    
class ModeOfPayment(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE,  blank=False, null=False)
    mop_name = models.CharField(max_length=100, blank=False, null=False)
    mop_acc_id = models.ForeignKey(AccountsMaster, on_delete=models.CASCADE,  blank=False, null=False)
    mop_commission_rate = models.DecimalField(max_digits=100, decimal_places=2, blank=False, null=False) # Commission charged by the bank/paymemnt aggregrator like 1.5%
    mop_commission_ledger = models.ForeignKey(AccountsMaster, on_delete=models.CASCADE,  blank=False, null=False)
    # HandoverDateTime = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE , null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
      return self.ModeOfPayment_id

class AccountsLedgerPending(models.Model):
    business_id= models.ForeignKey(BusinessMaster, on_delete=models.CASCADE,  blank=False, null=False)
    # locid =  models.ForeignKey('location', on_delete=models.CASCADE,  blank=False, null=False)
    vchr_entry_date_time = models.DateField(max_length=100,  blank=False, null=False)
    voucher_name_number = models.CharField(max_length=100, blank=False, null=False)
    loc_id_name =  models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False) # insert location name + locid in this
    # vchrentrytime = models.TimeField(max_length=100,  blank=False, null=False)
    acc_id_name = models.CharField(max_length=100, blank=False, null=False)
    vchr_ref = models.CharField(max_length=100,  blank=True, null=True)
    vchr_narration = models.CharField(max_length=100,  blank=True, null=True)
    crd_amt = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=10)
    dbt_amt = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=10) # 
    balance = models.IntegerField(blank=True, null=True) # Will not be required as it can be calculated from crdamt & dbtamt
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE , null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return str(self.AccountsVoucherEntry_id)
    
class OpeningAccounts(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    financial_year = models.CharField(blank=False, null=False, max_length=10)
    # locid = models.ForeignKey(LocationMaster, on_delete=models.CASCADE,  blank=False, null=False) # 0 if the location is invalid
    accounts_master_id = models.ForeignKey(AccountsMaster, on_delete=models.CASCADE,  blank=False, null=False)
    opening_balance = models.DecimalField(max_digits=100, decimal_places=2, blank=False, null=False, max_length=50)
    comments = models.CharField(blank=False, null=False)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.itemname