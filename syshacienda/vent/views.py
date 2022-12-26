from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse, reverse_lazy

from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages

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
##  Venta New
class VentaNew(LoginRequiredMixin, generic.CreateView):
    model = Venta
    template_name = "vent/venta_form.html"
    context_object_name =  "obj"
    form_class = VentaForm
    success_url = reverse_lazy("vent:venta_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)
##

class VentaEdit(LoginRequiredMixin, generic.UpdateView):
    model = Venta
    template_name = "vent/venta_form.html"
    context_object_name =  "obj"
    form_class = VentaForm
    success_url = reverse_lazy("vent:venta_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)

## DetalleVenta  ------------------------------------------------------------
class DetalleVentaView(LoginRequiredMixin, generic.ListView):
    model = DetalleVenta
    template_name="vent/venta_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class DetalleVentaNew(LoginRequiredMixin, generic.CreateView):
    model = DetalleVenta
    template_name = "vent/venta_form.html"
    context_object_name =  "obj"
    form_class = DetalleVentaForm
    success_url = reverse_lazy("vent:venta_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class DetalleVentaEdit(LoginRequiredMixin, generic.UpdateView):
    model = DetalleVenta
    template_name = "vent/venta_form.html"
    context_object_name =  "obj"
    form_class = DetalleVentaForm
    success_url = reverse_lazy("vent:venta_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)

class DetalleVentaDel(LoginRequiredMixin, generic.DeleteView):
    model = DetalleVenta
    template_name = "vent/venta_form.html"
    context_object_name =  "obj"
    form_class = DetalleVentaForm
    success_url = reverse_lazy("vent:venta_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)


@login_required(login_url='/login/',)
def Ventas(request, id=None):
    template_name = "vent/venta_form.html"
    detalle =  {}
    clientes = Cliente.objects.filter(estado=True)
    cultivos = Cultivo.objects.filter(estado=True)
    produccion = Produccion.objects.filter(estado=True)
    iva = Parametro.objects.filter(nombreParametro='IVA')
    contexto = {}

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
                'porc_iva':0.00,
                'valor_iva': 0.00
            }
            detalle=None
        else:
            vent_cabecera = {
                'id':venta_cabecera.id,
                'fechaVenta':venta_cabecera.fechaVenta,
                'cliente':venta_cabecera.cliente,
                'totalVenta':venta_cabecera.totalVenta,
                'porc_iva':venta_cabecera.porc_iva,
                'valor_iva':venta_cabecera.valor_iva
            }

        detalle =  DetalleVenta.objects.filter(venta=venta_cabecera)
        contexto = { "venta":vent_cabecera,"det":detalle,"clientes":clientes, "produccion":produccion, "iva": iva }
        return render(request,template_name,contexto)

    if request.method == "POST":
        cliente = request.POST.get("cliente_id")
        fecha  = request.POST.get("fechaVenta")
        cli=Cliente.objects.get(pk=cliente)

        if not id:
            venta_cabecera = Venta(
                cliente = cli,
                fechaVenta = fecha
            )
            if venta_cabecera:
                venta_cabecera.save()
                id = venta_cabecera.id
        else:
            venta_cabecera = Venta.objects.filter(pk=id).first()
            if venta_cabecera:
                venta_cabecera.cliente = cli
                venta_cabecera.save()

        if not id:
            messages.error(request,'No Puedo Continuar No Pude Detectar No. de Factura')
            return redirect("vent:venta_list")

        produccion_id = request.POST.get("produccion_id")
        cantidad = request.POST.get("cantidad")
        precio = request.POST.get("precio")
        #s_total = request.POST.get("sub_total_detalle")
        #descuento = request.POST.get("descuento_detalle")
        total = request.POST.get("total_detalle")

        prod = Produccion.objects.get(pk=produccion_id)
        det = DetalleVenta(
            venta = venta_cabecera,
            produccion = produccion,
            cantidad = cantidad,
            precio = precio,
            #sub_total = s_total,
            #descuento = descuento,
            total = total
        )

        if det:
            det.save()

        return redirect("vent:venta_edit",id=id)
    return render(request,template_name,contexto)

class ProduccionView(ProduccionView):
    template_name="vent/venta_busca_produccion.html" 
