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
                        Proveedor, RegistroInsumo
from vent.views import ventasView, VentaView
# Create your views here.


class iProveedoresView(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name="rpts/iProveedores.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class iClientesView(LoginRequiredMixin, generic.ListView):
    model = Cliente
    template_name="rpt/iClientes.html"
    context_object_name = "obj"
    login_url = "baseapp:login"

class iComprasView(LoginRequiredMixin, generic.ListView):
    model = RegistroInsumo
    template_name="rpt/iCompras.html"
    context_object_name = "obj"
    login_url = "baseapp:login"