from django.db import models
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum, F, DateTimeField, Count, FloatField, IntegerField, Prefetch, Case, When
from datetime import datetime, timezone
from django.db.models.functions import TruncMonth, TruncYear, ExtractMinute, ExtractMonth, ExtractYear, Cast, Coalesce
import json
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate

from mnt.views import ClienteView, CultivoView, ProduccionView, \
                            HaciendaView, EmpleadoNew, AsignacionView, \
                            ProveedorNew, RegistroInsumoNew
from mnt.models import Cliente, Cultivo, Produccion, DescripcionLote, \
                        Hacienda, Empleado, Asignacion, \
                        Proveedor, RegistroInsumo, Insumo, \
                        Parametro
from vent.views import ventasView, VentaView
from vent.models import Venta, DetalleVenta

#class Home(LoginRequiredMixin, generic.ListView):
#    template_name = 'baseapp/home.html'
#    login_url = "/login"

@login_required(login_url='/login/')
def Home(request):
    template_name='baseapp/home.html'
    anioactual = datetime.now().year
    anioanterior = anioactual-1

    tventasanio = Venta.objects.filter(fechaVenta__year=anioactual)\
                                .aggregate(sum_total=Cast(Sum('totalVenta'),IntegerField()))
    if tventasanio['sum_total'] is None:
        tventasanio = 0
    else:
        tventasanio = tventasanio['sum_total']

    tventasanioanterior = Venta.objects.filter(fechaVenta__year=anioanterior)\
                                .aggregate(sum_total=Cast(Sum('totalVenta'),IntegerField()))
    if tventasanioanterior['sum_total'] is None:
        tventasanioanterior = 0
    else:
        tventasanioanterior = tventasanioanterior['sum_total']

    
    prod = Produccion.objects.filter(fecha__year=anioactual) \
                            .aggregate(sum_Cosecha=Cast(Sum('cantidadCosecha'),IntegerField()))

    vent = Produccion.objects.filter(fecha__year=anioactual) \
                            .aggregate(sum_Venta=Cast(Sum('cantidadVentaCosecha'),IntegerField()))

    if prod['sum_Cosecha'] is None:
        sumCosecha = 0
    else:
        sumCosecha = prod['sum_Cosecha']

    if vent['sum_Venta'] is None:
        sumVentas = 0
    else:
        sumVentas = vent['sum_Venta']

    
    tcompras = RegistroInsumo.objects.filter(fechaCompra__year=anioactual) \
                                    .aggregate(sum_precio=Cast(Sum('precio'),IntegerField()))

    if tcompras['sum_precio'] is None:
        tcompras = 0
    else:
        tcompras = tcompras['sum_precio']

    tcompras_ant = RegistroInsumo.objects.filter(fechaCompra__year=anioanterior) \
                                    .aggregate(sum_precio=Cast(Sum('precio'),IntegerField()))

    if tcompras_ant['sum_precio'] is None:
        tcompras_ant = 0
    else:
        tcompras_ant = tcompras_ant['sum_precio']

    ventas = Venta.objects.filter(fechaVenta__year=anioactual)
    topventas =  ventas.values('fechaVenta__year', 'detalleventa__cultivo__nombre') \
                .annotate(det_cantidad=Cast(Sum('detalleventa__cantidad'), IntegerField()))\
                .order_by('-det_cantidad')[:10]


    context = {'anioactual': anioactual, 'anioanterior': anioanterior,
    'tventasanio': tventasanio, 'tventasanioanterior': tventasanioanterior,
    'sumCosecha': sumCosecha, 'sumVentas': sumVentas, 'tcompas': tcompras,
    'tcompras_ant': tcompras_ant, 'topventas': topventas 
     }

    return render(request,
                    template_name,
                    context)
