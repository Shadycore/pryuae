from django.db import models
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.db.models import Sum, F, DateTimeField, Count, FloatField, IntegerField, Prefetch, Case, When, Avg, Min, Max
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
from rpts.views import iProveedoresView, iClientesView, \
                        iComprasView, iComprasView_, \
                        oProduccionView, oProductosMasVendidosView, \
                        oVentasPorCultivoView, oGananciasView, \
                        impComprasView, impGananciasView, impProduccionView, \
                        impProductosMasVendidosView, impVentasPorCultivoView
                        
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
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
        if idcultivo=='0':
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

    ventas = Venta.objects.filter(fechaVenta__year=anioactual,)
    topventas =  ventas.values('fechaVenta__year', 'detalleventa__cultivo__nombre') \
                .annotate(det_cantidad=Cast(Sum('detalleventa__cantidad'), IntegerField()))\
                .exclude(det_cantidad=None) \
                .order_by('-det_cantidad')[:10]

    ventas = Venta.objects.filter(fechaVenta__gte=datetime.now() - timedelta(days=(tiempobi+8))).values('fechaVenta', 'totalVenta')

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

@login_required(login_url='/login/')
def superficieView(request):
    template_name="superficie.html"
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))

    anios = int(Parametro.objects.filter(nombreParametro="ANIOS") \
                            .values_list('valorParametro', flat=True) \
                            .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                            .get())

    ianio = dFecha
    ianio_anterior = ianio-1

    obj =  Produccion.objects.filter(fecha__year=ianio) \
                            .annotate(mes=ExtractMonth('fecha'), anio=ExtractYear('fecha')) \
                            .values('mes', 'anio', 'cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha') / Count('cantidadVentaCosecha'),IntegerField()) , total_venta_cosecha =Sum('cantidadVentaCosecha'),total_descripcionlote_area =Cast(Sum('descripcionlote__area'),IntegerField())) \
                            .order_by('anio', 'mes')

    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]

    datoLineal = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField()),\
                                        total_venta_cosecha=Cast(Sum('cantidadVentaCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')

    datoComprativo = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')


    context = {'obj': obj, 'datoLineal':  datoLineal,
            'datoComparativo': datoComprativo, 'dFecha': dFecha,
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)

@login_required(login_url='/login/')
def rendimientoView(request):
    template_name="rendimiento.html"
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))

    anios = int(Parametro.objects.filter(nombreParametro="ANIOS") \
                            .values_list('valorParametro', flat=True) \
                            .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                            .get())

    ianio = dFecha
    ianio_anterior = ianio-1

    obj =  Produccion.objects.filter(fecha__year=ianio) \
                            .annotate(mes=ExtractMonth('fecha'), anio=ExtractYear('fecha')) \
                            .values('mes', 'anio', 'cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField()) , \
                                    cultivo_cosecha =(Cast((Sum('cantidadCosecha') / Sum('descripcionlote__area')), FloatField())), \
                                    total_descripcionlote_area =Cast(Sum('descripcionlote__area'),IntegerField())) \
                            .order_by('anio', 'mes')

    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]

    datoLineal = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField()),\
                                        total_venta_cosecha=Cast(Sum('cantidadVentaCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')

    datoComprativo = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')


    context = {'obj': obj, 'datoLineal':  datoLineal,
            'datoComparativo': datoComprativo, 'dFecha': dFecha,
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)

@login_required(login_url='/login/')
def cantidadesView(request):
    template_name="cantidades.html"
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))

    anios = int(Parametro.objects.filter(nombreParametro="ANIOS") \
                            .values_list('valorParametro', flat=True) \
                            .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                            .get())

    ianio = dFecha
    ianio_anterior = ianio-1

    obj =  Produccion.objects.filter(fecha__year=ianio) \
                            .annotate(mes=ExtractMonth('fecha'), anio=ExtractYear('fecha')) \
                            .values('mes', 'anio', 'cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField()), 
                                      total_venta_cosecha =Sum('cantidadVentaCosecha'),
                                      total_descripcionlote_area =Cast(Sum('descripcionlote__area'),IntegerField())) \
                            .order_by('anio', 'mes')

    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]

    datoLineal = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')

    datoComprativo = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')


    context = {'obj': obj, 'datoLineal':  datoLineal,
            'datoComparativo': datoComprativo, 'dFecha': dFecha,
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)

@login_required(login_url='/login/')
def costoproduccionView(request):
    template_name="costoproduccion.html"
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))


    #if request.method == 'GET':
    #    if f1 is not None:
    #        dFecha = f1

    #if request.method == 'POST':
    #    f1 = int(request.POST.get("id_anios"))
    #    if f1 is not None:
    #        dFecha = f1

    anios = int(Parametro.objects.filter(nombreParametro="ANIOS") \
                            .values_list('valorParametro', flat=True) \
                            .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                            .get())

    ianio = dFecha
    ianio_anterior = ianio-1

    obj = RegistroInsumo.objects \
                        .filter(fechaCompra__year=ianio) \
                        .annotate(anio=F('fechaCompra__year'),
                                    month=F('fechaCompra__month'),
                                    insumo_name=F('insumo__nombre'),
                                    nombre_cultivo=F('cultivo__nombre')) \
                        .values('anio','month', 'insumo_name','nombre_cultivo') \
                        .annotate(total_compras=Sum('precio')) \
                        .order_by('anio','month','insumo_name')

    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]

    dato1 = {'01': 0, '02': 0, '03': 0, '04': 0,
             '05': 0, '06': 0, '07': 0, '08': 0,
             '09': 0, '10': 0, '11': 0, '12': 0}
    dato2 = {'01': 0, '02': 0, '03': 0, '04': 0,
             '05': 0, '06': 0, '07': 0, '08': 0,
             '09': 0, '10': 0, '11': 0, '12': 0}

    datoLineal = RegistroInsumo.objects \
                                .filter(fechaCompra__year=ianio) \
                                .annotate(month=ExtractMonth('fechaCompra'), year=ExtractYear('fechaCompra')) \
                                .values('month', 'year') \
                                .annotate(total=Cast(Sum('precio'), IntegerField()))  \
                                .annotate(total_int=Cast(Sum('precio'), IntegerField())) \
                                .order_by('month')

    datoComprativo = RegistroInsumo.objects \
                        .filter(fechaCompra__year=ianio) \
                        .annotate(nombre_cultivo=F('cultivo__nombre')) \
                        .values('nombre_cultivo') \
                        .annotate(total_compras=Cast(Sum('precio'),IntegerField())) \
                        .order_by('-total_compras')

    for item in datoLineal:
        if item.get('month') == 1:
            dato1['01'] = item.get('total')
        if item.get('month') == 2:
            dato1['02'] = item.get('total')
        if item.get('month') == 3:
            dato1['03'] = item.get('total')
        if item.get('month') == 4:
            dato1['04'] = item.get('total')
        if item.get('month') == 5:
            dato1['05'] = item.get('total')
        if item.get('month') == 6:
            dato1['06'] = item.get('total')
        if item.get('month') == 7:
            dato1['07'] = item.get('total')
        if item.get('month') == 8:
            dato1['08'] = item.get('total')
        if item.get('month') == 9:
            dato1['09'] = item.get('total')
        if item.get('month') == 10:
            dato1['10'] = item.get('total')
        if item.get('month') == 11:
            dato1['11'] = item.get('total')
        if item.get('month') == 12:
            dato1['12'] = item.get('total')

        if item.get('month') == 1:
            dato2['01'] = item.get('total')
        if item.get('month') == 2:
            dato2['02'] = item.get('total')
        if item.get('month') == 3:
            dato2['03'] = item.get('total')
        if item.get('month') == 4:
            dato2['04'] = item.get('total')
        if item.get('month') == 5:
            dato2['05'] = item.get('total')
        if item.get('month') == 6:
            dato2['06'] = item.get('total')
        if item.get('month') == 7:
            dato2['07'] = item.get('total')
        if item.get('month') == 8:
            dato2['08'] = item.get('total')
        if item.get('month') == 9:
            dato2['09'] = item.get('total')
        if item.get('month') == 10:
            dato2['10'] = item.get('total')
        if item.get('month') == 11:
            dato2['11'] = item.get('total')
        if item.get('month') == 12:
            dato2['12'] = item.get('total')

    salida1 = [dato1[key] for key in dato1]


    context = {'obj': obj, 'datoLineal':  salida1,
            'datoComparativo': datoComprativo, 'dFecha': dFecha,
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)

@login_required(login_url='/login/')
def precioventaView(request):
    template_name="precioventa.html"
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))

    anios = int(Parametro.objects.filter(nombreParametro="ANIOS") \
                            .values_list('valorParametro', flat=True) \
                            .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                            .get())

    ianio = dFecha
    ianio_anterior = ianio-1

    ventas = Venta.objects.filter(fechaVenta__year=ianio)
    obj =  ventas.values('fechaVenta__year', 'detalleventa__cultivo__nombre') \
                .annotate(cantidad=Count('detalleventa__cultivo'), 
                          det_total=Cast(Sum('detalleventa__total'),IntegerField()), 
                          det_cantidad=Cast(Sum('detalleventa__cantidad'),IntegerField()),
                          min_precio = Min('detalleventa__precio'),
                          max_precio = Max('detalleventa__precio'),
                          prom_precio =round(Avg('detalleventa__precio'),2)) \
                .order_by('-cantidad')

    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]

    datoLineal = ventas.values('fechaVenta__year', 'detalleventa__cultivo__nombre') \
                .annotate(cantidad=Count('detalleventa__cultivo'), det_total=Cast(Sum('detalleventa__total'),IntegerField()), det_cantidad=Cast(Sum('detalleventa__cantidad'),IntegerField())) \
                .filter(Q(det_total__isnull=False) & Q(det_cantidad__isnull=False)) \
                .order_by('-cantidad')

    cultivos = [item['detalleventa__cultivo__nombre'] for item in datoLineal ]
    ventas_com = Venta.objects.filter(fechaVenta__year=ianio_anterior)
    datoComprativo = ventas_com.values('fechaVenta__year', 'detalleventa__cultivo__nombre') \
                .annotate(cantidad=Count('detalleventa__cultivo'), det_total=Cast(Sum('detalleventa__total'),IntegerField()), det_cantidad=Cast(Sum('detalleventa__cantidad'),IntegerField())) \
                .order_by('-cantidad')

    context = {'obj': obj, 'datoLineal':  datoLineal,
            'datoComparativo': datoComprativo, 'dFecha': dFecha,
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)

@login_required(login_url='/login/')
def lotescultivadosView(request):
    template_name="lotescultivados.html"
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))

    anios = int(Parametro.objects.filter(nombreParametro="ANIOS") \
                            .values_list('valorParametro', flat=True) \
                            .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                            .get())

    ianio = dFecha
    ianio_anterior = ianio-1

    obj =  Produccion.objects.filter(fecha__year=ianio) \
                            .annotate(mes=ExtractMonth('fecha'), anio=ExtractYear('fecha')) \
                            .values('mes', 'anio', 'cultivo__nombre','cultivo__lote',descripcionlote_area=Cast('descripcionlote__area',IntegerField())) \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField()) , 
                                        total_venta_cosecha =Sum('cantidadVentaCosecha')) \
                            .order_by('anio', 'mes',  'cultivo__nombre','cultivo__lote')

    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]

    datoLineal = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField()),
                                        total_venta_cosecha=Cast(Sum('cantidadVentaCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')

    datoComprativo = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')


    context = {'obj': obj, 'datoLineal':  datoLineal,
            'datoComparativo': datoComprativo, 'dFecha': dFecha,
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)

@login_required(login_url='/login/')
def masproducidosView(request):
    template_name="masproducidos.html"
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))

    anios = int(Parametro.objects.filter(nombreParametro="ANIOS") \
                            .values_list('valorParametro', flat=True) \
                            .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                            .get())

    ianio = dFecha
    ianio_anterior = ianio-1

    obj =  Produccion.objects.filter(fecha__year=ianio) \
                            .annotate(mes=ExtractMonth('fecha'), anio=ExtractYear('fecha')) \
                            .values('mes', 'anio', 'cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField()), 
                                      total_venta_cosecha =Sum('cantidadVentaCosecha'),
                                      total_descripcionlote_area =Cast(Sum('descripcionlote__area'),IntegerField())) \
                            .order_by('-total_cosecha')

    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]

    datoLineal = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField()),
                                        total_venta_cosecha=Cast(Sum('cantidadVentaCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')

    datoComprativo = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')


    context = {'obj': obj, 'datoLineal':  datoLineal,
            'datoComparativo': datoComprativo, 'dFecha': dFecha,
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)

@login_required(login_url='/login/')
def valorminimoView(request):
    template_name="valorminimo.html"
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))

    anios = int(Parametro.objects.filter(nombreParametro="ANIOS") \
                            .values_list('valorParametro', flat=True) \
                            .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                            .get())

    ianio = dFecha
    ianio_anterior = ianio-1

    obj =  Produccion.objects.filter(fecha__year=ianio) \
                            .annotate(anio=ExtractYear('fecha')) \
                            .values('anio', 'cultivo__nombre') \
                            .annotate(min_cosecha=Cast(Min('cantidadCosecha'),IntegerField()) , 
                                    min_precio =Cast(Min('precio'), IntegerField()), 
                                    min_descripcionlote_area =Cast(Min('descripcionlote__area'),IntegerField()),
                                    min_ganancia = Cast((Min('cantidadCosecha') * Min('precio')), IntegerField())) \
                            .order_by('anio', 'cultivo__nombre')

    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]

    datoLineal = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField()),\
                                        total_venta_cosecha=Cast(Sum('cantidadVentaCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')

    datoComprativo = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')


    context = {'obj': obj, 'datoLineal':  datoLineal,
            'datoComparativo': datoComprativo, 'dFecha': dFecha,
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)

@login_required(login_url='/login/')
def valormaximoView(request):
    template_name="valormaximo.html"
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))

    anios = int(Parametro.objects.filter(nombreParametro="ANIOS") \
                            .values_list('valorParametro', flat=True) \
                            .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                            .get())

    ianio = dFecha
    ianio_anterior = ianio-1

    obj =  Produccion.objects.filter(fecha__year=ianio) \
                            .annotate(anio=ExtractYear('fecha')) \
                            .values('anio', 'cultivo__nombre') \
                            .annotate(max_cosecha=Cast(Max('cantidadCosecha'),IntegerField()) , 
                                    max_precio =Cast(Max('precio'), IntegerField()), 
                                    max_descripcionlote_area =Cast(Max('descripcionlote__area'),IntegerField()),
                                    max_ganancia = Cast((Max('cantidadCosecha') * Max('precio')), IntegerField())) \
                            .order_by('anio', 'cultivo__nombre')

    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]

    datoLineal = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField()),\
                                        total_venta_cosecha=Cast(Sum('cantidadVentaCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')

    datoComprativo = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')


    context = {'obj': obj, 'datoLineal':  datoLineal,
            'datoComparativo': datoComprativo, 'dFecha': dFecha,
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)

@login_required(login_url='/login/')
def valorpromedioView(request):
    template_name="valorpromedio.html"
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))

    anios = int(Parametro.objects.filter(nombreParametro="ANIOS") \
                            .values_list('valorParametro', flat=True) \
                            .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                            .get())

    ianio = dFecha
    ianio_anterior = ianio-1

    obj =  Produccion.objects.filter(fecha__year=ianio) \
                            .annotate(anio=ExtractYear('fecha')) \
                            .values('anio', 'cultivo__nombre') \
                            .annotate(prom_cosecha=Cast(Avg('cantidadCosecha'),IntegerField()) , 
                                    prom_precio =Cast(Avg('precio'), IntegerField()), 
                                    prom_descripcionlote_area =Cast(Avg('descripcionlote__area'),IntegerField()),
                                    prom_ganancia = Cast((Avg('cantidadCosecha') * Avg('precio')), IntegerField())) \
                            .order_by('anio', 'cultivo__nombre')

    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]

    datoLineal = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField()),\
                                        total_venta_cosecha=Cast(Sum('cantidadVentaCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')

    datoComprativo = Produccion.objects.filter(fecha__year=ianio) \
                            .values('cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField())) \
                            .order_by('cultivo__nombre')


    context = {'obj': obj, 'datoLineal':  datoLineal,
            'datoComparativo': datoComprativo, 'dFecha': dFecha,
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)

@login_required(login_url='/login/')
def masproduciraView(request):
    template_name="masproducira.html"
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))

    tiempobi = int(Parametro.objects.filter(nombreParametro="TIEMPOBI") \
                                .values_list('valorParametro', flat=True) \
                                .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                                .get())
    if tiempobi is None or not tiempobi:
        tiempobi = 180
    
    anios = int(Parametro.objects.filter(nombreParametro="ANIOS") \
                            .values_list('valorParametro', flat=True) \
                            .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                            .get())

    ianio = dFecha
    ianio_anterior = ianio-1

    #obj =  #Produccion.objects.filter(fecha__year=ianio) \
           #                 .annotate(mes=ExtractMonth('fecha'), anio=ExtractYear('fecha')) \
           #                 .values('mes', 'anio', 'cultivo__nombre') \
           #                 .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField()), 
           #                           total_venta_cosecha =Sum('cantidadVentaCosecha'),
           #                           total_descripcionlote_area =Cast(Sum('descripcionlote__area'),IntegerField())) \
           #                 .order_by('-total_cosecha')

    #Obtener los datos de los últimos 180 días de Producción
    obj = Produccion.objects.filter(fecha__gte=datetime.now()-timedelta(days=tiempobi)) \
                            .values('cultivo__nombre', 'cantidadCosecha')

    #Crear un DataFrame con los datos
    df = pd.DataFrame(list(obj))

    #Codificar los nombres de cultivo a números con LabelEncoder
    encoder = LabelEncoder()
    encoder.fit(df['cultivo__nombre'])
    df['cultivo__nombre'] = encoder.transform(df['cultivo__nombre'])

    #Crear un modelo de regresión lineal
    model = LinearRegression()

    #Entrenar el modelo
    model.fit(df[['cultivo__nombre']], df[['cantidadCosecha']])

    #Predecir cantidad de cosecha para los próximos 180 días
    predicciones = model.predict(df[['cultivo__nombre']])

    #Crear un diccionario con los resultados
    resultados = {'cultivo': encoder.inverse_transform(df['cultivo__nombre']), 'cantidadCosecha': df['cantidadCosecha'], 'prediccion': predicciones} 

    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]

    datoLineal = None #Produccion.objects.filter(fecha__year=ianio) \
                 #           .values('cultivo__nombre') \
                 #           .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField()),
                 #                       total_venta_cosecha=Cast(Sum('cantidadVentaCosecha'),IntegerField())) \
                 #          .order_by('cultivo__nombre')

    datoComprativo = None #Produccion.objects.filter(fecha__year=ianio) \
                     #       .values('cultivo__nombre') \
                     #       .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField())) \
                     #       .order_by('cultivo__nombre')


    context = {'obj': obj, 'datoLineal':  resultados,
            'datoComparativo': datoComprativo, 'dFecha': dFecha,
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)

@login_required(login_url='/login/')
def proximafechaView(request):
    template_name="proximafecha.html"
    anioactual = datetime.now().year
    dFecha = datetime.now().year

    if request.method == 'POST':
        dFecha = int(request.POST.get("id_anios"))

    tiempobi = int(Parametro.objects.filter(nombreParametro="TIEMPOBI") \
                                .values_list('valorParametro', flat=True) \
                                .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                                .get())
    if tiempobi is None or not tiempobi:
        tiempobi = 180
    
    anios = int(Parametro.objects.filter(nombreParametro="ANIOS") \
                            .values_list('valorParametro', flat=True) \
                            .annotate(valor_parametro=Cast('valorParametro', IntegerField())) \
                            .get())

    ianio = dFecha
    ianio_anterior = ianio-1

    obj =  Produccion.objects.filter(fecha__year=ianio) \
                            .annotate(mes=ExtractMonth('fecha'), anio=ExtractYear('fecha')) \
                            .values('mes', 'anio', 'cultivo__nombre') \
                            .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField()), 
                                      total_venta_cosecha =Sum('cantidadVentaCosecha'),
                                      total_descripcionlote_area =Cast(Sum('descripcionlote__area'),IntegerField())) \
                            .order_by('-total_cosecha')

    # Obtener los datos de la clase Producción
    producciones = Produccion.objects.filter(fecha__gte=datetime.now() - timedelta(days=(tiempobi)))
    # Filtrar los datos para obtener los últimos 180 días
    #df = df[df['fecha'] > (datetime.now() - timedelta(days=180))]

    # Crear un DataFrame con los datos
    df = pd.DataFrame(producciones)


    # Seleccionar las columnas de interés
    df = df[['cultivo', 'fecha', 'cantidadCosecha']]

    # Separar los datos en conjuntos de entrenamiento y prueba
    X = df[['cultivo', 'fecha']]
    y = df['cantidadCosecha']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    # Entrenar el modelo de regresión lineal
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Predecir la cantidad de cosecha futura para cada cultivo
    y_pred = regressor.predict(X_test)

    
    #print('Cantidad de cosecha futura para cada cultivo:')
    #for i in range(len(y_pred)):
    #    print('Cultivo: {}, Cantidad de cosecha futura: {}'.format(X_test.iloc[i]['cultivo'], y_pred[i]))
    obj = {}
    # Agregar los resultados al diccionario
    for i in range(len(y_pred)):
        obj[X_test.iloc[i]['cultivo']] = int(y_pred[i])


    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]

    datoLineal = None #Produccion.objects.filter(fecha__year=ianio) \
                 #           .values('cultivo__nombre') \
                 #           .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField()),
                 #                       total_venta_cosecha=Cast(Sum('cantidadVentaCosecha'),IntegerField())) \
                 #          .order_by('cultivo__nombre')

    datoComprativo = None #Produccion.objects.filter(fecha__year=ianio) \
                     #       .values('cultivo__nombre') \
                     #       .annotate(total_cosecha=Cast(Sum('cantidadCosecha'),IntegerField())) \
                     #       .order_by('cultivo__nombre')


    context = {'obj': obj, 'datoLineal':  datoLineal,
            'datoComparativo': datoComprativo, 'dFecha': dFecha,
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)
