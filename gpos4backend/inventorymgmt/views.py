from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import StockRegister, PhysicalStockTakingPending, PriceTagsPrinting, ItemMaster, ItemType, ItemUnit, Company, ItemBrand, ItemCategory, ItemGroup, ItemSubGroup, OpeningStock, ItemIngredientsMaster, StockManipulationType, StockManipulation, ItemBarcode
from mastercreations.models import BusinessMaster
import json
from .serializers import StockRegisterSerializer, PhysicalStockTakingPendingSerializer, PriceTagsPrintingSerializer, ItemMasterSerializer, ItemTypeSerializer, ItemUnitSerializer, CompanySerializer, ItemBrandSerializer, ItemCategorySerializer, ItemGroupSerializer, ItemSubGroupSerializer, ItemIngredientsMasterSerializer, StockManipulationTypeSerializer, StockManipulationSerializer, ItemBarcodeSerializer, OpeningStockSerializer

# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')


class ItemMasterApi(APIView):
    def post(self, request):

        item_master_data_fe = request.body.decode('utf-8')
        item_master_data_json = json.loads(item_master_data_fe)

        business_id = BusinessMaster.objects.get(id=item_master_data_json['BusinessId'])
        new_item = ItemMaster.objects.create(
            business_id = business_id,
            item_master_code = item_master_data_json['ItemMasterCode'],
            item_name = item_master_data_json['ItemName'],
            item_print_name = item_master_data_json['ItemPrintName'],
            item_alias = item_master_data_json['ItemAlias'],
            item_unit_id = item_master_data_json['ItemUnitId'],
            item_size = item_master_data_json['ItemSize'],
            item_category_id = item_master_data_json['ItemCategoryId'],
            item_group_id = item_master_data_json['ItemGroupId'],
            item_sub_group_id = item_master_data_json['ItemSubGroupId'],
            item_tax_master_id = item_master_data_json['ItemTaxMasterId'],
            item_hsn_id = item_master_data_json['ItemHsnId'],
            item_master_product_id = item_master_data_json['ItemMasterProductId'],
            item_case_size = item_master_data_json['ItemCaseSize'],
            item_shell = item_master_data_json['ItemShell'],
            item_type_id = item_master_data_json['ItemTypeId'],
            item_desc = item_master_data_json['ItemDesc'],
            item_ingredients = item_master_data_json['ItemIngredients'],
        )

        new_item.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_item.id,
            'message': f"Item with id: {new_item.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = ItemMaster.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': ItemMasterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class ItemTypeApi(APIView):
    def post(self, request):

        item_type_data = request.body.decode('utf-8')
        item_type_data_json = json.loads(item_type_data)

        business_id = BusinessMaster.objects.get(id=item_type_data_json['BusinessId'])
        new_item_type = ItemType.objects.create(
            business_id = business_id,
            item_type_code = item_type_data_json['ItemTypeCode'],
            item_type_name = item_type_data_json['ItemTypeName'],
            item_type_uqc_code = item_type_data_json['ItemTypeUqcCode'],
            item_type_quantity_type = item_type_data_json['ItemTypeQuantityType'],
            about = item_type_data_json['AboutItemType'],
        )

        new_item_type.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_item_type.id,
            'message': f"ItemType with id: {new_item_type.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = ItemType.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': ItemTypeSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class ItemUnitApi(APIView):
    def post(self, request):

        item_unit_data = request.body.decode('utf-8')
        item_unit_data_json = json.loads(item_unit_data)

        business_id = BusinessMaster.objects.get(id=item_unit_data_json['BusinessId'])
        new_item_unit = ItemUnit.objects.create(
            business_id = business_id,
            item_unit_code = item_unit_data_json['ItemUnitCode'],
            item_unit_name = item_unit_data_json['ItemUnitName'],
            item_unit_symbol = item_unit_data_json['ItemUnitSymbol'],
            item_unit_convert_to_grams = item_unit_data_json['ItemUnitConvertToGrams'],
            item_unit_about = item_unit_data_json['ItemUnitAbout'],
        )

        new_item_unit.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_item_unit.id,
            'message': f"ItemUnit with id: {new_item_unit.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = ItemUnit.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': ItemUnitSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class CompanyApi(APIView):
    def post(self, request):

        company_data = request.body.decode('utf-8')
        company_data_json = json.loads(company_data)

        business_id = BusinessMaster.objects.get(id=company_data_json['BusinessId'])
        new_company = Company.objects.create(
            business_id = business_id,
            company_code = company_data_json['CompanyCode'],
            name = company_data_json['CompanyName'],
            about = company_data_json['CompanyAbout'],
            company_base_margin = company_data_json['CompanyBaseMargin'], #Created by insertion is pending [Will require to fetch Employee ID for that]
        )

        new_company.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_company.id,
            'message': f"Company with id: {new_company.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = Company.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': CompanySerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class ItemBrandApi(APIView):
    def post(self, request):

        item_brand_data = request.body.decode('utf-8')
        item_brand_data_json = json.loads(item_brand_data)

        business_id = BusinessMaster.objects.get(id=item_brand_data_json['BusinessId'])
        new_item_brand = ItemBrand.objects.create(
            business_id = business_id,
            item_brand_code = item_brand_data_json['ItemBrandCode'],
            name = item_brand_data_json['ItemBrandName'],
            about = item_brand_data_json['ItemBrandAbout'],
            brand_base_margin = item_brand_data_json['ItemBrandBaseMargin'],
            company_id = item_brand_data['CompanyId'] #Created by insertion is pending [Will require to fetch Employee ID for that]
        )

        new_item_brand.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_item_brand.id,
            'message': f"Item Brand with id: {new_item_brand.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = ItemBrand.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': ItemBrandSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class ItemCategoryApi(APIView):
    def post(self, request):

        item_category_data = request.body.decode('utf-8')
        item_category_data_json = json.loads(item_category_data)

        business_id = BusinessMaster.objects.get(id=item_category_data_json['BusinessId'])
        new_item_category = ItemCategory.objects.create(
            business_id = business_id,
            item_category_code = item_category_data_json['ItemCategoryCode'],
            name = item_category_data_json['ItemCategoryName'],
            about = item_category_data_json['ItemCategoryAbout'],
        )

        new_item_category.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_item_category.id,
            'message': f"Item Category with id: {new_item_category.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = ItemCategory.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': ItemCategorySerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class ItemGroupApi(APIView):
    def post(self, request):

        item_group_data = request.body.decode('utf-8')
        item_group_data_json = json.loads(item_group_data)

        business_id = BusinessMaster.objects.get(id=item_group_data_json['BusinessId'])
        new_item_group = ItemGroup.objects.create(
            business_id = business_id,
            item_group_code = item_group_data_json['ItemGroupCode'],
            name = item_group_data_json['ItemGroupName'],
            item_category_id = item_group_data_json['ItemCategoryId'],
            about = item_group_data_json['ItemGroupAbout'],
        )

        new_item_group.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_item_group.id,
            'message': f"Item Group with id: {new_item_group.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = ItemGroup.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': ItemGroupSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class ItemSubGroupApi(APIView):
    def post(self, request):

        item_sub_group_data = request.body.decode('utf-8')
        item_sub_group_data_json = json.loads(item_sub_group_data)

        business_id = BusinessMaster.objects.get(id=item_sub_group_data_json['BusinessId'])
        new_item_sub_group = ItemSubGroup.objects.create(
            business_id = business_id,
            item_sub_group_code = item_sub_group_data_json['ItemSubGroupCode'],
            name = item_sub_group_data_json['ItemSubGroupName'],
            item_group_id = item_sub_group_data_json['ItemGroupId'],
            about = item_sub_group_data_json['ItemSubGroupAbout'],
        )

        new_item_sub_group.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_item_sub_group.id,
            'message': f"Item Sub Group with id: {new_item_sub_group.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = ItemSubGroup.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': ItemSubGroupSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class OpeningStockApi(APIView):
    def post(self, request):

        opening_stock_data = request.body.decode('utf-8')
        opening_stock_data_json = json.loads(opening_stock_data)

        business_id = BusinessMaster.objects.get(id=opening_stock_data_json['BusinessId'])
        new_opening_stock = OpeningStock.objects.create(
            business_id = business_id,
            opening_stock_code = opening_stock_data_json['OpeningStockCode'],
            financial_year = opening_stock_data_json['FinancialYear'],
            loc_id = opening_stock_data_json['LocId'],
            item_master_id = opening_stock_data_json['ItemMasterId'],
            child_barcode = opening_stock_data_json['ChildBarcode'],
            item_mrp = opening_stock_data_json['ItemMrp'],
            item_pur_rate = opening_stock_data_json['ItemPurRate'],
            item_sale_rate = opening_stock_data_json['ItemSaleRate'],
            item_qty = opening_stock_data_json['ItemQty'],
        )

        new_opening_stock.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_opening_stock.id,
            'message': f"Opening Stock with id: {new_opening_stock.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = OpeningStock.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': OpeningStockSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class StockRegisterApi(APIView):
    def post(self, request):

        stock_register_data = request.body.decode('utf-8')
        stock_register_data_json = json.loads(stock_register_data)

        business_id = BusinessMaster.objects.get(id=stock_register_data_json['BusinessId'])
        new_stock_register = StockRegister.objects.create(
            business_id = business_id,
            stock_register_code = stock_register_data_json['StockRegisterCode'],
            item_master_id = stock_register_data_json['ItemMasterId'],
            item_qty = stock_register_data_json['ItemQty'],
            item_pur_rate = stock_register_data_json['ItemPurRate'],
            item_mrp = stock_register_data_json['ItemMrp'],
            item_sale_rate = stock_register_data_json['ItemSaleRate'],
            item_barcode = stock_register_data_json['ItemBarcode'],
            child_barcode = stock_register_data_json['ChildBarcode'],
            loc_id = stock_register_data_json['LocId'],
        )

        new_stock_register.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_stock_register.id,
            'message': f"Stock Register with id: {new_stock_register.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = StockRegister.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': StockRegisterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class ItemIngredientsMasterApi(APIView):
    def post(self, request):

        item_ingredients_master_data = request.body.decode('utf-8')
        item_ingredients_master_data_json = json.loads(item_ingredients_master_data)

        business_id = BusinessMaster.objects.get(id=item_ingredients_master_data_json['BusinessId'])
        new_item_ingredients_master = ItemIngredientsMaster.objects.create(
            business_id = business_id,
            item_ingredients_master_code = item_ingredients_master_data_json['ItemIngredientsMasterCode'],
            ingredient_name = item_ingredients_master_data_json['IngredientName'],
            ingredient_description = item_ingredients_master_data_json['IngredientDescription'],
            ingredient_is_red_dot = item_ingredients_master_data_json['IngredientIsRedDot'],
            ingredient_health_hazard_level = item_ingredients_master_data_json['IngredientHealthHazardLevel'],
        )

        new_item_ingredients_master.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_item_ingredients_master.id,
            'message': f"Item Ingredients Master with id: {new_item_ingredients_master.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = ItemIngredientsMaster.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': ItemIngredientsMasterSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class PhysicalStockTakingPendingApi(APIView):
    def post(self, request):

        physical_stock_taking_pending_data = request.body.decode('utf-8')
        physical_stock_taking_pending_data_json = json.loads(physical_stock_taking_pending_data)

        business_id = BusinessMaster.objects.get(id=physical_stock_taking_pending_data_json['BusinessId'])
        new_physical_stock_taking_pending = PhysicalStockTakingPending.objects.create(
            business_id = business_id,
            loc_id = physical_stock_taking_pending_data_json['LocId'],
            location_master_id = physical_stock_taking_pending_data_json['LocationMasterId'],
            item_master_id = physical_stock_taking_pending_data_json['ItemMasterId'],
            item_name = physical_stock_taking_pending_data_json['ItemName'],
            item_barcode = physical_stock_taking_pending_data_json['ItemBarcode'],
            item_child_barcode = physical_stock_taking_pending_data_json['ItemChildBarcode'],
            item_child_purchase_rate = physical_stock_taking_pending_data_json['ItemChildPurchaseRate'],
            item_child_mrp = physical_stock_taking_pending_data_json['ItemChildMrp'],
            item_child_qty = physical_stock_taking_pending_data_json['ItemChildQty'],
            item_tax_id = physical_stock_taking_pending_data_json['ItemTaxId'],

        )

        new_physical_stock_taking_pending.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_physical_stock_taking_pending.id,
            'message': f"Physical Stock Taking Pending with id: {new_physical_stock_taking_pending.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = PhysicalStockTakingPending.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': PhysicalStockTakingPendingSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class StockManipulationTypeApi(APIView):
    def post(self, request):

        stock_manipulation_type_data = request.body.decode('utf-8')
        stock_manipulation_type_data_json = json.loads(stock_manipulation_type_data)

        business_id = BusinessMaster.objects.get(id=stock_manipulation_type_data_json['BusinessId'])
        new_stock_manipulation_type = StockManipulationType.objects.create(
            business_id = business_id,
            stock_manipulation_type_code = stock_manipulation_type_data_json['StockManipulationTypeCode'],
            stock_manipulation_type_name = stock_manipulation_type_data_json['StockManipulationTypeName'],
            stock_manipulation_operator = stock_manipulation_type_data_json['StockManipulationOperator'],

        )

        new_stock_manipulation_type.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_stock_manipulation_type.id,
            'message': f"Stock Manipulation Type with id: {new_stock_manipulation_type.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = StockManipulationType.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': StockManipulationTypeSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class PriceTagsPrintingApi(APIView):
    def post(self, request):

        price_tags_printing_data = request.body.decode('utf-8')
        price_tags_printing_data_json = json.loads(price_tags_printing_data)

        business_id = BusinessMaster.objects.get(id=price_tags_printing_data_json['BusinessId'])
        new_price_tags_printing = PriceTagsPrinting.objects.create(
            business_id = business_id,
            loc_id = price_tags_printing_data_json['LocId'],
            price_tags_printing_code = price_tags_printing_data_json['PriceTagsPrintingCode'],
            location_master_id = price_tags_printing_data_json['LocationMasterId'],
            item_master_id = price_tags_printing_data_json['ItemMasterId'],
            item_barcode = price_tags_printing_data_json['ItemBarcode'],
            child_barcode = price_tags_printing_data_json['ChildBarcode'],
            item_mrp = price_tags_printing_data_json['ItemMrp'],
            item_sale_rate = price_tags_printing_data_json['ItemSaleRate'],
            item_discount_percent = price_tags_printing_data_json['ItemDiscountPercent'],
            item_discount_rate = price_tags_printing_data_json['ItemDiscountRate'],
            item_row_total = price_tags_printing_data_json['ItemRowTotal'],
            price_tag_printing_date_time = price_tags_printing_data_json['PriceTagPrintingDateTime'],

        )

        new_price_tags_printing.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_price_tags_printing.id,
            'message': f"Price Tags Printing with id: {new_price_tags_printing.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = PriceTagsPrinting.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': PriceTagsPrintingSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class ItemBarcodeApi(APIView):
    def post(self, request):

        item_barcode_data = request.body.decode('utf-8')
        item_barcode_data_json = json.loads(item_barcode_data)

        business_id = BusinessMaster.objects.get(id=item_barcode_data_json['BusinessId'])
        new_item_barcode = ItemBarcode.objects.create(
            business_id = business_id,
            item_barcode_code = item_barcode_data_json['ItemBarcodeCode'],
            item_master_id = item_barcode_data_json['ItemMasterId'],
            item_barcode = item_barcode_data_json['ItemBarcode'],

        )

        new_item_barcode.save()

        x = {
            'success': True,
            'status_code': 201,
            'data': new_item_barcode.id,
            'message': f"Item Barcode with id: {new_item_barcode.id} created successfully",
        }
        return Response(x, status=201)
    
    def get(self, request):
        business_idx = request.GET.get("business_id")
        #employee_master_id = request.GET.get("employee_master_id")
        result = ItemBarcode.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': ItemBarcodeSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class StockManipulationApi(APIView):
    def post(self, request):
        stock_manipulation_data = request.body.decode('utf-8')
        stock_manipulation_data_json = json.loads(stock_manipulation_data)

        business_id = BusinessMaster.objects.get(id=stock_manipulation_data_json['BusinessId'])
        stock_manipulation_type = StockManipulationType.objects.get(id=stock_manipulation_data_json['StockManipulationTypeId'])
        item_master = ItemMaster.objects.get(id=stock_manipulation_data_json['ItemMasterId'])

        new_stock_manipulation = StockManipulation.objects.create(
            business_id=business_id,
            stock_manipulation_code=stock_manipulation_data_json['StockManipulationCode'],
            stock_manipulation_type=stock_manipulation_type,
            item_master=item_master,
            item_qty=stock_manipulation_data_json['ItemQty'],
            item_rate=stock_manipulation_data_json['ItemRate'],
            item_total=stock_manipulation_data_json['ItemTotal'],
            loc_id=stock_manipulation_data_json['LocId'],
            remarks=stock_manipulation_data_json['Remarks'],
        )

        new_stock_manipulation.save()

        response = {
            'success': True,
            'status_code': 201,
            'data': new_stock_manipulation.id,
            'message': f"Stock Manipulation with id: {new_stock_manipulation.id} created successfully",
        }
        return Response(response, status=201)

    def get(self, request):
        business_idx = request.GET.get("business_id")
        result = StockManipulation.objects.filter(business_id=business_idx)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': StockManipulationSerializer(result, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
