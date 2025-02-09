from django.db import models

# Create your models here.
class Owner(models.Model):
    firstname = models.CharField(max_length=80, blank=True, null=True)
    lastname = models.CharField(max_length=80, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    mobile = models.BigIntegerField(blank=True, null=True)
    whatsapp = models.BigIntegerField( blank=True, null=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    pin = models.BigIntegerField(blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Business(models.Model):
    Owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    businessname = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    gstin = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=10, blank=True, null=True)
    district = models.CharField(max_length=10, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.businessname
    
class EmployeeMaster(models.Model):
    #group = models.ForeignKey(Group, default=None , on_delete=models.CASCADE)
    Business_id = models.ForeignKey('Business', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)
    # age = models.PositiveIntegerField()
    date_of_birth = models.CharField(max_length=10)  # Changed to CharField
    gender = models.CharField(max_length=1)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    current_address = models.TextField(blank=True, null=True)
    spouse_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    father_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    mother_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    # proof_of_address = models.ImageField(upload_to='proofs/', blank=True, null=True)
    # proof_of_identity = models.ImageField(upload_to='proofs/', blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True,unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    bank_name = models.CharField(max_length=100)
    bank_acc_name = models.CharField(max_length=100)
    bank_acc_num = models.CharField(max_length=100)
    bank_ifsc_code = models.CharField(max_length=100)
    # objects = EmployeeMasterManager()
    locid = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
