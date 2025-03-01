from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json

from .models import OwnerMaster

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
        
        x = {
            'success': True,
            'status_code': 201,
            'message': 'Owner created successfully',
        }
        return Response(x, status=201)