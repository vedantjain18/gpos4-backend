from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json

from .models import Owner

# Create your views here.

class OwnerManageView(APIView):
    def post(self, request):
        
        replyfe = request.body.decode('utf-8')
        reply_body = json.loads(replyfe)
        print(reply_body)
        reply_body['firstname'] = reply_body['fullname'].split(' ', 1)[0]
        reply_body['lastname'] = reply_body['fullname'].split(' ', 1)[1]


        new_owner = Owner.objects.create(reply_body)
        new_owner.save()
        x = {
            'success': True,
            'status_code': 201,
            'message': 'Owner created successfully',
        }
        return Response(x, status=201)