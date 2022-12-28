from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.serializers import ProduccionSerializer,ClienteSerializer, CultivoSerializer
from mnt.models import Produccion, Cliente, Cultivo

from django.db.models import Q

class ProduccionList(APIView):
    def get(self,request):
        prod = Produccion.objects.all()
        data = ProduccionSerializer(prod,many=True).data
        return Response(data)


class ProduccionDetalle(APIView):
    def get(self,request, codigo):
        prod = get_object_or_404(Produccion,Q(id=codigo))
        #|Q(disponible>0)
        data = ProduccionSerializer(prod).data
        return Response(data)


class ClienteList(APIView):
    def get(self,request):
        obj = Cliente.objects.all()
        data = ClienteSerializer(obj,many=True).data
        return Response(data)

class ProduccionUpdate(APIView):
    #Actualizar cantidad disponible, cantidad venta de Produccion
    def put(self,request, codigo):
        prod = get_object_or_404(Produccion,Q(id=codigo))
        prod.update(request.data)
        prod.save()
