from django.db import models
from mastercreations.models import *
from employeemgmt.models import *
# from inventorymgmt.models import *
from mastercreations.models import *

# Create your models here.
class Company(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    about = models.CharField(max_length=355, null=True)
    base_margin_company = models.DecimalField(blank=False, null=False, decimal_places=3, default=0)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ItemBrand(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    about = models.CharField(max_length=355, null=True)
    base_margin_brand = models.DecimalField(blank=False, null=False, decimal_places=3, default=0)
    company_id=models.ForeignKey(Company, on_delete=models.CASCADE)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ItemCategory(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    about = models.CharField(max_length=355, null=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ItemGroup(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    item_category_id = models.ForeignKey(ItemCategory, on_delete=models.CASCADE) # how do i make this 2D? so that i can accommodate multiple itemGroups inside a single itemCategory
    about = models.CharField(max_length=355, null=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ItemSubGroup(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    item_group_id = models.ForeignKey(ItemGroup, on_delete=models.CASCADE) # how do i make this 2D? 
    about = models.CharField(max_length=355, null=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ItemTaxMaster(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    item_tax_symbol = models.CharField(max_length=255)
    item_tax_rate = models.CharField(max_length=255)
    about = models.CharField(max_length=355, null=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ItemTaxContainer(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    item_tax_symbol = models.CharField(max_length=255)
    item_tax_master_id = models.ForeignKey(ItemTaxMaster, on_delete=models.CASCADE) # how do i make this 2D? so that it may contain multiple tax masters like CGST2.5% + SGST2.5% UNDER GST 5%
    about = models.CharField(max_length=355, null=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ItemHSN(models.Model):
    item_hsn = models.CharField(max_length=255)
    item_hsn_desc = models.CharField(max_length=255)
    item_hsn_type = models.CharField(max_length=255) # HSN Or SAC
    item_hsn_category = models.CharField(max_length=255) # 2 Digit / 4 Digit / 8 Digit HSN Code [0 For SAC]
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.itemhsn}"
    
class ItemType(models.Model): # Refer to UQC Codes from tally screenshots & redefine this class
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    item_type_symbol = models.CharField(max_length=255) # Like Loose (LSE), Pieces (PCS), Hybrid (HYD), etc.
    about = models.CharField(max_length=355, null=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ItemUnit(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    item_unit_symbol = models.CharField(max_length=255)
    item_unit_convert_to_grams = models.CharField(max_length=255)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE,  blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CentralDataHSN(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE) # [can keep it as '0']
    item_hsn = models.CharField(max_length=255, unique=True)
    item_hsn_desc = models.CharField(max_length=255)
    item_hsn_type = models.CharField(max_length=255) # HSN Or SAC
    item_hsn_category = models.CharField(max_length=255) # 2 Digit / 4 Digit / 8 Digit HSN Code [0 For SAC]
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.itemhsn

class CentralDataPincode(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE) # [can keep it as '0']
    pincode = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pincode
    
class CentralDataCurrency(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE, blank=False, null=False) # [can keep it as '0' for Central Data]
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
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=500, blank=False, null=False)
    ingredient_description = models.CharField(blank=False, null=False, max_length=500)
    ingredient_is_red_dot = models.CharField(blank=False, null=False, max_length=500)
    ingredient_health_hazard_level = models.CharField(blank=False, null=False, max_length=500) # On a scale of 1-5; 5 being the worst for health
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.ingredient_name

