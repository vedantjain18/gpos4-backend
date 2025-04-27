from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import *
from .serializers import AccountsLedgerPendingSerializer, AccountsMasterSerializer

# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')

class AccountsLedgerPendingApi(APIView):
    def get(self, request):
        stocks = AccountsLedgerPending.objects.all()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': AccountsLedgerPendingSerializer(stocks, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)

class AccountsMasterApi(APIView):
    def get(self, request):
        business_id = request.GET.get("business_id")
        # employee_master_id = request.GET.get("employee_master_id")
        stocks = AccountsMaster.objects.filter(business_id=business_id) 
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': AccountsMasterSerializer(stocks, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)