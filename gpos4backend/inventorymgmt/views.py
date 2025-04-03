from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import StockRegister, PhysicalStockTakingPending, PriceTagsPrinting
from .serializers import StockRegisterSerializer, PhysicalStockTakingPendingSerializer, PriceTagsPrintingSerializer

# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')

class StockRegisterAllApi(APIView):
    def get(self, request):
        business_id = request.GET.get("business_id")
        stocks = StockRegister.objects.filter(business_id=business_id) 
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': StockRegisterSerializer(stocks, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)


class PhysicalStockTakingPendingApi(APIView):
    def get(self, request):
        business_id = request.GET.get("business_id")
        stocks = PhysicalStockTakingPending.objects.filter(business_id=business_id)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': PhysicalStockTakingPendingSerializer(stocks, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)
    
class PriceTagsPrintingApi(APIView):
    def get(self, request):
        business_id = request.GET.get("business_id")
        stocks = PriceTagsPrinting.objects.filter(business_id=business_id)
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': PriceTagsPrintingSerializer(stocks, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)