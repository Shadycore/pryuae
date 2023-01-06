from django.shortcuts import render
from django.utils.dateparse import parse_date
from datetime import timedelta

from django.db import models
from vent.models import Venta, DetalleVenta
from mnt.models import Cliente, Cultivo, Produccion, Empleado, Asignacion, Proveedor


def imprimirLista(request,id,f1=None,f2=None):
    template_name="rpts/imprimirlista.html"
    #Clientes
    if id == 1:
        cliente = Cliente.objects.all().order_by('-id')
        context={
            'opt'   : "1",
            'titulo':"Informe de cliente",
            'cabecera': { "id", "Apellido", "Nombre", "Email", "Teléfono", "Ciudad" },
            'detalle': cliente
        }

    #Proveedores
    if id ==2:
        vent = Venta.objects.get(id=id)
        det = DetalleVenta.objects.filter(venta=id)

        context={
            'request':request,
            'venta':vent,
            'detalle':det
        }
    
    #compras
    if id == 3:
        vent = Venta.objects.get(id=id)
        det = DetalleVenta.objects.filter(venta=id)
        context={
            'request':request,
            'venta':vent,
            'detalle':det
        }

    return render(request,template_name,context)
