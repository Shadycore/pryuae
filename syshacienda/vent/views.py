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

## Venta  ------------------------------------------------------------
class VentaView(LoginRequiredMixin, generic.ListView):
    model = Venta
    template_name="vent/venta_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

    def get_queryset(self):
        return super().get_queryset()
        #return Venta.objects.all()



@login_required(login_url='/login/',)
def Ventas(request, id=None):
    template_name = "vent/venta_form.html"
    clientes = Cliente.objects.filter(estado=True)
    cultivos = Cultivo.objects.filter(estado=True)
    produccion = Produccion.objects.filter(estado=True)
    iva = Parametro.objects.filter(nombreParametro='IVA')
    contexto = {}
    detalle =  {}

    if request.method == "GET":
        venta_cabecera = Venta.objects.filter(pk=id).first()
        if id:
            if not venta_cabecera:
                messages.error(request,'Factura No Existe')
                return redirect("vent:venta_list")

            #usr = request.user
            #if not usr.is_superuser:
            #    if venta_cabecera.uc != usr:
            #        messages.error(request,'Factura no fue creada por usuario')
            #        return redirect("vent:venta_list")

        if not venta_cabecera:
            vent_cabecera = {
                'id':0,
                'fechaVenta':datetime.today(),
                'cliente':0,
                'totalVenta':0.00,
                'subTotal': 0.00,
                'porcIva':0.00,
                'totalIva': 0.00,
                'usuarioCreacion': request.user
            }
            detalle=None
        else:
            vent_cabecera = {
                'id':venta_cabecera.id,
                'fechaVenta':venta_cabecera.fechaVenta,
                'cliente':venta_cabecera.cliente,
                'totalVenta':venta_cabecera.totalVenta,
                'subTotal': venta_cabecera.subTotal,
                'porcIva':venta_cabecera.porcIva,
                'totalIva':venta_cabecera.totalIva
            }

        detalle =  DetalleVenta.objects.filter(venta=venta_cabecera)
        contexto = { "venta":vent_cabecera,
                     "det":detalle,
                    "clientes":clientes,
                    "produccion":produccion, 
                    "iva": iva }
        return render(request,template_name,contexto)

    if request.method == "POST":
        cliente = request.POST.get("id_cliente")
        fecha  = request.POST.get("id_fechaVenta")
        cli=Cliente.objects.get(pk=cliente)

        if not id:
            venta_cabecera = Venta(
                cliente = cli,
                fechaVenta = fecha,
                usuarioCreacion = request.user
            )
            if venta_cabecera:
                venta_cabecera.save()
                id = venta_cabecera.id
        else:
            venta_cabecera = Venta.objects.filter(pk=id).first()
            if venta_cabecera:
                venta_cabecera.cliente = cli
                venta_cabecera.usuarioCreacion = request.user
                venta_cabecera.save()

        if not id:
            messages.error(request,'No Puedo Continuar No Pude Detectar No. de Factura')
            return redirect("vent:venta_list")

        produccion_id = request.POST.get("id_produccion")
        cantidad = request.POST.get("id_cantidad")
        precio = request.POST.get("id_precio")
        total = request.POST.get("id_total")

        prod = Produccion.objects.get(pk=produccion_id)
        det = DetalleVenta(
            venta = venta_cabecera,
            produccion = produccion,
            cantidad = cantidad,
            precio = precio,
            total = total
        )

        if det:
            det.save()

        return redirect("vent:venta_edit",id=id)
    return render(request,template_name,contexto)

class ProduccionView(LoginRequiredMixin, generic.ListView):
    template_name="vent/busca_produccion.html" 
    model = Produccion
    context_object_name = "obj"