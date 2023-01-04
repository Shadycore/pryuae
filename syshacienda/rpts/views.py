from django.shortcuts import render
from mnt.views import ClienteView, CultivoView, ProduccionView, HaciendaView, EmpleadoNew, AsignacionView
from vent.views import ventasView, VentaView
# Create your views here.


#Vista para clientes
class EmpleadosView(EmpleadosView):
    template_name = 'rpt/rpt_empleados.html'

