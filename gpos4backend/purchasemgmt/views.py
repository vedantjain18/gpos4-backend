from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import PurchaseInvoiceRegister, PurchaseInvoicePending, PurchaseOrderRegister, PurchaseChallanRegister
from .serializers import PurchaseInvoiceRegisterSerializer, PurchaseInvoicePendingSerializer, PurchaseOrderRegisterSerializer, PurchaseChallanRegisterSerializer

# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')

class PurchaseInvoiceRegisterApi(APIView):
    def get(self, request):
        business_idx = request.GET.get("business_id")
        # employee_master_id = request.GET.get("employee_master_id")
        start_date = request.GET.get("from_date")
        end_date = request.GET.get("till_date")
        result = PurchaseInvoiceRegister.objects.filter(business_id=business_idx, purchase_invoice_date__gte=start_date, purchase_invoice_date__lte=end_date)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': PurchaseInvoiceRegisterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)

class PurchaseInvoicePendingApi(APIView):
    def get(self, request):
        business_idx = request.GET.get("business_id")
        employee_master_id = request.GET.get("employee_master_id")
        result = PurchaseInvoicePending.objects.filter(business_id=business_idx, employee_master_id=employee_master_id) 
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': PurchaseInvoicePendingSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class PurchaseOrderRegisterApi(APIView):
    def get(self, request):
        business_idx = request.GET.get("business_id")
        # employee_master_id = request.GET.get("employee_master_id")
        start_date = request.GET.get("from_date")
        end_date = request.GET.get("till_date")
        result = PurchaseOrderRegister.objects.filter(business_id=business_idx, purchase_invoice_date__gte=start_date, purchase_invoice_date__lte=end_date)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': PurchaseOrderRegisterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class PurchaseChallanRegisterApi(APIView):
    def get(self, request):
        business_idx = request.GET.get("business_id")
        # employee_master_id = request.GET.get("employee_master_id")
        start_date = request.GET.get("from_date")
        end_date = request.GET.get("till_date")
        result = PurchaseChallanRegister.objects.filter(business_id=business_idx, purchase_invoice_date__gte=start_date, purchase_invoice_date__lte=end_date)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': PurchaseChallanRegisterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)