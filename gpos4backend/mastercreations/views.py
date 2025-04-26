from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import json

from .models import OwnerMaster, BusinessMaster, LocationMaster, EmployeeMaster, LocationType
from .serializers import OwnerMasterSerializer, BusinessMasterSerializer, LocationMasterSerializer, EmployeeMasterSerializer, LocationTypeSerializer

# Create your views here.

class OwnerMasterApi(APIView):
    def post(self, request):
        
        owner_data_fe = request.body.decode('utf-8')
        owner_data_json = json.loads(owner_data_fe)
        owner_data_json['firstname'] = owner_data_json['fullname'].split(' ', 1)[0]
        owner_data_json['lastname'] = owner_data_json['fullname'].split(' ', 1)[1]

        new_owner = OwnerMaster.objects.create(
            firstname = owner_data_json['firstname'],
            lastname = owner_data_json['lastname'],
            username = owner_data_json['username'],
            password = owner_data_json['password'],
            email = owner_data_json['email'],
            mobile = owner_data_json['mobile'],
            whatsapp = owner_data_json['whatsapp'],
            address1 = owner_data_json['address1'],
            address2 = owner_data_json['address2'],
            city = owner_data_json['city'],
            pin = owner_data_json['pincode'],
            district = owner_data_json['district'],
            state = owner_data_json['state'],
            country = owner_data_json['country'],
        )

        new_owner.save()

        print(new_owner)
        
        x = {
            'success': True,
            'status_code': 201,
            'data': new_owner.id,
            'message': f"Owner with id: {new_owner.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        #business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = OwnerMaster.objects.filter()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': OwnerMasterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    


class BusniessMasterViewApi(APIView):
    def post(self, request):

        business_data_fe = request.body.decode('utf-8')
        business_data_json = json.loads(business_data_fe)

        owner_id = OwnerMaster.objects.get(id=business_data_json['OwnerId'])

        last_business = BusinessMaster.objects.filter(owner_id=owner_id).order_by('-created_at').first()
    
        new_code = 1
        if last_business and last_business.business_master_code:
             new_code = last_business.business_master_code + 1
    
        new_business = BusinessMaster.objects.create(
            owner_id = owner_id,
            business_master_code = new_code,
            business_name = business_data_json['BusinessName'],
            email =  business_data_json['BusinessEmail'],
            mobile =  business_data_json['BusinessMobile'],
            whatsapp =  business_data_json['BusinessWhatsapp'],
            address1 =  business_data_json['BusinessAddress1'],
            address2 =  business_data_json['BusinessAddress2'],
            gstin =  business_data_json['Gstin'],
            city =  business_data_json['City'],
            pin =  business_data_json['Pincode'],
            district =  business_data_json['District'],
            state =  business_data_json['State'],
            currency_name =  'Rupee',
            currency_symbol =  'R',
            currency_country =  'India',
            currency_code =  'RPP',
            country =  business_data_json['Country']
        )
        # new_business.business_master_code = new_business.get_business_master_code()
        print("new_business", new_business)
        # print(new_business.business_master_code)
        new_business.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_business.id,
            'message': f"Business with id: {new_business.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        #business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = BusinessMaster.objects.filter()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': BusinessMasterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class LocationTypeApi(APIView):
    def post(self, request, **kwargs):
        # location_type_data_fe = request.body.decode('utf-8')
        location_type_data_json = kwargs['selectedLocationType']
        print("location_type_data_json", location_type_data_json)

        business_id = BusinessMaster.objects.get(id=kwargs['business_id'])

        last_location = LocationType.objects.filter(business_id=business_id).order_by('-created_at').first()

        new_code = 1
        if last_location and last_location.location_type_code:
             new_code = last_location.location_type_code + 1

        new_location_type = LocationType.objects.create(
            business_id = business_id,
            location_type_code = new_code,
            location_type_name = location_type_data_json['location_type_name'],
            purpose = location_type_data_json['purpose'],
            is_sale_permitted = location_type_data_json['is_sale_permitted'],
            is_purchase_permitted = location_type_data_json['is_purchase_permitted'],
            is_stock_permitted = location_type_data_json['is_stock_permitted'],
            is_production_permitted = location_type_data_json['is_production_permitted'],
            employee_limit = location_type_data_json['employee_limit'],
            is_active = location_type_data_json['is_active'],
            # created_by = business_id,
        )

        new_location_type.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_location_type,
            'id': new_location_type.id,
            'message': f"Location Type with id: {new_location_type.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = LocationType.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': LocationTypeSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class LocationMasterApi(APIView):
    def post(self, request):
        location_data_fe = request.body.decode('utf-8')
        location_data_json = json.loads(location_data_fe)

        location_type_response = LocationTypeApi.post(self, request, selectedLocationType=location_data_json['selectedLocationType'], business_id=location_data_json['BusinessId'])
        print("location_type_response", location_type_response.data)
        
        business_id = BusinessMaster.objects.get(id=location_data_json['BusinessId'])
        print("business_id", business_id)
        
        last_location = LocationMaster.objects.filter(business_id=business_id).order_by('-created_at').first()

        new_code = 1
        if last_location and last_location.location_master_code:
             new_code = last_location.location_master_code + 1

        
        new_location = LocationMaster.objects.create(
            business_id = business_id,
            location_master_code = new_code,
            name = location_data_json['LocationName'],
            location_type_id = location_type_response.data["data"],
            email = location_data_json['LocationEmail'],
            phone = location_data_json['LocationMobile'],
            whatsapp = location_data_json['LocationWhatsapp'],
            address = location_data_json['LocationAddress1'],
            city = location_data_json['City'],
            pin = location_data_json['Pincode'],
            district = location_data_json['District'],
            state = location_data_json['State'],
            country = location_data_json['Country'],
            pan = location_data_json['Pan'],
            gstin = location_data_json['Gstin'],
        )

        new_location.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_location.id,
            'message': f"Location with id: {new_location.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = LocationMaster.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': LocationMasterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class EmployeeMasterApi(APIView):
    def post(self, request):
        employee_data_fe = request.body.decode('utf-8')
        employee_data_json = json.loads(employee_data_fe)

        business_id = BusinessMaster.objects.get(id=employee_data_json['BusinessId'])
        new_employee = EmployeeMaster.objects.create(
            business_id=business_id,
            employee_master_code = employee_data_json['EmployeeMasterCode'],
            first_name=employee_data_json['FirstName'],
            middle_name=employee_data_json['MiddleName'],
            last_name=employee_data_json['LastName'],
            mobile=employee_data_json['Mobile'],
            whatsapp=employee_data_json['Whatsapp'],
            email=employee_data_json['Email'],
            date_of_birth=employee_data_json['DateOfBirth'],
            gender = employee_data_json['Gender'],
            address=employee_data_json['Address'],
            city=employee_data_json['City'],
            pin=employee_data_json['Pincode'],
            current_address=employee_data_json['CurrentAddress'],
            spouse_name=employee_data_json['SpouseName'],
            spouse_mobile_number=employee_data_json['SpouseMobileNumber'],
            father_name=employee_data_json['FatherName'],
            father_mobile_number=employee_data_json['FatherMobileNumber'],
            mother_name=employee_data_json['MotherName'],
            mother_mobile_number=employee_data_json['MotherMobileNumber'],
            username=employee_data_json['Username'],
            password=employee_data_json['Password'],
            bank_name=employee_data_json['BankName'],
            bank_acc_name=employee_data_json['BankAccName'],
            bank_acc_num=employee_data_json['BankAccNum'],
            bank_ifsc_code=employee_data_json['BankIfscCode'],
            location_master_id=employee_data_json['LocationMasterId'],
            created_by=employee_data_json['CreatedBy']
        )

        new_employee.save()

        response = {
            'success': True,
            'status_code': 201,
            'data': new_employee.id,
            'message': f"Employee with id: {new_employee.id} created successfully",
        }
        return Response(response, status=201)

    def get(self, request):
        business_idx = request.GET.get("business_id")
        result = EmployeeMaster.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': EmployeeMasterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)