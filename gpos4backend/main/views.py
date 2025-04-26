from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import ItemTaxMaster, ItemTaxContainer, ItemHSN, CentralDataHSN, CentralDataPincode, CentralDataCurrency, CentralDataIngredients, CentralDataLocationType, CentralDataNatureOfGroup, CentralDataAccountsGroup, CentralDataAccountsMaster, CentralDataVoucherType, CentralDataItemType
from mastercreations.models import BusinessMaster
from .serializers import CentralDataLocationTypeSerializer, ItemTaxMasterSerializer, ItemTaxContainerSerializer, ItemHSNSerializer, CentralDataHSNSerializer, CentralDataPincodeSerializer, CentralDataCurrencySerializer, CentralDataIngredientsSerializer, CentralDataNatureOfGroupSerializer, CentralDataAccountsGroupSerializer, CentralDataAccountsMasterSerializer, CentralDataVoucherTypeSerializer, CentralDataItemTypeSerializer
import json

class CentralDataLocationTypeView(APIView):
    def get(self, request):
        result = CentralDataLocationType.objects.filter()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': CentralDataLocationTypeSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request):
        location_type_data = request.data
        location_type_created = CentralDataLocationType.objects.create(**location_type_data)
        location_type_created.save()
        # [1, 2, 3] -> 1, 2, 3

        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': location_type_created.location_type_name
        }
        return Response(response, status=status.HTTP_200_OK)
    
class ItemTaxMasterApi(APIView):
    def post(self, request):
        item_tax_master_data_fe = request.body.decode('utf-8')
        item_tax_master_data_json = json.loads(item_tax_master_data_fe)

        business_id = BusinessMaster.objects.get(id=item_tax_master_data_json['BusinessId'])
        new_item_tax_master = ItemTaxMaster.objects.create(
            business_id = business_id,
            name = item_tax_master_data_json['ItemTaxMasterName'],
            item_tax_symbol = item_tax_master_data_json['ItemTaxMasterSymbol'],
            item_tax_rate = item_tax_master_data_json['ItemTaxMasterRate'],
            about = item_tax_master_data_json['ItemTaxMasterAbout'],
            is_active = item_tax_master_data_json['IsActive'],
        )

        new_item_tax_master.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_item_tax_master.id,
            'message': f"Item Tax Master with id: {new_item_tax_master.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = ItemTaxMaster.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': ItemTaxMasterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class ItemTaxContainerApi(APIView):
    def post(self, request):
        item_tax_container_data_fe = request.body.decode('utf-8')
        item_tax_container_data_json = json.loads(item_tax_container_data_fe)

        business_id = BusinessMaster.objects.get(id=item_tax_container_data_json['BusinessId'])
        item_tax_master_id = ItemTaxMaster.objects.get(id=item_tax_container_data_json['ItemTaxMasterId'])

        new_item_tax_container = ItemTaxContainer.objects.create(
            business_id = business_id,
            item_tax_master_id = item_tax_master_id,
            name = item_tax_container_data_json['ItemTaxContainerName'],
            item_tax_container_symbol = item_tax_container_data_json['ItemTaxContainerSymbol'],
            about = item_tax_container_data_json['ItemTaxContainerAbout'],
        )

        new_item_tax_container.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_item_tax_container.id,
            'message': f"Item Tax Container with id: {new_item_tax_container.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = ItemTaxContainer.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': ItemTaxContainerSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
        
class ItemHSNApi(APIView):
    def post(self, request):
        item_hsn_data_fe = request.body.decode('utf-8')
        item_hsn_data_json = json.loads(item_hsn_data_fe)

        business_id = BusinessMaster.objects.get(id=item_hsn_data_json['BusinessId'])

        new_item_hsn = ItemHSN.objects.create(
            business_id = business_id,
            item_hsn = item_hsn_data_json['ItemHSNCode'],
            item_hsn_desc = item_hsn_data_json['ItemHSNDescription'],
            item_hsn_type = item_hsn_data_json['ItemHSNType'],
            item_hsn_category = item_hsn_data_json['ItemHSNCategory'],
        )

        new_item_hsn.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_item_hsn.id,
            'message': f"Item HSN with id: {new_item_hsn.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = ItemHSN.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': ItemHSNSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)

class CentralDataNatureOfGroupApi(APIView):
    def post(self, request):
        nature_of_group_data_fe = request.body.decode('utf-8')
        nature_of_group_data_json = json.loads(nature_of_group_data_fe)

        new_nature_of_group = CentralDataNatureOfGroup.objects.create(
            nog_name = nature_of_group_data_json['NatureOfGroupName'],
            nog_symbol = nature_of_group_data_json['NatureOfGroupSymbol'],
            nog_operator = nature_of_group_data_json['NatureOfGroupOperator'],
        )

        new_nature_of_group.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_nature_of_group.id,
            'message': f"Central Data Nature Of Group with id: {new_nature_of_group.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        result = CentralDataNatureOfGroup.objects.filter()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': CentralDataNatureOfGroupSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class CentralDataAccountsGroupApi(APIView):
    def post(self, request):
        accounts_group_data_fe = request.body.decode('utf-8')
        accounts_group_data_json = json.loads(accounts_group_data_fe)

        nog_id = CentralDataNatureOfGroup.objects.get(id=accounts_group_data_json['NatureOfGroupId'])

        new_accounts_group = CentralDataAccountsGroup.objects.create(
            nog_id = nog_id,
            acc_grp_name = accounts_group_data_json['AccountsGroupName'],
        )

        new_accounts_group.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_accounts_group.id,
            'message': f"Central Data Accounts Group with id: {new_accounts_group.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        result = CentralDataAccountsGroup.objects.filter()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': CentralDataAccountsGroupSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)

class CentralDataAccountsMasterApi(APIView):
    def post(self, request):
        accounts_master_data_fe = request.body.decode('utf-8')
        accounts_master_data_json = json.loads(accounts_master_data_fe)

        acc_grp_id = CentralDataAccountsGroup.objects.get(id=accounts_master_data_json['CentralDataAccountsGroupId'])

        new_accounts_master = CentralDataAccountsMaster.objects.create(
            acc_grp_id = acc_grp_id,
            acc_name = accounts_master_data_json['AccountsMasterName'],
            acc_bill_wise = accounts_master_data_json['AccountsMasterBillWise'],
            acc_cred_period = accounts_master_data_json['AccountsMasterCreditPeriod'],
            acc_cred_limit = accounts_master_data_json['AccountsMasterCreditLimit'],
            acc_add1 = accounts_master_data_json['AccountsMasterAddress1'],
            acc_add2 = accounts_master_data_json['AccountsMasterAddress2'],
            acc_city = accounts_master_data_json['AccountsMasterCity'],
            acc_pincode = accounts_master_data_json['AccountsMasterPincode'],
            acc_gstin = accounts_master_data_json['AccountsMasterGSTIN'],
            acc_g_loc_lat = accounts_master_data_json['AccountsMasterLocationLatitude'],
            acc_g_loc_long = accounts_master_data_json['AccountsMasterLocationLongitude'],
            acc_mob = accounts_master_data_json['AccountsMasterMobile'],
            acc_phone = accounts_master_data_json['AccountsMasterPhone'],
            acc_email = accounts_master_data_json['AccountsMasterEmail'],
            acc_opp_bal = accounts_master_data_json['AccountsMasterOpeningBalance'],
            
        )

        new_accounts_master.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_accounts_master.id,
            'message': f"Central Data Accounts Master with id: {new_accounts_master.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        result = CentralDataAccountsMaster.objects.filter()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': CentralDataAccountsMasterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)

class CentralDataVoucherTypeApi(APIView):
    def post(self, request):
        voucher_type_data_fe = request.body.decode('utf-8')
        voucher_type_data_json = json.loads(voucher_type_data_fe)

        new_voucher_type = CentralDataVoucherType.objects.create(
            location_master_id = voucher_type_data_json['LocationMasterId'],
            vchr_name = voucher_type_data_json['VoucherTypeName'],
            voucher_symbol = voucher_type_data_json['VoucherTypeSymbol'],
        )

        new_voucher_type.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_voucher_type.id,
            'message': f"Central Data Voucher Type with id: {new_voucher_type.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        result = CentralDataVoucherType.objects.filter()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': CentralDataVoucherTypeSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class CentralDataItemTaxMasterApi(APIView):
    def post(self, request):
        item_tax_master_data_fe = request.body.decode('utf-8')
        item_tax_master_data_json = json.loads(item_tax_master_data_fe)

        new_item_tax_master = CentralDataItemType.objects.create(
            name = item_tax_master_data_json['ItemTaxMasterName'],
            item_tax_symbol = item_tax_master_data_json['ItemTaxMasterSymbol'],
            item_tax_rate = item_tax_master_data_json['ItemTaxMasterRate'],
            about = item_tax_master_data_json['ItemTaxMasterAbout'],
        )

        new_item_tax_master.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_item_tax_master.id,
            'message': f"Central Data Item Tax Master with id: {new_item_tax_master.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        result = CentralDataItemType.objects.filter()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': CentralDataItemTypeSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class CentralDataItemTypeApi(APIView):
    def post(self, request):
        item_type_data_fe = request.body.decode('utf-8')
        item_type_data_json = json.loads(item_type_data_fe)

        new_item_type = CentralDataItemType.objects.create(
            name = item_type_data_json['ItemTypeName'],
            item_type_symbol = item_type_data_json['ItemTypeSymbol'],
            about = item_type_data_json['ItemTypeAbout'],
        )

        new_item_type.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_item_type.id,
            'message': f"Central Data Item Type with id: {new_item_type.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        result = CentralDataItemType.objects.filter()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': CentralDataItemTypeSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class CentralDataHSNApi(APIView):
    def post(self, request):
        hsn_data_fe = request.body.decode('utf-8')
        hsn_data_json = json.loads(hsn_data_fe)

        new_hsn = CentralDataHSN.objects.create(
            item_hsn = hsn_data_json['HSNCode'],
            item_hsn_desc = hsn_data_json['HSNDescription'],
            item_hsn_type = hsn_data_json['HSNType'],
            item_hsn_category = hsn_data_json['HSNCategory'],
        )

        new_hsn.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_hsn.id,
            'message': f"Central Data HSN with id: {new_hsn.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        result = CentralDataHSN.objects.filter()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': CentralDataHSNSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)