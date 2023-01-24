from django.db import models
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.db.models import Sum, F, DateTimeField, Count, FloatField, IntegerField, Prefetch, Case, When
from datetime import datetime, timezone, timedelta, date
from django.db.models.functions import TruncMonth, TruncYear, ExtractMinute, ExtractMonth, ExtractYear, Cast, Coalesce
from django.db.models.query import Q
import json
from django.http import HttpResponse
from datetime import datetime
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

import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 


@login_required(login_url='/login/')
def analiticaView(request):
    template_name = 'analitica.html'
    anioactual = datetime.now().year
    dFecha = datetime.now().year
    flag = True
    idcultivo = 0
    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))
        idcultivo = 0 #int(request.POST.get("id_cultivo"))
        if idcultivo==0:
            flag = False
    
    anios = int(Parametro.objects.filter(nombreParametro="ANIOS") \
                        .values_list('valorParametro', flat=True) \
                        .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                        .get())
    ianio = dFecha
    anioanterior = ianio-1
    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]

    tiempobi = int(Parametro.objects.filter(nombreParametro="TIEMPOBI") \
                                .values_list('valorParametro', flat=True) \
                                .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                                .get())
    if tiempobi is None or not tiempobi:
        tiempobi = 180
    listaProduccion = Produccion.objects.filter(Q(estado=True)).order_by('id')

    ## Ano actual [ ianio ]
    tactividades = Asignacion.objects.filter(fecha__year=anioactual)\
                                .aggregate(actividades_realizadas=Count('actividad')) 

    tactividades_ant = Asignacion.objects.filter(fecha__year=anioactual)\
                                .aggregate(actividades_realizadas=Count('actividad')) 
    #actividades = Asignacion.objects.filter(fecha__year=ianio, cultivo=idcultivo).annotate(actividades_realizadas=Count('actividad'))

    tventasanio = Venta.objects.filter(fechaVenta__year=anioactual)\
                                .aggregate(sum_total=Cast(Sum('totalVenta'),IntegerField()))

    tventasanioanterior = Venta.objects.filter(fechaVenta__year=anioanterior)\
                                .aggregate(sum_total=Cast(Sum('totalVenta'),IntegerField()))
    
    prod = Produccion.objects.filter(fecha__year=anioactual) \
                            .aggregate(sum_Cosecha=Cast(Sum('cantidadCosecha'),IntegerField()))
    
    prod_ant = Produccion.objects.filter(fecha__year=anioanterior) \
                            .aggregate(sum_Cosecha=Cast(Sum('cantidadCosecha'),IntegerField()))
    
    vent = Produccion.objects.filter(fecha__year=anioactual) \
                            .aggregate(sum_Venta=Cast(Sum('cantidadVentaCosecha'),IntegerField()))

    vent_ant = Produccion.objects.filter(fecha__year=anioanterior) \
                            .aggregate(sum_Venta=Cast(Sum('cantidadVentaCosecha'),IntegerField()))

    tcompras = RegistroInsumo.objects.filter(fechaCompra__year=anioactual) \
                                    .aggregate(sum_precio=Cast(Sum('precio'),IntegerField()))

    tcompras_ant = RegistroInsumo.objects.filter(fechaCompra__year=anioanterior) \
                                    .aggregate(sum_precio=Cast(Sum('precio'),IntegerField()))

    ventasmesanio = Venta.objects.exclude(totalVenta=None) \
                                    .filter(fechaVenta__year=anioactual) \
                                    .annotate(month=F('fechaVenta__month')) \
                                    .values('month') \
                                    .annotate(total_venta=Sum('totalVenta', output_field=IntegerField()))\
                                    .order_by('month')
    
    datoVentas = {'01': 0, '02': 0, '03': 0, '04': 0,
            '05': 0, '06': 0, '07': 0, '08': 0,
            '09': 0, '10': 0, '11': 0, '12': 0}

    for item in ventasmesanio:
        if item.get('total') is None:
             item['total'] = 0
        
        if item.get('month') == 1:
            datoVentas['01'] = item.get('total')
        if item.get('month') == 2:
            datoVentas['02'] = item.get('total')
        if item.get('month') == 3:
            datoVentas['03'] = item.get('total')
        if item.get('month') == 4:
            datoVentas['04'] = item.get('total')
        if item.get('month') == 5:
            datoVentas['05'] = item.get('total')
        if item.get('month') == 6:
            datoVentas['06'] = item.get('total')
        if item.get('month') == 7:
            datoVentas['07'] = item.get('total')
        if item.get('month') == 8:
            datoVentas['08'] = item.get('total')
        if item.get('month') == 9:
            datoVentas['09'] = item.get('total')
        if item.get('month') == 10:
            datoVentas['10'] = item.get('total')
        if item.get('month') == 11:
            datoVentas['11'] = item.get('total')
        if item.get('month') == 12:
            datoVentas['12'] = item.get('total')

    salidaventasanio = [datoVentas[key] for key in datoVentas]
    #salida2 = [dato2[key] for key in dato2]
    ## Validacion info
    if tactividades['actividades_realizadas'] is None:
        tactividades = 0
    else:
        tactividades = int(tactividades['actividades_realizadas'])

    if tactividades_ant['actividades_realizadas'] is None:
        tactividades_ant = 0
    else:
        tactividades_ant = int(tactividades_ant['actividades_realizadas'])


    if tventasanio['sum_total'] is None:
        tventasanio = 0
    else:
        tventasanio = tventasanio['sum_total']

    if tventasanioanterior['sum_total'] is None:
        tventasanioanterior = 0
    else:
        tventasanioanterior = tventasanioanterior['sum_total']

    if prod['sum_Cosecha'] is None:
        sumCosecha = 0
    else:
        sumCosecha = prod['sum_Cosecha']

    if prod_ant['sum_Cosecha'] is None:
        sumCosecha_ant = 0
    else:
        sumCosecha_ant = prod_ant['sum_Cosecha']

    if vent['sum_Venta'] is None:
        sumVentas = 0
    else:
        sumVentas = vent['sum_Venta']

    if vent_ant['sum_Venta'] is None:
        sumVentas_ant = 0
    else:
        sumVentas_ant = vent_ant['sum_Venta']


    if tcompras['sum_precio'] is None:
        tcompras = 0
    else:
        tcompras = tcompras['sum_precio']

    if tcompras_ant['sum_precio'] is None:
        tcompras_ant = 0
    else:
        tcompras_ant = tcompras_ant['sum_precio']

    if not listaProduccion or listaProduccion['id'] is None:
        listaProduccion = {'':''}
    
    ventas = Venta.objects.filter(fechaVenta__year=anioactual,)
    topventas =  ventas.values('fechaVenta__year', 'detalleventa__cultivo__nombre') \
                .annotate(det_cantidad=Cast(Sum('detalleventa__cantidad'), IntegerField()))\
                .exclude(det_cantidad=None) \
                .order_by('-det_cantidad')[:10]
    
    if not topventas or topventas['det_cantidad'] is None:
        topventas = [{'fechaVenta': '2020','detalleventa__cultivo__nombre': '', 'det_cantidad': 0},
                      {'fechaVenta': '2020','detalleventa__cultivo__nombre': '', 'det_cantidad': 0},
                       {'fechaVenta': '2020','detalleventa__cultivo__nombre': '', 'det_cantidad': 0},
                        {'fechaVenta': '2020','detalleventa__cultivo__nombre': '', 'det_cantidad': 0},
                        {'fechaVenta': '2020','detalleventa__cultivo__nombre': '', 'det_cantidad': 0},
                        {'fechaVenta': '2020','detalleventa__cultivo__nombre': '', 'det_cantidad': 0},
                        {'fechaVenta': '2020','detalleventa__cultivo__nombre': '', 'det_cantidad': 0},
                        {'fechaVenta': '2020','detalleventa__cultivo__nombre': '', 'det_cantidad': 0},
                         {'fechaVenta': '2020','detalleventa__cultivo__nombre': '', 'det_cantidad': 0},
                         {'fechaVenta': '2020','detalleventa__cultivo__nombre': '', 'det_cantidad': 0}]

    ventas = Venta.objects.filter(fechaVenta__gte=datetime.now() - timedelta(days=(tiempobi+8))).values('fechaVenta', 'totalVenta')
    if not ventas or ventas['fechaVenta'] is None:
        pred_formateada = [0,0,0,0,0,0,0,0] # formateamos la lsta
    else:
        #realizamos la proyección basado en el parametro tiempobi: 180 días
        df = pd.DataFrame(ventas)
        df['fechaVenta'] = pd.to_datetime(df['fechaVenta']) # Convertimos la columna fechaVenta a tipo datetime
        df['dias'] = (df['fechaVenta'] - df['fechaVenta'].min())  / np.timedelta64(1,'D') # Creamos una columna con el número de días desde el primer registro de venta 
        X = df[['dias']] # Definimos X como la columna dias del DataFrame 
        y = df[['totalVenta']] # Definimos y como la columna totalVenta del DataFrame 
        model = LinearRegression() # Creamos un modelo de regresión lineal 
        model.fit(X, y) # Entrenamos el modelo con los datos obtenidos 
        predicciones = model.predict([[181], [182], [183], [184], [185], [186], [187], [188], [189], [190], [191], [192]]) # Realizamos predicciones para los siguientes 8 días 
        pred_formateada = np.round(predicciones, decimals=0).tolist() # Redondeamos las predicciones a 0 decimales 
        pred_formateada =  [int(numero[0]) for numero in pred_formateada] # formateamos la lsta

    context = {'anioactual': anioactual, 'anioanterior': anioanterior,
    'tventasanio': tventasanio, 'sumCosecha': sumCosecha, 'sumVentas': sumVentas, 
    'tcompras': tcompras, 'tactividades': tactividades,
    'topventas': topventas, 'listaProduccion': listaProduccion,
    'anios': oanios,'ianio': ianio, 'predicciones_df': pred_formateada, 
    'tventasanioanterior': tventasanioanterior, 'tcompras_ant': tcompras_ant, 'sumCosecha_ant': sumCosecha_ant,
    'sumVentas_ant': sumVentas_ant, 'tactividades_ant': tactividades_ant, 'ventasanio': salidaventasanio
     }

    return render(request,
                    template_name,
                    context)