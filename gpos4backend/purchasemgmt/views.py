from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import PurchaseRegister
from .serializers import PurchaseRegisterSerializer

# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')

class PurchaseRegisterApi(APIView):
    def get(self, request):
        purchase_register = PurchaseRegister.objects.all()
        response = {
            'success': True,
            'status_code': status.HTTP_200_OK,
            'data': PurchaseRegisterSerializer(purchase_register, many=True).data,
        }
        return Response(response, status=status.HTTP_200_OK)