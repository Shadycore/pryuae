from django.db import models
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum, F, DateTimeField, Count, FloatField, IntegerField, Prefetch, Case, When
from datetime import datetime, timezone, timedelta, date
from django.db.models.functions import TruncMonth, TruncYear, ExtractMinute, ExtractMonth, ExtractYear, Cast, Coalesce, TruncDay
from django.utils.dateparse import parse_date
import json
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate

import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 


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

    ventas = Venta.objects.filter(fechaVenta__year=anioanterior)
    topventas =  ventas.values('fechaVenta__year', 'detalleventa__cultivo__nombre') \
                .annotate(det_cantidad=Cast(Sum('detalleventa__cantidad'), IntegerField()))\
                .exclude(det_cantidad=None) \
                .order_by('-det_cantidad')[:10]


    fecha_actual = datetime.now()
    fecha_inicio = fecha_actual - timedelta(days=8)

    ventas_semana = Venta.objects.filter(fechaVenta__month=date.today().month, fechaVenta__year=date.today().year) \
                                .annotate(total_venta=Sum('totalVenta'), fecha_venta=TruncDay('fechaVenta')) \
                                .order_by('-fechaVenta')[:8]
    
    fecha_inicio = datetime.now() - timedelta(days=180) 
    fecha_fin = fecha_actual - timedelta(days=8)

    fecha_inicio = date.today() - timedelta(days=(180-8))
    ventas_ultimos_180dias = Venta.objects.filter(fechaVenta__gte=fecha_inicio).annotate(total_venta=Sum('totalVenta'), fecha_venta=TruncDay('fechaVenta')).order_by('-fechaVenta')[:180]

    fechas_venta = ventas_ultimos_180dias.values_list('fecha_venta', flat=True)
    totales_venta = ventas_ultimos_180dias.values_list('total_venta', flat=True)

    # Crear una función de pronóstico
    def pronostico_ventas(fechas, totales, dias_pronostico=8):
        x = np.array(range(len(fechas)))
        y = np.array(totales)
        p4 = np.poly1d(np.polyfit(x, y, 4))
        dias_futuros = np.array(range(len(fechas), len(fechas)+dias_pronostico))
        pronosticos = p4(dias_futuros)
        return pronosticos

    # Crear los pronósticos
    predicciones_df = pronostico_ventas(fechas_venta, totales_venta)

    context = {'anioactual': anioactual, 'anioanterior': anioanterior,
    'tventasanio': tventasanio, 'tventasanioanterior': tventasanioanterior,
    'sumCosecha': sumCosecha, 'sumVentas': sumVentas, 'tcompas': tcompras,
    'tcompras_ant': tcompras_ant, 'topventas': topventas, 'ventas_semana': ventas_semana,
    'predicciones_df': predicciones_df
     }

    return render(request,
                    template_name,
                    context)
