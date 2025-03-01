from django.db import models
from mastercreations.models import *
from employeemgmt.models import *
from main.models import *
from mastercreations.models import *

# Create your models here.
class EmployeeMaster(models.Model):
    #group = models.ForeignKey(Group, default=None , on_delete=models.CASCADE)
    business_id = models.ForeignKey(BusinessMaster, on_delete=models.CASCADE)
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
    current_address = models.TextField(blank=False, null=False)
    spouse_name = models.CharField(max_length=100, blank=True, null=True)
    spouse_mobile_number = models.CharField(max_length=20, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=False, null=False)
    father_mobile_number = models.CharField(max_length=20, blank=False, null=False)
    mother_name = models.CharField(max_length=100, blank=False, null=False)
    mother_mobile_number = models.CharField(max_length=20, blank=False, null=False)
    # proof_of_address = models.ImageField(upload_to='proofs/', blank=False, null=False)
    # proof_of_identity = models.ImageField(upload_to='proofs/', blank=False, null=False)
    username = models.CharField(max_length=50, blank=False, null=False,unique=True)
    password = models.CharField(max_length=255, blank=False, null=False)
    bank_name = models.CharField(max_length=100)
    bank_acc_name = models.CharField(max_length=100)
    bank_acc_num = models.CharField(max_length=100)
    bank_ifsc_code = models.CharField(max_length=100)
    # objects = EmployeeMasterManager()
    locid = models.CharField(max_length=10)
    created_by = models.CharField(max_length=100) # How do i put in employee id here?
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"