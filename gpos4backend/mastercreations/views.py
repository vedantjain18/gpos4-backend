from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json

from .models import OwnerMaster, BusinessMaster

# Create your views here.

class OwnerManageView(APIView):
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
    
class BusniessCreateViewApi(APIView):
    def post(self, request):

        business_data_fe = request.body.decode('utf-8')
        business_data_json = json.loads(business_data_fe)

        owner = OwnerMaster.objects.get(id=business_data_json['OwnerId'])
        new_business = BusinessMaster.objects.create(
            owner_id = owner,
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

        new_business.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_business.id,
            'message': f"Business with id: {new_business.id} created successfully",
        }
        return Response(x, status=201)