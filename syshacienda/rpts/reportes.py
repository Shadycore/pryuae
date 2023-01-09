from django.shortcuts import render
from django.utils.dateparse import parse_date
from datetime import timedelta

from django.db import models
from vent.models import Venta, DetalleVenta
from mnt.models import Cliente, Cultivo, Produccion, Empleado, Asignacion, Proveedor, RegistroInsumo, Insumo


def imprimirClientes(request):
    template_name="rpts/impClientes.html"

    cliente = Cliente.objects.all().order_by('-id')
    context={
        'titulo':"Informe de cliente",
        'cabecera': { },
        'detalle': cliente
    }

    return render(request,template_name,context)

def imprimirProveedores(request):
    template_name="rpts/impProveedores.html"
    proveedor = Proveedor.objects.all().order_by('-id')

    context={
        'titulo':"Informe de Proveedores",
        'cabecera': { },
        'detalle': proveedor
    }
    
    return render(request,template_name,context)

def imprimirCompras(request,f1=None):
    template_name="rpts/impCompras.html"
    insumo = Insumo.objects.all().order_by('-id')
    context={
        'titulo':"Informe de Compras",
        'cabecera': { },
        'detalle': insumo
    }

    return render(request,template_name,context)
