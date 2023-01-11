from django.db import models
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.db.models import Sum, F, DateTimeField, Count, FloatField, IntegerField, Prefetch, Case, When
from datetime import datetime, timezone
from django.db.models.functions import TruncMonth, TruncYear, ExtractMinute, ExtractMonth, ExtractYear, Cast, Coalesce
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
# Create your views here.


class iProveedoresView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name="rpts/iProveedores.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class iClientesView(LoginRequiredMixin, generic.ListView):
    model = Cliente
    template_name="rpts/iClientes.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class iComprasView_(LoginRequiredMixin, generic.ListView):
    model = RegistroInsumo
    template_name="rpt/iCompras.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

@login_required(login_url='/login/')
def iComprasView(request):
    template_name="rpts/iCompras.html"
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
                                    insumo_name=F('insumo__nombre')) \
                        .values('anio','month', 'insumo_name') \
                        .annotate(total_compras=Sum('precio')) \
                        .order_by('anio','month')
                        
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
                                .filter(fechaCompra__year=ianio_anterior) \
                                .annotate(month=ExtractMonth('fechaCompra'), year=ExtractYear('fechaCompra')) \
                                .values('month', 'year') \
                                .annotate(total=Cast(Sum('precio'), IntegerField())) \
                                .order_by('month')
    
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

    for item in datoComprativo:
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
    salida2 = [dato2[key] for key in dato2]

    context = {'obj': obj, 'datoLineal':  salida1, 
            'datoComparativo': salida2, 'dFecha': dFecha, 
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)


@login_required(login_url='/login/')
def oProduccionView(request):
    template_name="rpts/oProduccionPorHALote.html"
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
                            .values('mes', 'anio', 'cultivo__nombre', 'descripcionlote__area', 'descripcionlote__etapa') \
                            .annotate(total_cosecha=Sum('cantidadCosecha'),total_venta_cosecha=Sum('cantidadVentaCosecha')) \
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
def oProductosMasVendidosView(request):
    template_name="rpts/oProductosMasVendidos.html"
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
                .annotate(cantidad=Count('detalleventa__cultivo'), det_total=Sum('detalleventa__total'), det_cantidad=Sum('detalleventa__cantidad')) \
                .order_by('-cantidad') \
                .aggregate(cantidad=Coalesce(Count('detalleventa__cultivo'), 0), 
                det_total=Coalesce(Sum('detalleventa__total'), 0), 
                det_cantidad=Coalesce(Sum('detalleventa__cantidad'), 0))

    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]
        
    datoLineal = ventas.values('fechaVenta__year', 'detalleventa__cultivo__nombre') \
                .annotate(cantidad=Count('detalleventa__cultivo'), det_total=Cast(Sum('detalleventa__total'),IntegerField()), det_cantidad=Cast(Sum('detalleventa__cantidad'),IntegerField())) \
                .order_by('-cantidad') \
                .aggregate(cantidad=Coalesce(Count('detalleventa__cultivo'), 0), 
                det_total=Coalesce(Cast(Sum('detalleventa__total'),IntegerField()), 0), 
                det_cantidad=Coalesce(Cast(Sum('detalleventa__cantidad'),IntegerField()), 0))


    cultivos = [item['detalleventa__cultivo__nombre'] for item in datoLineal]
    ventas_com = Venta.objects.filter(fechaVenta__year=ianio_anterior)
    datoComprativo = ventas_com.values('fechaVenta__year', 'detalleventa__cultivo__nombre') \
                .annotate(cantidad=Count('detalleventa__cultivo'), det_total=Cast(Sum('detalleventa__total'),IntegerField()), det_cantidad=Cast(Sum('detalleventa__cantidad'),IntegerField())) \
                .order_by('-cantidad') \
                .aggregate(cantidad=Coalesce(Count('detalleventa__cultivo'), 0), 
                det_total=Coalesce(Cast(Sum('detalleventa__total'),IntegerField()), 0), 
                det_cantidad=Coalesce(Cast(Sum('detalleventa__cantidad'),IntegerField()), 0))
        
    context = {'obj': obj, 'datoLineal':  datoLineal, 
            'datoComparativo': datoComprativo, 'dFecha': dFecha, 
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)

@login_required(login_url='/login/')
def oVentasPorCultivoView(request):
    template_name="rpts/oVentasPorCultivo.html"
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
                .annotate(cantidad=Count('detalleventa__cultivo'), det_total=Sum('detalleventa__total'), det_cantidad=Sum('detalleventa__cantidad')) \
                .order_by('-cantidad') \
                .aggregate(cantidad=Coalesce(Count('detalleventa__cultivo'), 0), 
                det_total=Coalesce(Sum('detalleventa__total'), 0), 
                det_cantidad=Coalesce(Sum('detalleventa__cantidad'), 0))
                        
    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]
    
    datoLineal = ventas.values('fechaVenta__year', 'detalleventa__cultivo__nombre') \
                .annotate(cantidad=Count('detalleventa__cultivo'), det_total=Cast(Sum('detalleventa__total'),IntegerField()), det_cantidad=Cast(Sum('detalleventa__cantidad'),IntegerField())) \
                .order_by('-cantidad') \
                .aggregate(cantidad=Coalesce(Count('detalleventa__cultivo'), 0), 
                det_total=Coalesce(Cast(Sum('detalleventa__total'),IntegerField()), 0), 
                det_cantidad=Coalesce(Cast(Sum('detalleventa__cantidad'),IntegerField()), 0))
    
    cultivos = [item['detalleventa__cultivo__nombre'] for item in datoLineal ]
    ventas_com = Venta.objects.filter(fechaVenta__year=ianio_anterior)
    datoComprativo = ventas_com.values('fechaVenta__year', 'detalleventa__cultivo__nombre') \
                .annotate(cantidad=Count('detalleventa__cultivo'), det_total=Cast(Sum('detalleventa__total'),IntegerField()), det_cantidad=Cast(Sum('detalleventa__cantidad'),IntegerField())) \
                .order_by('-cantidad') \
                .aggregate(cantidad=Coalesce(Count('detalleventa__cultivo'), 0), 
                det_total=Coalesce(Cast(Sum('detalleventa__total'),IntegerField()), 0), 
                det_cantidad=Coalesce(Cast(Sum('detalleventa__cantidad'),IntegerField()), 0))
    
   
    context = {'obj': obj, 'datoLineal':  datoLineal, 
            'datoComparativo': datoComprativo, 'dFecha': dFecha, 
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)

@login_required(login_url='/login/')
def oGananciasView(request):
    template_name="rpts/oGanancias.html"
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

    obj =    Produccion.objects.filter(fecha__year=YEAR) \
                                .values('cultivo__nombre', 'fecha__year') \
                                .annotate(sum_cantidadCosecha=Sum('cantidadCosecha'))
    

    oanios = [i for i in range(anioactual,(anioactual - anios),-1)]
    
    datoLineal =  DetalleVenta.objects.filter(venta__fechaVenta__year=ianio, cultivo__nombre__in=obj.values('cultivo__nombre')) \
                                        .values('venta__fechaVenta__year') \
                                        .annotate(sum_total=Cast(Sum('total'),IntegerField()), sum_cantidad=Cast(Sum('cantidad'),IntegerField()))
    
    cultivos =[item['detalleventa__cultivo__nombre'] for item in datoLineal ]

    datoComprativo = RegistroInsumo.objects.filter(cultivo__nombre__in=producciones.values('cultivo__nombre')) \
                                            .values('fechaCompra__year', 'insumo__nombre') \
                                            .annotate(precio=Cast(Sum('precio'),IntegerField()))
    
   resultado = obj.annotate(
    precio_insumo=Sum(Case(
                    When(cultivo__nombre=datoComprativo.values('cultivo__nombre'), then='registro_insumos__precio')
                    )),
    total_ventas=Sum(Case(
                    When(cultivo__nombre=datoLineal.values('cultivo__nombre'), then='detalle_ventas__total')
                    ))).values('cultivo__nombre', 'fecha__year', 'cantidadCosecha', 'precio_insumo', 'total_ventas')

    context = {'obj': obj, 'datoLineal':  datoLineal, 
            'datoComparativo': datoComprativo, 'dFecha': dFecha, 
            'ianio': ianio, 'ianio_anterior':ianio_anterior,
            'anios': oanios}

    return render(request,
                    template_name,
                    context)