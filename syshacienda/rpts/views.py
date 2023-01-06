from django.db import models
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse, reverse_lazy


from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate

from mnt.views import ClienteView, CultivoView, ProduccionView, \
                            HaciendaView, EmpleadoNew, AsignacionView, \
                            ProveedorNew, RegistroInsumoNew
from mnt.models import Cliente, Cultivo, Produccion, \
                        Hacienda, Empleado, Asignacion, \
                        Proveedor, RegistroInsumo, Insumo
from vent.views import ventasView, VentaView
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
def iComprasView(request,f1=None,f2=None):    
    template_name="rpts/iCompras.html"
    dFecha = datetime.datetime.now()

    if request.method == 'POST':
        if f1 is not None and f2 is not None:
            dFecha = parse_date(f1)
    
    ianio = dFecha.year()
    ianio_anterior = ianio-1
    obj = RegistroInsumo.objects.all().order_by('-id')
    ##get('total',0.00) 
    datoLineal = RegistroInsumo.objects.filter('fechaCompra__year = ' + ianio) \
                    .annotate('fechaCompra__month') \
                    .aggregate(total=sum(precio),
                            output_field=models.FloatField()) \
                    .order_by('fechaCompra__month')

 
    datoLineal2 = RegistroInsumo.objects\
                    .filter('fechaCompra__year = ' + ianio) \
                    .values('fechaCompra__month') \
                    .annotate(total=sum(precio),
                                output_field=models.FloatField()) \
                    .order_by('fechaCompra__month')

    datoComprativo = RegistroInsumo.objects\
                    .filter('fechaCompra__year = ' + ianio_anterior) \
                    .values('fechaCompra__month') \
                    .annotate(total=sum(precio)) \
                    .order_by('fechaCompra__month')

    return render(request,
                    template_name,
                    obj,
                    datoLineal,
                    datoLineal2,
                    datoComprativo,
                    dFecha,
                    ianio)
