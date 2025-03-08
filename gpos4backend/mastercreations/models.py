from django.db import models

# Create your models here.
class OwnerMaster(models.Model):
    firstname = models.CharField(max_length=80, blank=False, null=False)
    lastname = models.CharField(max_length=80, blank=False, null=False)
    username = models.CharField(max_length=50, blank=False, null=False, unique=True)
    password = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    mobile = models.BigIntegerField(blank=False, null=False)
    whatsapp = models.BigIntegerField(blank=True, null=True)
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
    business_name = models.CharField(max_length=15, blank=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    mobile = models.CharField(max_length=15, blank=False, null=False)
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
    
class EmployeeMaster(models.Model):
    #group = models.ForeignKey(Group, default=None , on_delete=models.CASCADE)
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    # age = models.PositiveIntegerField()
    date_of_birth = models.CharField(max_length=10)  # Changed to CharField
    gender = models.CharField(max_length=1)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    current_address = models.TextField(blank=False, null=False)
    spouse_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    father_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    mother_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    # proof_of_address = models.ImageField(upload_to='proofs/', blank=False, null=False)
    # proof_of_identity = models.ImageField(upload_to='proofs/', blank=False, null=False)
    username = models.CharField(max_length=50, blank=False, null=False,unique=True)
    password = models.CharField(max_length=255, blank=False, null=False)
    bank_name = models.CharField(max_length=100)
    bank_acc_name = models.CharField(max_length=100)
    bank_acc_num = models.CharField(max_length=100)
    bank_ifsc_code = models.CharField(max_length=100)
    # objects = EmployeeMasterManager()
    location_master_id = models.ForeignKey(LocationMaster, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=100) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"