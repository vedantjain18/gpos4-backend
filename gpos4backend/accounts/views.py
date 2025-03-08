from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import AccountsLedgerPending
from .serializers import AccountsLedgerPendingSerializer

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
