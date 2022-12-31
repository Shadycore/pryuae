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

from vent.models import Venta, DetalleVenta
from vent.forms import VentaForm,DetalleVentaForm
from mnt.models import Cliente, Cosecha, Produccion, Cultivo, Parametro
from mnt.views import ProduccionView, ParametroView
from django.db.models import Q

## Venta  ------------------------------------------------------------
class VentaView(LoginRequiredMixin, generic.ListView):
    model = Venta
    template_name="vent/venta_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

    def get_queryset(self):
        return super().get_queryset()
        #return Venta.objects.all()

@login_required(login_url='/login/')
def ventasView(request, id=None):
    template_name = "vent/venta_form.html"
    clientes = Cliente.objects.filter(estado=True)
    #cultivos = Cultivo.objects.filter(estado=True)
    produccion = Produccion.objects.filter(estado=True)
    contexto = {}

    if request.method == "GET":
        venta_cabecera = Venta.objects.filter(pk=id).first()
        if id:
            if not venta_cabecera:
                messages.error(request,'Factura No Existe')
                return redirect("vent:venta_list")

        if not venta_cabecera:
            porciva = Parametro.objects.filter(nombreParametro='IVA').first()
            iIva = float(porciva.valorParametro)
            cabecera = {
                'id':0,
                'fechaVenta':datetime.today(),
                'cliente':0,
                'totalVenta':0.00,
                'subTotal': 0.00,
                'porcIva':iIva,
                'totalIva': 0.00,
                'usuarioCreacion': request.user
            }
            detalle=None  
        else:

            cabecera = {
                'id':venta_cabecera.id,
                'fechaVenta':venta_cabecera.fechaVenta,
                'cliente':venta_cabecera.cliente,
                'totalVenta':venta_cabecera.totalVenta,
                'subTotal': venta_cabecera.subTotal,
                'porcIva':venta_cabecera.porcIva,
                'totalIva':venta_cabecera.totalIva
            }

            detalle =  DetalleVenta.objects.filter(venta=venta_cabecera)
        contexto = { "venta":cabecera, "det":detalle,
                    "clientes":clientes,  "produccion":produccion }
        return render(request,template_name,contexto)

    if request.method == "POST":
        cliente = request.POST.get("id_cliente_detalle")
        fechaVenta  = request.POST.get("id_fechaVenta")
        cli = Cliente.objects.get(pk=cliente)     
        produccion_id = request.POST.get("cod_produccion")     
        cultivo_id = request.POST.get("cod_cultivo")
        porciva = request.POST.get("id_porciva")

        if not id:
            cabecera = Venta(
                cliente = cli,
                fechaVenta = fechaVenta,
                usuarioCreacion = request.user
            )
            if cabecera:
                cabecera.save()
                id = cabecera.id
        else:
            cabecera = Venta.objects.filter(pk=id).first()
            if cabecera:
                cabecera.cliente = cli
                cabecera.usuarioCreacion = request.user
                cabecera.porcIva = porciva 
                cabecera.save()

        if not id:
            messages.error(request,'No Puedo Continuar No Pude Detectar No. de Factura')
            return redirect("vent:venta_list")

        cantidad = request.POST.get("id_cantidad")
        precio = request.POST.get("id_precio")
        total = request.POST.get("id_total")

        prod = Produccion.objects.get(pk=produccion_id)
        cult = Cultivo.objects.get(pk=cultivo_id)
        det = DetalleVenta(
                venta = cabecera,
                produccion = prod,
                cultivo = cult,
                cantidad = cantidad,
                precio = precio,
                total = total,
                usuarioCreacion = request.user
                )

        if det:
            det.save()

        return redirect('vent:venta_edit',id)

    #return render(request,template_name,contexto)


class ProduccionView(LoginRequiredMixin, generic.ListView):
    template_name="vent/busca_produccion.html" 


def borrar_detalle_factura(request, id):
    template_name = "fac/factura_borrar_detalle.html"

    det = DetalleVenta.objects.get(pk=id)

    if request.method=="GET":
        context={"det":det}

    if request.method == "POST":
        usr = request.POST.get("usuario")
        pas = request.POST.get("pass")

        user =authenticate(username=usr,password=pas)

        if not user:
            return HttpResponse("Usuario o Clave Incorrecta")
        
        if not user.is_active:
            return HttpResponse("Usuario Inactivo")

        if user.is_superuser or user.has_perm("fac.sup_caja_facturadet"):
            det.id = None
            det.cantidad = (-1 * det.cantidad)
            #det.sub_total = (-1 * det.sub_total)
            #det.descuento = (-1 * det.descuento)
            det.total = (-1 * det.total)
            det.save()

            return HttpResponse("ok")

        #return HttpResponse("Usuario no autorizado")
    
    return render(request,template_name,context)