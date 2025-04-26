from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import SalesBillPending, SalesReturnBillPending, SalesOrderPending, SalesQuotationPending, SalesReturnRegister, SalesOrderRegister, SalesQuotationRegister, SalesRegister, SalesRegisterDetails, SalesReturnRegisterDetails
from .serializers import ItemMasterSerializer, SalesBillPendingSerializer, SalesReturnBillPendingSerializer, SalesRegisterSerializer, SalesOrderPendingSerializer, SalesQuotationPendingSerializer, SalesReturnRegisterSerializer, CashHandoverSerializer, SalesOrderRegisterSerializer, SalesQuotationRegisterSerializer, ItemBarcodeSerializer
from inventorymgmt.models import ItemMaster, ItemBarcode
from accounts.models import CashHandover

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

class ItemMasterSearchByBarcodeApi(APIView):
    def get(self, request):
        business_idx = request.GET.get("business_id")
        item_barcodex = request.GET.get("item_barcode") #Here, first check whether item_barcode is entered or item_child_barcode (we can use startswith() which is a python function) is entered which starts with CB [Or perform this check in the frontend and create a separate fucntion for child_item_barcode]
        result = ItemBarcode.objects.filter(business_id=business_idx, item_barcode=item_barcodex) 
        print(business_idx, result) #Here, from result, extract all child_barcodes & return their respective stock qtys & rates; if nil, return 'item out of stock'
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': ItemBarcodeSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    

class SalesBillPendingApi(APIView):
    def get(self, request):
        business_id = request.GET.get("business_id")
        employee_master_id = request.GET.get("employee_master_id")
        stocks = SalesBillPending.objects.filter(business_id=business_id, employee_master_id=employee_master_id) 
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
        stocks = SalesReturnBillPending.objects.filter(business_id=business_id, employee_master_id=employee_master_id) 
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': SalesReturnBillPendingSerializer(stocks, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class SalesRegisterApi(APIView):
    def get(self, request):
        business_idx = request.GET.get("business_id")
        # employee_master_id = request.GET.get("employee_master_id")
        start_date = request.GET.get("from_date")
        end_date = request.GET.get("till_date")
        result = SalesRegister.objects.filter(business_id=business_idx, sale_date_time__gte=start_date, sale_date_time__lte=end_date)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': SalesRegisterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class SalesRegisterDetailsApi(APIView):
    def get(self, request):
        business_idx = request.GET.get("business_id")
        sales_register_id = request.GET.get("sales_register_id")
        # employee_master_id = request.GET.get("employee_master_id")
        start_date = request.GET.get("from_date")
        end_date = request.GET.get("till_date")
        result = SalesRegisterDetails.objects.filter(business_id=business_idx, sales_register_id=sales_register_id, sale_date_time__gte=start_date, sale_date_time__lte=end_date)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': SalesRegisterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class SalesReturnRegisterApi(APIView):
    def get(self, request):
        business_idx = request.GET.get("business_id")
        # employee_master_id = request.GET.get("employee_master_id")
        start_date = request.GET.get("from_date")
        end_date = request.GET.get("till_date")
        result = SalesReturnRegister.objects.filter(business_id=business_idx, sale_date_time__gte=start_date, sale_date_time__lte=end_date)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': SalesReturnRegisterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class SalesOrderPendingApi(APIView):
    def get(self, request):
        business_id = request.GET.get("business_id")
        employee_master_id = request.GET.get("employee_master_id")
        stocks = SalesOrderPending.objects.filter(business_id=business_id, employee_master_id=employee_master_id) 
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': SalesOrderPendingSerializer(stocks, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class SalesOrderRegisterApi(APIView):
    def get(self, request):
        business_idx = request.GET.get("business_id")
        # employee_master_id = request.GET.get("employee_master_id")
        start_date = request.GET.get("from_date")
        end_date = request.GET.get("till_date")
        result = SalesOrderRegister.objects.filter(business_id=business_idx, sale_date_time__gte=start_date, sale_date_time__lte=end_date)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': SalesOrderRegisterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class SalesQuotationPendingApi(APIView):
    def get(self, request):
        business_id = request.GET.get("business_id")
        employee_master_id = request.GET.get("employee_master_id")
        stocks = SalesQuotationPending.objects.filter(business_id=business_id, employee_master_id=employee_master_id) 
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': SalesQuotationPendingSerializer(stocks, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class SalesQuotationRegisterApi(APIView):
    def get(self, request):
        business_idx = request.GET.get("business_id")
        # employee_master_id = request.GET.get("employee_master_id")
        start_date = request.GET.get("from_date")
        end_date = request.GET.get("till_date")
        result = SalesQuotationRegister.objects.filter(business_id=business_idx, sale_date_time__gte=start_date, sale_date_time__lte=end_date)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': SalesQuotationRegisterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class CashHandoverRegisterApi(APIView):
    def get(self, request):
        business_idx = request.GET.get("business_id")
        # employee_master_id = request.GET.get("employee_master_id")
        start_date = request.GET.get("from_date")
        end_date = request.GET.get("till_date")
        result = CashHandover.objects.filter(business_id=business_idx, sale_date_time__gte=start_date, sale_date_time__lte=end_date)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': CashHandoverSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)