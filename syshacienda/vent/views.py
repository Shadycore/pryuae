from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from vent.models import Venta, DetalleVenta
from vent.forms import VentaForm,DetalleVentaForm
from mnt.models import Cliente, Cosecha, Produccion, Cultivo

## Venta  ------------------------------------------------------------
class VentaView(LoginRequiredMixin, generic.ListView):
    model = Venta
    template_name="vent/venta_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

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
    template_name="vent/detalleventa_list.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class DetalleVentaNew(LoginRequiredMixin, generic.CreateView):
    model = DetalleVenta
    template_name = "vent/detalleventa_form.html"
    context_object_name =  "obj"
    form_class = DetalleVentaForm 
    success_url = reverse_lazy("vent:detalleventa_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioCreacion = self.request.user
        return super().form_valid(form)

class DetalleVentaEdit(LoginRequiredMixin, generic.UpdateView):
    model = DetalleVenta
    template_name = "vent/detalleventa_form.html"
    context_object_name =  "obj"
    form_class = DetalleVentaForm 
    success_url = reverse_lazy("vent:detalleventa_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)

class DetalleVentaDel(LoginRequiredMixin, generic.DeleteView):
    model = DetalleVenta
    template_name = "vent/detalleventa_form.html"
    context_object_name =  "obj"
    form_class = DetalleVentaForm 
    success_url = reverse_lazy("vent:detalleventa_list")
    login_url = "baseapp:login"

    def form_valid(self, form):
        form.instance.usuarioModificacion = self.request.user.id
        return super().form_valid(form)


