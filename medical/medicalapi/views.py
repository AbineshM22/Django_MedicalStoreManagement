from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework import filters

from rest_framework import generics


from .serializers import MedicineSerializer
from projectapp1.models import Medicalstore
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from rest_framework.response import Response
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def simpleapi(request):
    return Response({'text': 'Hello world, This is your first api call'},status=HTTP_200_OK)



@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)

class Medicineinsert(APIView):
    def post(self, request):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class Medicinepick(APIView):
    

    def get(self, request, id=None):
        if id:
            item = Medicalstore.objects.get(id=id)
            serializer = MedicineSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Medicalstore.objects.all()
        serializer = MedicineSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
class Medicineupdate(APIView):
       
    def patch(self, request, id=None):
        item = Medicalstore.objects.get(id=id)
        serializer = MedicineSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
        
        

class Medicinedelete(APIView):
    
    def delete(self, request, id=None):
        item = get_object_or_404(Medicalstore, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


class Medicinesearch(generics.ListCreateAPIView):
    search_fields = ['Medicine']
    filter_backends = (filters.SearchFilter,)
    queryset = Medicalstore.objects.all()
    serializer_class = MedicineSerializer

class Medicinelist(generics.ListAPIView):
    queryset = Medicalstore.objects.all()
    serializer_class = MedicineSerializer

