from django.db import models
from mastercreations.models import *
# from employeemgmt.models import *
from main.models import *

# Create your models here.

class ItemType(models.Model): # Refer to UQC Codes from tally screenshots & redefine this class
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    item_type_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz ItemType_id will not be serially assigned to every different business]
    name = models.CharField(max_length=255)
    item_type_uqc_code = models.CharField(max_length=255) # Like Loose (LSE), Pieces (PCS), Hybrid (HYD), etc.
    item_type_quantity_type = models.CharField(max_length=255) # Like Weight, Volume, Count, etc.
    about = models.CharField(max_length=355, null=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ItemUnit(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    item_unit_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz ItemUnit_id will not be serially assigned to every different business]
    name = models.CharField(max_length=255)
    item_unit_symbol = models.CharField(max_length=255)
    item_unit_convert_to_grams = models.CharField(max_length=255)
    about = models.CharField(max_length=355, null=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    company_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz Company_id will not be serially assigned to every different business]
    name = models.CharField(max_length=255)
    about = models.CharField(max_length=355, null=True)
    company_base_margin = models.DecimalField(max_digits=10, blank=False, null=False, decimal_places=3, default=0)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ItemBrand(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    item_brand_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz ItemBrand_id will not be serially assigned to every different business]
    name = models.CharField(max_length=255)
    about = models.CharField(max_length=355, null=True)
    item_brand_base_margin = models.DecimalField(max_digits=10, blank=False, null=False, decimal_places=3, default=0)
    company_id=models.ForeignKey(Company, on_delete=models.CASCADE)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ItemCategory(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    item_category_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz ItemCategory_id will not be serially assigned to every different business]
    name = models.CharField(max_length=255)
    about = models.CharField(max_length=355, null=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ItemGroup(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    item_group_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz ItemGroup_id will not be serially assigned to every different business]
    name = models.CharField(max_length=255)
    item_category_id = models.ForeignKey(ItemCategory, on_delete=models.CASCADE) # how do i make this 2D? so that i can accommodate multiple itemGroups inside a single itemCategory
    about = models.CharField(max_length=355, null=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ItemSubGroup(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    item_sub_group_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz ItemSubGroup_id will not be serially assigned to every different business]
    name = models.CharField(max_length=255)
    item_group_id = models.ForeignKey(ItemGroup, on_delete=models.CASCADE) # how do i make this 2D? 
    about = models.CharField(max_length=355, null=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class ItemMaster(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    item_master_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz ItemMaster_id will not be serially assigned to every different business]
    # itemid = models.BigIntegerField(primary_key=True)
    item_name = models.CharField(max_length=255)
    item_print_name = models.CharField(max_length=255)
    item_alias = models.CharField(max_length=255)
    item_unit_id = models.ForeignKey(ItemUnit, on_delete=models.CASCADE)
    item_size = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2, default=0)
    item_category_id = models.ForeignKey(ItemCategory, on_delete=models.CASCADE) # Make it 2D, in order for it to be visible in multiple Categories
    item_group_id = models.ForeignKey(ItemGroup, on_delete=models.CASCADE)
    # item_group2_id = models.ManyToManyField(ItemGroup, on_delete=models.CASCADE) # Make it 2D, in order for it to be visible in multiple Categories
    item_sub_group_id = models.ForeignKey(ItemSubGroup, on_delete=models.CASCADE) # Make it 2D, in order for it to be visible in multiple Categories
    item_tax_master_id =models.ForeignKey(ItemTaxMaster, on_delete=models.CASCADE)
    item_hsn_id = models.ForeignKey(ItemHSN, on_delete=models.CASCADE)
    # itemmrp = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    item_master_product_code = models.CharField(max_length=50, blank=True, null=True) #Enter master product code
    item_case_size = models.CharField(max_length=50, blank=True, null=True)
    item_shell = models.CharField(max_length=50, blank=True, null=True)
    item_type_id = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    item_desc = models.TextField(blank=True, null=True)
    #item_images = models.ImageField(max_length=50, blank=True, null=True) # Change to ImageField & to 2D array to store multiple images
    item_ingredients = models.CharField(max_length=50, blank=True, null=True) #make this 2d to store multiple ingredients
    created_at = models.DateTimeField(auto_now_add=True)
    # itembarcode1 = models.CharField(max_length=50, blank=True, null=True)
    # itembarcode2 = models.CharField(max_length=50, blank=True, null=True)
    # itembarcode3 = models.CharField(max_length=50,blank=True, null=True)
    # itembrand = models.ForeignKey(Brand,on_delete=models.CASCADE,blank=True, null=True,)
    # itemcompany = models.ForeignKey(Company,on_delete=models.CASCADE,blank=True, null=True)
    # Attributes= models.ForeignKey(Attribute,on_delete=models.CASCADE,blank=True, null=True)
    # Attributes_options= models.ForeignKey(Attribute_options,on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.item_name

class StockRegister(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    stock_register_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz StockRegister_id will not be serially assigned to every different business]
    # osid = models.CharField(blank=False, null=False, max_length=10)
    # itemname = models.CharField(max_length=255)
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE, blank=False, null=False)
    item_qty = models.IntegerField(blank=False, null=False, default=0)  # Set default value to 0
    item_pur_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2, default=0)  # Set default value to 0
    item_mrp = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2, default=0)  # Set default value to 0
    item_sale_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2, default=0)  # Set default value to 0
    item_barcode = models.BigIntegerField(blank=False, null=False,)  # Set default value to 0
    child_barcode = models.BigIntegerField(blank=False, null=False,)
    loc_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.item_id
    
class OpeningStock(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    opening_stock_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz OpeningStock_id will not be serially assigned to every different business]
    financial_year = models.CharField(blank=False, null=False, max_length=10)
    loc_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE, blank=False, null=False)
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE, blank=False, null=False)
    child_barcode = models.CharField(blank=False, null=False, max_length=50)
    item_mrp = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_pur_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_sale_rate = models.DecimalField(blank=False, null=False, max_digits=10, decimal_places=2)
    item_qty = models.IntegerField(blank=False, null=False)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.itemname
    
class ItemIngredientsMaster(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    item_ingredients_master_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz ItemIngredientsMaster_id will not be serially assigned to every different business]
    ingredient_name = models.CharField(blank=False, null=False, max_length=500)
    ingredient_description = models.CharField(blank=False, null=False, max_length=500)
    ingredient_is_red_dot = models.CharField(blank=False, null=False, max_length=500)
    ingredient_health_hazard_level = models.CharField(blank=False, null=False, max_length=500) # On a scale of 1-5; 5 being the worst for health
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.ingredient_name
    
class PhysicalStockTakingPending(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE)
    # employee_master_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, related_name='pstp_employee_master_id')
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    item_barcode = models.CharField(max_length=50)
    item_child_barcode = models.CharField(max_length=50)
    item_child_purchase_rate = models.DecimalField(max_digits=10, decimal_places=2)
    item_child_mrp = models.DecimalField(max_digits=10, decimal_places=2)
    item_child_qty = models.DecimalField(max_digits=10, decimal_places=2)
    item_tax_id = models.ForeignKey(ItemTaxMaster, on_delete=models.CASCADE)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True) # no separate register for this, all updation will take place inside StockRegister & StockManipulation (under manipulation id = 'stock adjustment' or physical stock taking)

    def __str__(self):
        return self.item_name
    
class StockManipulationType(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    stock_manipulation_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz StockManipulationType_id will not be serially assigned to every different business]
    stock_manipulation_type = models.CharField(max_length=255) #Production, Consumption, Damage, Spoilage, Stock Adjustment, e, Stock Transfer, Stock Conversion, Stock Correction, Stock Write Off, Stock Write On, Theft
    stock_manipulation_operator = models.CharField(max_length=100, blank=False, null=False) # (+1) or (-1)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stock_manipulation_type
    
class StockManipulation(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    stock_manipulation_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz StockManipulation_id will not be serially assigned to every different business]
    loc_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE)
    stock_manipulation_type_id = models.ForeignKey(StockManipulationType, on_delete=models.CASCADE)
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE)
    item_barcode = models.CharField(max_length=50)
    child_barcode = models.CharField(max_length=50)
    item_mrp = models.DecimalField(max_digits=10, decimal_places=2)
    item_pur_rate = models.DecimalField(max_digits=10, decimal_places=2)
    item_sale_rate = models.DecimalField(max_digits=10, decimal_places=2)
    item_qty = models.IntegerField()
    item_gst = models.IntegerField()
    stock_manipulation_comments = models.TextField()
    # item_row_total = models.DecimalField(max_digits=10, decimal_places=2)
    # employee_master_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE)
    stock_manipulation_date_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.child_barcode
    
class PriceTagsPrinting(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    price_tags_printing_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz PriceTagsPrinting_id will not be serially assigned to every different business]
    location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE)
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE)
    item_barcode = models.CharField(max_length=50)
    child_barcode = models.CharField(max_length=50)
    item_mrp = models.DecimalField(max_digits=10, decimal_places=2)
    # item_pur_rate = models.DecimalField(max_digits=10, decimal_places=2)
    item_sale_rate = models.DecimalField(max_digits=10, decimal_places=2)
    item_discount_percent = models.DecimalField(max_digits=10, decimal_places=2) # Percentage discount
    item_discount_rate = models.DecimalField(max_digits=10, decimal_places=2) # MRP - Sale Rate
    # item_qty = models.IntegerField()
    # item_gst = models.IntegerField()
    item_row_total = models.DecimalField(max_digits=10, decimal_places=2)
    #employee_master_id = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE)
    price_tag_printing_date_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.child_barcode
    
class ItemBarcode(models.Model):
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    item_barcode_code = models.IntegerField(blank=False, null=False) # 1,2,3,4 [Coz ItemBarcode_id will not be serially assigned to every different business]
    item_master_id = models.ForeignKey(ItemMaster, on_delete=models.CASCADE, unique=False)
    item_barcode = models.CharField(max_length=255, unique=True)
    created_by = models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE, blank=False, null=False) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_barcode