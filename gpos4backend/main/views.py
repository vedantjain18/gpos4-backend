from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import CentralDataLocationType
from .serializers import CentralDataLocationTypeSerializer

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