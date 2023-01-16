from django.db import models
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum, F, DateTimeField, Count, FloatField, IntegerField, Prefetch, Case, When
from datetime import datetime, timezone, timedelta 
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

    ventas = Venta.objects.filter(fechaVenta__year=anioactual)
    topventas =  ventas.values('fechaVenta__year', 'detalleventa__cultivo__nombre') \
                .annotate(det_cantidad=Cast(Sum('detalleventa__cantidad'), IntegerField()))\
                .exclude(det_cantidad=None) \
                .order_by('-det_cantidad')[:10]

    ventas_semana = Venta.objects.filter(fechaVenta__gte=parse_date('8 days ago')) \
                                .annotate(
                                    dia_semana=Case(
                                        When(fechaVenta__week_day=1, then=CharField('Lun')),
                                        When(fechaVenta__week_day=2, then=CharField('Mar')),
                                        When(fechaVenta__week_day=3, then=CharField('Mie')),
                                        When(fechaVenta__week_day=4, then=CharField('Jue')),
                                        When(fechaVenta__week_day=5, then=CharField('Vie')),
                                        When(fechaVenta__week_day=6, then=CharField('Sab')),
                                        When(fechaVenta__week_day=7, then=CharField('Dom')),
                                        output_field=CharField()
                                    )) \
                                .annotate(total_dia=Sum('totalVenta')) \
                                .values('dia_semana') \
                                .annotate(total_dia=Sum('total_dia'))\
                                .order_by('-fechaVenta')
    fecha_inicio = datetime.now() - timedelta(days=180) 
    fecha_fin = datetime.now()

    ventas = Venta.objects.filter(fechaVenta__gte=fecha_inicio, fechaVenta__lte=fecha_fin) 

    # Crear un DataFrame con los datos 
    datos_ventas = pd.DataFrame(list(ventas.values('cliente', 'fechaVenta', 'subTotal', 'totalVenta', 'porcIva', 'totalIva'))) 

    # Preparar los datos para el entrenamiento 
    X = datos_ventas.drop('totalVenta', axis=1) 
    Y = datos_ventas['totalVenta'] 

    # Dividir los datos en entrenamiento y validación 
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0) 

    # Crear el modelo de regresión lineal 
    regresion_lineal = LinearRegression()
    regresion_lineal.fit(X_train, Y_train)

    # Predecir los resultados de las últimas 8 ventas 
    predicciones_ventas = regresion_lineal.predict(X_test)

    # Crear el DataFrame de predicciones
    predicciones_df = pd.DataFrame(predicciones_ventas, columns=['Prediccion'])

    # Obtener la fecha para cada predicción
    fechas_predicciones = X_test['fechaVenta'].tolist()

    # Obtener el nombre del día para cada predicción
    dias_predicciones = []
    for fecha in fechas_predicciones:
        dias_predicciones.append(fecha.strftime("%A"))

    # Agregar el nombre del día al DataFrame
    predicciones_df['Dia'] = dias_predicciones

    # Agregar la columna con el total de ventas
    predicciones_df['Total de Ventas'] = predicciones_df.groupby('Dia')['Prediccion'].transform(Sum)

    context = {'anioactual': anioactual, 'anioanterior': anioanterior,
    'tventasanio': tventasanio, 'tventasanioanterior': tventasanioanterior,
    'sumCosecha': sumCosecha, 'sumVentas': sumVentas, 'tcompas': tcompras,
    'tcompras_ant': tcompras_ant, 'topventas': topventas, 'ventas_semana': ventas_semana,
    'predicciones_df': predicciones_df
     }

    return render(request,
                    template_name,
                    context)
