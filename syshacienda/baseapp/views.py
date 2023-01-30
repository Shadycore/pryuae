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
    tiempobi = int(Parametro.objects.filter(nombreParametro="TIEMPOBI") \
                                .values_list('valorParametro', flat=True) \
                                .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                                .get())
    if tiempobi is None or not tiempobi:
        tiempobi = 180
    
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

    ventas = Venta.objects.filter(fechaVenta__year=anioactual,)
    topventas =  ventas.values('fechaVenta__year', 'detalleventa__cultivo__nombre') \
                .annotate(det_cantidad=Cast(Sum('detalleventa__cantidad'), IntegerField()))\
                .exclude(det_cantidad=None) \
                .order_by('-det_cantidad')[:10]


    fecha_actual = datetime.now()
    fecha_inicio = fecha_actual - timedelta(days=8)
    #Obtengo los últimos 8 días de ventas de la base.
    ventas_semana = Venta.objects.filter(fechaVenta__month=date.today().month, fechaVenta__year=date.today().year) \
                                .annotate(total_venta=Sum('totalVenta'), fecha_venta=TruncDay('fechaVenta')) \
                                .order_by('fechaVenta')[:8]
    
    if not ventas_semana:
        ventas_semana = []
        dia_ini = date.today()  - timedelta(days=8)
        for i in range(8):
            fecha_venta = dia_ini + timedelta(days=i)
            fecha_venta = fecha_venta.strftime('%Y-%m-%d')
            ventas_semana.append({'fecha_venta': fecha_venta, 'total_venta': 0})

    ventas = Venta.objects.filter(fechaVenta__gte=datetime.now() - timedelta(days=(tiempobi+8))).values('fechaVenta', 'totalVenta')
    if ventas:
        #realizamos la proyección basado en el parametro tiempobi: 180 días
        df = pd.DataFrame(ventas)
        df['fechaVenta'] = pd.to_datetime(df['fechaVenta']) # Convertimos la columna fechaVenta a tipo datetime
        df['dias'] = (df['fechaVenta'] - df['fechaVenta'].min())  / np.timedelta64(1,'D') # Creamos una columna con el número de días desde el primer registro de venta 
        X = df[['dias']] # Definimos X como la columna dias del DataFrame 
        y = df[['totalVenta']] # Definimos y como la columna totalVenta del DataFrame 
        model = LinearRegression() # Creamos un modelo de regresión lineal 
        model.fit(X, y) # Entrenamos el modelo con los datos obtenidos 
        predicciones = model.predict([[181], [182], [183], [184], [185], [186], [187], [188]]) # Realizamos predicciones para los siguientes 8 días 
        pred_formateada = np.round(predicciones, decimals=0).tolist() # Redondeamos las predicciones a 0 decimales 
        pred_formateada =  [int(numero[0]) for numero in pred_formateada] # formateamos la lsta
    else:
         pred_formateada =  [0,0,0,0,0,0,0,0] # formateamos la lsta
         

    context = {'anioactual': anioactual, 'anioanterior': anioanterior,
    'tventasanio': tventasanio, 'tventasanioanterior': tventasanioanterior,
    'sumCosecha': sumCosecha, 'sumVentas': sumVentas, 'tcompras': tcompras,
    'tcompras_ant': tcompras_ant, 'topventas': topventas, 'ventas_semana': ventas_semana,
    'predicciones_df': pred_formateada
     }

    return render(request,
                    template_name,
                    context)
