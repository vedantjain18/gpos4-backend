from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import ItemMaster, SalesReturnBillPending
from .serializers import ItemMasterSerializer, SalesBillPendingSerializer, SalesReturnBillPendingSerializer
from inventorymgmt.models import StockRegister

# Create your views here.
class ItemMasterSearchByNameApi(APIView):
    def get(self, request):
        business_id = request.GET.get("business_id")
        stocks = ItemMaster.objects.filter(business_id=business_id) 
        print(business_id, stocks)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': ItemMasterSerializer(stocks, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class SalesBillPendingApi(APIView):
    def get(self, request):
        business_id = request.GET.get("business_id")
        employee_master_id = request.GET.get("employee_master_id")
        stocks = StockRegister.objects.filter(business_id=business_id) 
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': SalesBillPendingSerializer(stocks, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)

class SalesReturnBillPendingApi(APIView):
    def get(self, request):
        business_id = request.GET.get("business_id")
        employee_master_id = request.GET.get("employee_master_id")
        stocks = SalesReturnBillPending.objects.filter(business_id=business_id) 
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': SalesReturnBillPendingSerializer(stocks, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)