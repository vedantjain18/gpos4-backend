from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import json

from .models import PurchaseInvoiceRegister, PurchaseInvoicePending, PurchaseOrderRegister, PurchaseChallanRegister, PurchaseInvoiceRegisterDetails
from mastercreations.models import *
from inventorymgmt.models import *
from accounts.models import *
from main.models import *
from .serializers import PurchaseInvoiceRegisterSerializer, PurchaseInvoicePendingSerializer, PurchaseOrderRegisterSerializer, PurchaseChallanRegisterSerializer, PurchaseInvoiceRegisterDetailsSerializer

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
    
    def post(self, request):

        pur_inv_register_data = request.body.decode('utf-8')
        pur_inv_register_data_json = json.loads(pur_inv_register_data)

        business_id = BusinessMaster.objects.get(id=pur_inv_register_data_json['businessId'])
        new_pur_inv_register = PurchaseInvoiceRegister.objects.create(
            business_id = business_id,
            purchase_invoice_register_code = pur_inv_register_data_json['purchaseInvoiceRegisterCode'],
            location_master_id = pur_inv_register_data_json['locationMasterId'],
            financial_year = pur_inv_register_data_json['financialYear'],
            purchase_invoice_no = pur_inv_register_data_json['purchaseInvoiceNo'],
            purchase_invoice_date = pur_inv_register_data_json['purchaseInvoiceDate'],
            account_master_id = pur_inv_register_data_json['accountMasterId'],
            bill_total_amount = pur_inv_register_data_json['billTotalAmount'],
            other_charges = pur_inv_register_data_json['otherCharges'],
            other_discounts = pur_inv_register_data_json['otherDiscounts'],
            freight = pur_inv_register_data_json['freight'],
            net_amount = pur_inv_register_data_json['netAmount'],
            created_by = pur_inv_register_data_json['createdBy'],
            
        )

        new_pur_inv_register.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_pur_inv_register.id,
            'message': f"Item Brand with id: {new_pur_inv_register.id} created successfully",
        }
        return Response(x, status=201)
    
class PurchaseInvoiceRegisterDetailsApi(APIView):
    def get(self, request):
        business_idx = request.GET.get("business_id")
        purchase_invoice_register_id = request.GET.get("purchase_invoice_register_id")
        # employee_master_id = request.GET.get("employee_master_id")
        # start_date = request.GET.get("from_date")
        # end_date = request.GET.get("till_date")
        result = PurchaseInvoiceRegister.objects.filter(business_id=business_idx, purchase_invoice_register_id=purchase_invoice_register_id)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': PurchaseInvoiceRegisterDetailsSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def post(self, request):
        pur_inv_register_details_data = request.body.decode('utf-8')
        pur_inv_register_details_data_json = json.loads(pur_inv_register_details_data)

        new_pur_inv_register_details = PurchaseInvoiceRegisterDetails.objects.create(
            business_id = BusinessMaster.objects.get(id=pur_inv_register_details_data_json['businessId']),
            purchase_invoice_register_id = PurchaseInvoiceRegister.objects.get(id=pur_inv_register_details_data_json['purchaseInvoiceRegisterId']),
            item_master_id = ItemMaster.objects.get(id=pur_inv_register_details_data_json['itemMasterId']),
            item_barcode = pur_inv_register_details_data_json['itemBarcode'],
            item_child_barcode = pur_inv_register_details_data_json['itemChildBarcode'],
            item_child_purchase_rate = pur_inv_register_details_data_json['itemChildPurchaseRate'],
            item_child_mrp = pur_inv_register_details_data_json['itemChildMrp'],
            item_child_sales_qty = pur_inv_register_details_data_json['itemChildSalesQty'],
            item_child_sales_rate = pur_inv_register_details_data_json['itemChildSalesRate'],
            item_tax_id = ItemTaxMaster.objects.get(id=pur_inv_register_details_data_json['itemTaxId']),
            created_by = EmployeeMaster.objects.get(id=pur_inv_register_details_data_json['createdBy']),

        )

        new_pur_inv_register_details.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_pur_inv_register_details.id,
            'message': f"Purchase Register Details with id: {new_pur_inv_register_details.id} created successfully",
        }
        return Response(x, status=201)

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
    
    def post(self, request):
        # business_idx = request.GET.get("business_id")
        # employee_master_id = request.GET.get("employee_master_id")

        pur_inv_pending_data = request.body.decode('utf-8')
        pur_inv_pending_data_json = json.loads(pur_inv_pending_data)
        
        last_barcode = ItemBarcode.objects.filter(
            business_id=pur_inv_pending_data_json['businessId'], 
            item_master_id = pur_inv_pending_data_json['itemMasterId']
        ).order_by('-created_at').first()

        last_rates = StockRegister.objects.filter(
            business_id=pur_inv_pending_data_json['businessId'], 
            item_master_id = pur_inv_pending_data_json['itemMasterId']
            ).order_by('-created_at').first()

        # new_code = 1
        # if last_location and last_location.location_master_code:
        #      new_code = last_location.location_master_code + 1

        print(last_barcode, last_rates)
        print(pur_inv_pending_data_json)
        new_pur_inv_pending = PurchaseInvoicePending.objects.create(
            business_id = BusinessMaster.objects.get(id=pur_inv_pending_data_json['businessId']),
            location_master_id= LocationMaster.objects.get(id=pur_inv_pending_data_json['locationMasterId']),
            purchase_bill_no= pur_inv_pending_data_json['purchaseBillNo'],
            purchase_bill_date= pur_inv_pending_data_json['purchaseBillDate'],
            account_id= AccountsMaster.objects.get(id=pur_inv_pending_data_json['accountId']),
            item_master_id= ItemMaster.objects.get(id=pur_inv_pending_data_json['itemMasterId']),
            item_name= pur_inv_pending_data_json['itemName'],
            item_child_sales_qty= pur_inv_pending_data_json['itemChildSalesQty'],
            item_tax_id= ItemTaxMaster.objects.get(id=pur_inv_pending_data_json['itemTaxId']),
            created_by= EmployeeMaster.objects.get(id=pur_inv_pending_data_json['createdBy']),

            #Fetch these from the itemBarcode table
            item_barcode= last_barcode.item_barcode,
            item_child_barcode= last_barcode.item_barcode,

            #will get from StockRegisterDetails (Latest value)
            item_child_sales_rate= last_rates is not None and last_rates.item_sale_rate or 0,
            item_child_mrp= last_rates is not None and last_rates.item_mrp or 0,
            item_child_purchase_rate= last_rates is not None and last_rates.item_pur_rate or 0,
        )

        new_pur_inv_pending.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': PurchaseInvoicePendingSerializer(new_pur_inv_pending).data,
            'message': f"Pur Inv Pending with id: {new_pur_inv_pending.id} created successfully",
        }
        return Response(x, status=201)
    
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